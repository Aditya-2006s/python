# Input age from the user
age = int(input("Enter your age: "))

# Check if the person is eligible to watch the movie
if age >= 18:
    eligibility = "Allowed"
else:
    eligibility = "Not Allowed"

# Output the result
print(f"You are {eligibility} to watch the movie.")
