
email = "hamza@example.com"
password = "12345"


while True:

    user_email = input("enter your email: ")
    user_password = input("enter your password: ")

    if user_email == email:
        print("valid email.")
    else:
        print("Invalid email.") 

    if user_password == password:
        print("valid password.")
    else:
        print("Invalid password.")
    
    if user_email == email and user_password == password:
        print("Login successful!")
        break
    else:
        print("user not found.")

