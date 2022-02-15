import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

print(hdir)

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')
print(pattern)

# TODO: Use the glob.glob() function to obtain the list of filenames
file_names = glob.glob(pattern)

# TODO: use os.path.getsize to find each file's size
for file in file_names:
    os.path.getsize(file)

# TODO: Add a test to only display files that are not zero length
size = 0

for file in file_names:
    size = os.path.getsize(file)
    if size > 0:
        print(file)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
for file in os.scandir(hdir):
    size += os.path.getsize(file)
    if size > 0:
        print(os.path.basename(file))
