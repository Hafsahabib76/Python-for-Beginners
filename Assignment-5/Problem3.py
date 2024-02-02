import datetime

# Input the date from the user
userDateInput = input("Enter a date (YYYY-MM-DD): ")

# Convert the user input date into date object
userDate = datetime.datetime.strptime(userDateInput, "%Y-%m-%d")

# Converts and prints it in the "Month Day, Year" format
formatted_date = userDate.strftime("%B %d, %Y")
print("Formatted date:", formatted_date)