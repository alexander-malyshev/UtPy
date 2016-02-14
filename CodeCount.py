import os

anExtensionsList = {"c", "cpp", "h", "hxx", "lxx", "hpp", "cxx", "py"}

# recursive function to compute the code values.
def Count(thePath,
          theSize,
          theLinesNb):
  aDirList = os.listdir(thePath)
  for aDir in aDirList:
    aPath = os.path.join(thePath, aDir)
    if not os.path.isdir(aPath):
      continue
    aCurSize, aCurLinesNb = Count(aPath, 0, 0)
    theSize += aCurSize
    theLinesNb += aCurLinesNb

  for aFile in aDirList:
    aPath = os.path.join(thePath, aFile)
    if not os.path.isfile(aPath):
      continue

    anExtension = aPath.split(".")[-1]
    if anExtension in anExtensionsList:
      theSize += os.path.getsize(aPath)
      theLinesNb += sum(1 for line in open(aPath, "r"))

  return theSize, theLinesNb


aRootPath = input("Please input root path: ")

aSize, aLinesNb = 0, 0
aSize, aLinesNb = Count(aRootPath, aSize, aLinesNb)

print("The Code size is [KiB]:", aSize / 1024)
print("The total number of lines is [thousands]:", (aLinesNb / 1000))
