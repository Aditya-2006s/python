# Input character from the user
char = input("Enter a character: ")

# Check if the character is uppercase, lowercase, or a digit
if char.isupper():
    result = "Uppercase"
elif char.islower():
    result = "Lowercase"
elif char.isdigit():
    result = "Digit"
else:
    result = "Neither uppercase, lowercase, nor digit"

# Output the result
print(f"The character is: {result}")
