# Write a program that takes input of 2 values and adds them.
#  The program should only accept numbers and floats only or otherwise
#  display an error “invalid character entered” and take the user to re-enter the inputs .
value1 =  input("Enter the first value: ")
value2 =  input("Enter the second value: ")
while True:
    try:
        value1 = float(value1)
        value2 = float(value2)
        sum = value1 + value2
        print("The sum of the two values is: ", sum)
        break
    except ValueError:
        print("Invalid character entered. Please enter a number or float.")
