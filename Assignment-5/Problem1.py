import datetime

# Take Year, Month, and Day input from the user
year = int(input('Enter a year (YYYY): '))
month = int(input('Enter a month (MM): '))
day = int(input('Enter a day (DD): '))

# Use of date function to get the date in the actual format of YYYY-MM-DD
userDateInput = datetime.date(year, month, day)

# Calculate the day of the week for the given date.
dayOfWeek = userDateInput.strftime("%A")
print("The day of the week for", userDateInput, "is:", dayOfWeek)

# Calculate the date of the next day
nextDay = userDateInput + datetime.timedelta(days=1)
print("Next day date:", nextDay)

# Calculate the date of the previous day
previousDay = userDateInput - datetime.timedelta(days=1)
print("Previous day date:", previousDay)