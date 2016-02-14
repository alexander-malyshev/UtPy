import os

anExtensionsList = {"c", "cpp", "h", "hxx", "lxx", "hpp", "cxx", "py"}

# recursive function to compute the code values.
def Count(thePath,
          theSize,
          theLinesNb):
  aDirPaths = os.listdir(thePath)
  for anEntry in aDirPaths:
    aPath = os.path.join(thePath, anEntry)
    if os.path.isfile(aPath):
      anExtension = aPath.split(".")[-1]
      if anExtension in anExtensionsList:
        theSize += os.path.getsize(aPath)
        theLinesNb += sum(1 for line in open(aPath, "r"))
    elif os.path.isdir(aPath):
      aCurSize, aCurLinesNb = Count(aPath, 0, 0)
      theSize += aCurSize
      theLinesNb += aCurLinesNb
    else:
      print("What should we do with a {}? It's not a file or a directory?".format(aPath))

  return theSize, theLinesNb


aRootPath = input("Please input root path: ")

aSize, aLinesNb = 0, 0
aSize, aLinesNb = Count(aRootPath, aSize, aLinesNb)

print("The Code size is [KiB]:", aSize / 1024)
print("The total number of lines is [thousands]:", (aLinesNb / 1000))
