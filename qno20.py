month = int(input("Enter the month number (1–12): "))

if month == 12 or month == 1 or month == 2:
    season = "Winter"
elif month == 3 or month == 4 or month == 5:
    season = "Spring"
elif month == 6 or month == 7 or month == 8:
    season = "Summer"
elif month == 9 or month == 10 or month == 11:
    season = "Autumn"
else:
    season = "Invalid month number"

print(f"The season is: {season}")
