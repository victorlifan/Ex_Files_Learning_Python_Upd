#
# Read and write files using the built-in Python file methods
#

def main():
    # Open a file for writing and create it if it doesn't exist
    with open("textfile.txt", "w+") as w:

        # Open the file for appending text to the end
        # with open("testfile.txt","") as a:

        # write some lines of data to the file
        for i in range(3):
            w.write(f"line {i}\n")

    # close the file when done
    # w.close()

    # Open the file back up and read the contents
    with open("textfile.txt", "r") as r:
        print(r.mode)
        print(r.read())


if __name__ == "__main__":
    main()
