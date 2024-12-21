# Input age and experience from the user
age = int(input("Enter your age: "))
experience = int(input("Enter your experience in years: "))

# Check eligibility based on age and experience
if age > 18 and experience >= 2:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"

# Output the eligibility status
print(f"You are {eligibility} for the job.")
