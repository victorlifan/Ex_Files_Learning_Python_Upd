#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2021, 6, 0)
print(str)
# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
print(hc.formatmonth(2021, 1))
# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2021, 6):
    print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for i in calendar.month_name:
    print(i)
for i in calendar.day_name:
    print(i)
# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for i in range(1, 13):
    #c = calendar.TextCalendar()
    mo = calendar.monthcalendar(2017, i)
    w1 = mo[0]
    w2 = mo[1]
    if w1[calendar.FRIDAY] != 0:
        print(w1[calendar.FRIDAY])
    else:
        print(w2[calendar.FRIDAY])
