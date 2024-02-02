import datetime

# get the current date
currentDate = datetime.datetime.now()

# input the user birthday date
userBirthDateInput = input ('Plz enter your date of birth (mm/dd/yyyy) ')
userBirthDate = datetime.datetime.strptime(userBirthDateInput,'%m/%d/%Y')

# calculate the user Age
userAge = currentDate - userBirthDate

# calculate for the years
years = ((userAge.total_seconds())/(365.242*24*3600))
yearsInt = int(years)

# calculate for the months
months = (years-yearsInt)*12
monthsInt = int(months)

# calculate for the days
days = (months-monthsInt)*(365.242/12)
daysInt = int(days)

# print the age in years, months and days
print(f'Your Age {yearsInt} years, {monthsInt}  months, {daysInt}  days old.')