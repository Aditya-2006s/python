# Input temperature from the user
temperature = float(input("Enter the temperature in °C: "))

# Give advice based on the temperature
if temperature > 30:
    advice = "It's hot, stay hydrated!"
elif 15 <= temperature <= 30:
    advice = "Enjoy the weather!"
else:
    advice = "It's cold, wear warm clothes!"

# Output the advice
print(advice)
