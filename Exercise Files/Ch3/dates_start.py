#
# Example file for working with date information
#


def main():
    # DATE OBJECTS
    from datetime import datetime
    # Get today's date from the simple today() method from the date class
    today = datetime.today()
    print(today)
    # print out the date's individual components
    print(today.year)
    print(today.month)
    print(today.day)
    # retrieve today's weekday (0=Monday, 6=Sunday)
    wd = {0: 'Monday', 1: 'tuesday', 2: 'wednesday',
          3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'saturday'}
    print(wd[today.weekday()])

    # DATETIME OBJECTS
    # Get today's date from the datetime class
    print(today.date())
    # Get the current time
    print(today.now())


if __name__ == "__main__":
    main()
