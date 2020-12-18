usernameInput = input("username : ")
passwordInput = input("password : ")
while usernameInput != "admin" or passwordInput != "1234":
    print("Wrong username or password ,Please login again")
    usernameInput = input("username : ")
    passwordInput = input("password : ")
print("Good Job! You're in!")