# Dictionary mapping numbers to months
months = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

# Ask the user for input
number = int(input("Enter a number (1-12): "))

# Check if the number is in the valid range
if 1 <= number <= 12:
    print(f"The month is {months[number]}.")
else:
    print("Error: The number must be in the range of 1 to 12.")
