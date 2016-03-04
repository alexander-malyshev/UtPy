import os
import shutil
import sys

# This method performs two-way recursive synchronization of a pair folders.
def DateSync(aSourceFolder1, aSourceFolder2):
   folders = os.listdir(aSourceFolder1)
   folders.sort(key=lambda x: os.stat(os.path.join(aSourceFolder1, x)).st_ctime)
   for folder in folders:
      # print folder;
      src = os.path.join(aSourceFolder1, folder)
      dst = os.path.join(aSourceFolder2, folder)
      shutil.copytree(src, dst)


if len(sys.argv) != 3:
  print("Usage: TwoWaySync srcFolder1 srcFolder2")
  exit(1)

aSrcFolder1 = sys.argv[1]
aSrcFolder2 = sys.argv[2]

#DateSync(aSrcFolder1, aSrcFolder2)