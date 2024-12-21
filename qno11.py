# Input age from the user
age = int(input("Enter the age: "))

# Categorize the age
if age < 13:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teenager"
else:
    category = "Adult"

# Output the category
print(f"The category is: {category}")
