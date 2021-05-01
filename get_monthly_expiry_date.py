# Author Arun K Selvaraj
# Created to get NSE monthly expiry date.
import datetime, calendar

def get_monthly_expiry_date(year, month):
    # Create a datetime.date for the last day of the given month
    daysInMonth = calendar.monthrange(year, month)[1]   # Returns (month, numberOfDaysInMonth)
    dt = datetime.date(year, month, daysInMonth)

    # Back up to the most recent Thursday
    offset = 4 - dt.isoweekday()
    if offset > 0: offset -= 7                          # Back up one week if necessary
    dt += datetime.timedelta(offset)                    # dt is now date of last Th in month

    # Throw an exception if dt is in the current month and occurred before today
   # now = datetime.date.today()                         # Get current date (local time, not utc)
   # if dt.year == now.year and dt.month == now.month and dt < now:
   #     raise Exception('Oops - missed the last Thursday of this month')

    return dt

for month in range(1, 13): print(get_monthly_expiry_date(2021, month))