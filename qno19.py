# Input username and password from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the credentials are correct
if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")
