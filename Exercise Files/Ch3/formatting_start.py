#
# Example file for formatting time and date output
#

from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()
    print(now)
    #### Date Formatting ####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime('now is %Y %A %B %d'))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("locale's date is %c"))
    print(now.strftime("date is %X"))
    print(now.strftime("%x"))
    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("%H %M %S %p"))


if __name__ == "__main__":
    main()
