color = input("Enter a color (Red, Yellow, Green): ").capitalize()
if color == "Red":
    action = "Stop"
elif color == "Yellow":
    action = "Get Ready"
elif color == "Green":
    action = "Go"
else:
    action = "Invalid color"

print(f"The action is: {action}")
