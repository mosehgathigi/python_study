# Write a program that takes the email and password as input from a user and checks
#  if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print
#   “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 
# tries after which it notifies you that you have been blocked.
trials = 0
while trials < 3:
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == "admin@mail.com" and password == "Admin@123":
        print("Login is Successful")
        break
    else:
        trials += 1
        print("Invalid username or password")
        if trials == 3:
            print("You have been blocked")
            break




