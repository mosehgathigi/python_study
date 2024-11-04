
# 6. Write a program that lets the user input a password. Give them only 4 attempts
# to check the passwords entered against “admin@123”. If the password is correct
# access is granted. After you show them a message , the account is blocked.
# for loop
attempts = 0
while attempts < 4:
    password = input("Enter your password: ")
    if password == "admin@123":
        print("Access granted")
        break
    else:
        attempts += 1
        print("Incorrect password. Attempts remaining: ", 4 - attempts)
else:
    print("Account blocked")




correct_password = "admin@123"
max_attempts = 4

for attempt in range(max_attempts):
    user_input = input("Enter your password: ")
    if user_input == correct_password:
        print("Access granted.")
        break  
    else:
        max_attempts-=1
        print(f"Incorrect password. Please try again {max_attempts} times.")
else:
    print("Too many incorrect attempts. Your account is blocked.")
