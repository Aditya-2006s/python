char = input("Enter a character: ")

if char.isupper():
    result = "Uppercase"
elif char.islower():
    result = "Lowercase"
elif char.isdigit():
    result = "Digit"
else:
    result = "Neither uppercase, lowercase, nor digit"

print(f"The character is: {result}")
