#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from zipfile import ZipFile


def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath('textfile.txt')

        # let's make a backup copy by appending "bak" to the name
        shutil.copy(src, src+'.bak')
        # copy over the permissions, modification times, and other info
        shutil.copystat(src, src+'.bak')
        # rename the original file
        os.rename('textfile.txt', 'newfile.txt')
        # now put things into a ZIP archive
        root_dir, name = path.split(src)
        #print(root_dir, name)
        #shutil.make_archive('archive', 'zip', root_dir)
        # more fine-grained control over ZI,P files
        with ZipFile('testzip.zip', 'w') as zp:
            zp.write('newfile.txt')
            zp.write('textfile.txt.bak')


if __name__ == "__main__":
    main()
