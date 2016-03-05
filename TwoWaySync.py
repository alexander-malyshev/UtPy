import os
import shutil
import sys

# This method performs two-way recursive synchronization of a pair of folders.
def DateSync(aSourceFolder1, aSourceFolder2):
   aFolders1 = os.listdir(aSourceFolder1)
   aFolders1.sort(key=lambda x: os.stat(os.path.join(aSourceFolder1, x)).st_mtime)

   aFolders2 = os.listdir(aSourceFolder2)
   aFolders2.sort(key=lambda x: os.stat(os.path.join(aSourceFolder2, x)).st_mtime)

   for aFolder in aFolders1:
      aSrc = os.path.join(aSourceFolder1, aFolder)
      aDst = os.path.join(aSourceFolder2, aFolder)
      if os.path.isdir(aSrc):
        print("Forward  sync: {}".format(aSrc))

      # Recursive call on level deeper.
      if aFolder in aFolders2 and os.path.isdir(aSrc):
        DateSync(aSrc, aDst)
        continue
      if aFolder not in aFolders2 and os.path.isdir(aSrc):
        os.mkdir(aDst)
        DateSync(aSrc, aDst)
        continue

      # Synchronize files. Choose which is more "fresh".
      if aFolder in aFolders2 and os.path.isfile(aSrc):
        aTime1 = os.path.getmtime(aSrc)
        aTime2 = os.path.getmtime(aDst)
        if aTime1 > aTime2:
          print("  File {} is out of date".format(aSrc))
          shutil.copyfile(aSrc, aDst)
          aTime2 = os.path.getmtime(aDst)
          os.utime(aSrc, (aTime2, aTime2))

      # Dir not found in another list.
      if aFolder not in aFolders2 and os.path.isdir(aSrc):
        print("  File {} is out of date".format(aSrc))
        os.mkdir(aDst)
        shutil.copytree(aSrc, aDst)
        aTime2 = os.path.getmtime(aDst)
        os.utime(aSrc, (aTime2, aTime2))

      # File not found in another list.
      if aFolder not in aFolders2 and os.path.isfile(aSrc):
        print("  File {} is out of date".format(aSrc))
        shutil.copyfile(aSrc, aDst)
        aTime2 = os.path.getmtime(aDst)
        os.utime(aSrc, (aTime2, aTime2))

   for aFolder in aFolders2:
      aSrc = os.path.join(aSourceFolder2, aFolder)
      aDst = os.path.join(aSourceFolder1, aFolder)
      if os.path.isdir(aSrc):
        print("Backward sync: {}".format(aSrc))

      # Recursive call on level deeper.
      if aFolder in aFolders1 and os.path.isdir(aSrc):
        DateSync(aSrc, aDst)
        continue
      if aFolder not in aFolders1 and os.path.isdir(aSrc):
        os.mkdir(aDst)
        DateSync(aSrc, aDst)
        continue

      # Synchronize files. Choose which is more "fresh".
      if aFolder in aFolders1 and os.path.isfile(aSrc):
        aTime1 = os.path.getmtime(aSrc)
        aTime2 = os.path.getmtime(aDst)
        if aTime1 > aTime2:
          print("  File {} is out of date".format(aSrc))
          shutil.copyfile(aSrc, aDst)
          aTime2 = os.path.getmtime(aDst)
          os.utime(aSrc, (aTime2, aTime2))

      # Dir not found in another list.
      if aFolder not in aFolders1 and os.path.isdir(aSrc):
        print("  File {} is out of date".format(aSrc))
        os.mkdir(aDst)
        shutil.copytree(aSrc, aDst)
        aTime2 = os.path.getmtime(aDst)
        os.utime(aSrc, (aTime2, aTime2))

      # File not found in another list
      if aFolder not in aFolders1 and os.path.isfile(aSrc):
        print("  File {} is out of date".format(aSrc))
        shutil.copyfile(aSrc, aDst)
        aTime2 = os.path.getmtime(aDst)
        os.utime(aSrc, (aTime2, aTime2))

if len(sys.argv) != 3:
  print("Usage: TwoWaySync srcFolder1 srcFolder2")
  exit(1)

aSrcFolder1 = sys.argv[1]
aSrcFolder2 = sys.argv[2]

if not os.path.isdir(aSrcFolder1):
      os.mkdir(aSrcFolder1)
if not os.path.isdir(aSrcFolder2):
      os.mkdir(aSrcFolder2)

DateSync(aSrcFolder1, aSrcFolder2)