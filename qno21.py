# Input salary and credit score from the user
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))

# Check car loan eligibility
if salary >= 50000 and credit_score >= 700:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"

# Output the eligibility status
print(f"You are {eligibility} for the car loan.")
