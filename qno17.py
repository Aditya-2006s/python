# Input height from the user
height = float(input("Enter your height in feet: "))

# Select players based on height
if height >= 6:
    selection = "Selected"
else:
    selection = "Not Selected"

# Output the result
print(f"You are {selection}.")
