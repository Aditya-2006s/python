# Input color from the user
color = input("Enter a color (Red, Yellow, Green): ").capitalize()

# Determine the corresponding action based on the color
if color == "Red":
    action = "Stop"
elif color == "Yellow":
    action = "Get Ready"
elif color == "Green":
    action = "Go"
else:
    action = "Invalid color"

# Output the action
print(f"The action is: {action}")
