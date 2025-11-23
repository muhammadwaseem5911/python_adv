# this is for date
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)
# when monday 0
from datetime import date

d = date(2019, 11, 4)
print(d.weekday())

# when monday is 1
from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())
# time module
import time
print(time.ctime())


