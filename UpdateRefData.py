import os
import fileinput

# Function which updates reference value.
def UpdateByReferenceValue(file, value, inc):
  newLine = "thull_compare_contours c res 1.0 " + str(value + inc) + "\n"
  for line in fileinput.input(file, inplace = True):
    if "thull_compare_contours" in line:
      print(newLine, end = '')
      continue
    print(line, end = '')

# Reference file
aReferanceFile = input("Please set reference file: ")

# Reference path to the tests
aTestRootPath = input("Please set root path for tests: ")
aTestRootPath = os.path.join(aTestRootPath, "draw")
aTestRootPath = os.path.join(aTestRootPath, "hull")

aFile = open(aReferanceFile, "r")

for line in aFile:
  aSubDir = line.split(" ")[0]
  aSubFile = line.split(" ")[2]
  aValue = float((line.split(" ")[4]).split("\n")[0])

  aPath = os.path.join(aTestRootPath, aSubDir)
  aPath = os.path.join(aPath, aSubFile)
  os.path.normpath(aPath)
  
  # Increase by 0.01
  UpdateByReferenceValue(aPath, aValue, 0.01)

aFile.close()


