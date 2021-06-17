#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print("if file exists:", path.exists('textfile.txt'))
    print("item is a file:", path.isfile('textfile.txt'))
    print("item is a directory", path.isdir("textfile.txt"))

    # Work with file paths
    print(path.realpath('textfile.txt'))
    print(path.split(path.realpath('textfile.txt')))

    # Get the modification time
    mtime = datetime.datetime.fromtimestamp(path.getmtime(
        'textfile.txt')).strftime('%Y %B %d %A %H:%M:%S')
    print(mtime)
    # Calculate how long ago the item was modified
    print(datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime('textfile.txt')))


if __name__ == "__main__":
    main()
