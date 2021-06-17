#
# Example file for working with conditional statements
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if x < y:
        print('x is smaller than y')
    elif x == y:
        print("x is equal to y")
    else:
        print('x is greater than y')
    # conditional statements let you use "a if C else b"
    st = 'x is smaller or equal to y' if x <= y else 'x is greater than y'
    print(st)


if __name__ == "__main__":
    main()
