#
# Example file for working with loops
#

def main():
    x = 0

    # define a while loop
    # while x <= 5:
    # print(x)
    #    x += 1
    # print(x)
    # define a for loop
    # for i in range(5):
    #    x += 1
    # print(x)
    # use a for loop over a collection

    # use the break and continue statements
    while True:
        x += 1
        if x > 10:
            break
        elif x == 2 or x % 2 != 0:
            print(x)
        else:
            continue

# using the enumerate() function to get index
    for i, n in enumerate(range(1, 10)):
        print(i, n)


if __name__ == "__main__":
    main()
