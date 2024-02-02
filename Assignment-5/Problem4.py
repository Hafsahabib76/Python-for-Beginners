import datetime

# Input the date from the user
userDateInput = input("Enter any future date (YYYY-MM-DD): ")

# Convert the user input date into a date
userDate = datetime.datetime.strptime(userDateInput, "%Y-%m-%d").date()

# Get the current date
todayDate = datetime.date.today()

# Calculate the number of days remaining
remainingDays = (userDate - todayDate).days

# if remaining days is less than 0 - print date is in the past, else print the remain days
if remainingDays < 0:
    print("The input date is in the past.")
else:
    print(f"Number of days remaining until {userDateInput}: {remainingDays} days")