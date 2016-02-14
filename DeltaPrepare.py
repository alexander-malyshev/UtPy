# This script prepare delta for x last commits in git
import git
import shutil
import os

# Take input data.
aRepoPath = input("Please input repository path: ")
aRepoPath = os.path.normpath(aRepoPath)
aNb = int(input("Please input number of commits to take: "))

# Iterate over last commits and prepare delta content.
aRepo = git.Repo(aRepoPath)
aComList = list(aRepo.iter_commits())
aFilesList = list()
for i in range(0, aNb):
  for aDiff in aComList[0 + i].diff(aComList[1 + i]):
    if aDiff.a_blob.path not in aFilesList:
      aFilesList.append(os.path.normpath(aDiff.a_blob.path))

# Copy files to store directory order.
aResPath = input("Please input result folder to store delta: ")
aResPath = os.path.normpath(aResPath)
for aFileDeltaPath in aFilesList:
  anInpPath = os.path.join(aRepoPath, aFileDeltaPath)
  aDestPath = os.path.join(aResPath, aFileDeltaPath)

  # Create sub directories for current file.
  aSplitList = aDestPath.split(os.sep)
  aString = aSplitList[0] + os.sep
  for aToken in aSplitList[1:-1]:
    aString = os.path.join(aString, aToken)
    if not os.path.isdir(aString):
      os.mkdir(aString)

  # Copy file.
  shutil.copyfile(anInpPath, aDestPath)


