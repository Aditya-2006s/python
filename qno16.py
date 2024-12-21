# Input menu option from the user
menu_option = input("Enter a menu option (Pizza, Burger, Pasta): ").capitalize()

# Determine the price based on the menu option
if menu_option == "Pizza":
    price = "$10"
elif menu_option == "Burger":
    price = "$7"
elif menu_option == "Pasta":
    price = "$8"
else:
    price = "Invalid option"

# Output the price
print(f"The price of {menu_option} is: {price}")
