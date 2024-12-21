menu_option = input("Enter a menu option (Pizza, Burger, Pasta): ").capitalize()

if menu_option == "Pizza":
    price = "$10"
elif menu_option == "Burger":
    price = "$7"
elif menu_option == "Pasta":
    price = "$8"
else:
    price = "Invalid option"

print(f"The price of {menu_option} is: {price}")
