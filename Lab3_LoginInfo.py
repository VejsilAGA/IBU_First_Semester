registeremail = str(input("Register email: "))
registerpassword = str(input("Register password: "))

email = str(input("Enter your login email adress: "))

if email == registeremail:
    password = str(input("Enter you password: "))
    if password == registerpassword:
        print("You have sucesfully logged in.")
    else:
        print("Incorrect password.")
else:
    print("Incorrect email.")