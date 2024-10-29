# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."
amount = float(input('Amount: '))
account_type = input('Account type (Standard/Premium): ')   
if account_type == "Standard":  
    if amount > 500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved.")
elif account_type == "Premium":
    if amount > 1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")
else:
    print("Invalid account type.")

# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"




# 4 Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password = input('Enter your password: ')
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")  
    
# 5 Write a Python program that checks if a variable student
# score is greater than 90. If true, check if the attendance is greater than 80
# . If both conditions are true, print "Excellent student", otherwise print "Good score, but    
# attendance needs improvement"

student_score = float(input('Enter your score: '))
attendance = float(input('Enter your attendance: '))
if student_score > 90 and attendance > 80:
    print("Excellent student")
else:
    print("Good score, but attendance needs improvement")  



# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "
# Conditions met", otherwise print "Conditions not met" 

x = float(input('Enter a number: '))
y = float(input('Enter another number: '))
if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")


# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
num3 = float(input('Enter the third number: '))
numbers = [num1, num2, num3]
print(max(numbers))
# 2. Take as input from a user the temperature if the temperature is above 30°C
# print "It is hot outside", otherwise print "It is not hot outside"
temperature = float(input('Enter the temperature: '))
if temperature > 30:
    print("It is hot outside")
else:
    print("It is not hot outside")








