#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime, timedelta

# construct a basic timedelta and print it
timedelta(days=365, hours=5, minutes=1)

# print today's date
today = datetime.now().date()
print(today)
# print today's date one year from now
print(today+timedelta(days=365))

# create a timedelta that uses more than one argument
print(today+timedelta(days=1, hours=1, minutes=1, weeks=2))

# calculate the date 1 week ago, formatted as a string
str(datetime.now()+timedelta(weeks=-1))

# How many days until April Fools' Day?
apf = datetime.strptime('2021-04-01', '%Y-%m-%d')
foo = apf - datetime.now()
print(foo)
print(apf)
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if foo.days < 0:
    apf = apf.replace(year=2022)
    print(apf)
# Now calculate the amount of time until April Fool's Day
    print(apf - datetime.now())
