import os
import fileinput

anExtensionsList = {"html"}

# recursive function to compute the reference values.
def CreateReference(thePath,
                    theResFile,
                    theThresholdVal):
  aDirPaths = os.listdir(thePath)
  for anEntry in aDirPaths:
    aPath = os.path.join(thePath, anEntry)
    if os.path.isfile(aPath):
      anExtension = aPath.split(".")[-1]
      
      # Check extension.
      if anExtension not in anExtensionsList:
        continue

      # Check lines
      for line in fileinput.input(aPath):
       if "Final Hausdorff deviation is" not in line:
         continue
         
       print(aPath)
       
       aCurrentVal = 0.0
       try:
         aCurrentVal = float(line.split(" ")[-1])
       except :
         pass

       # Print result in file
       if aCurrentVal > theThresholdVal:
         # Create result string
         aString = aPath.split(os.path.sep)[-2]
         aString = aString + " -> "
         aString = aString + (aPath.split(os.path.sep)[-1]).split(".")[0]
         aString = aString + " -> "
         aString = aString + str(aCurrentVal)
         aString = aString + "\n"
         
         theResFile.write(aString)
    elif os.path.isdir(aPath):
      CreateReference(aPath, theResFile, theThresholdVal)

  return


aRootPath = input("Please input root path: ")
aResPath = input("Please input path to store result: ")
aThreshold = input("Please input path to threshold value: ")

# Delete file if exists.
try:
    os.remove(aResPath)
except OSError:
    pass

# Open or create result file.
aFileDescriptor = open(aResPath, 'w')
CreateReference(aRootPath, aFileDescriptor, float(aThreshold))

aFileDescriptor.close()
