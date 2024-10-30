# # 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# # If start_date comes before end_date, print "Valid period",
# # If start_date is after end_date, print "Invalid period".
# # If both dates are the same, print "One-day period".
# start_date = '2024-01-01'
# end_date = '2024-12-31'
# if start_date < end_date:
#     print("Valid period")
# elif start_date > end_date:
#     print("Invalid period")
# else:
#     print("One-day period")

# # 2.Given two strings str1 and str2, write a conditional statement that checks:
# # If str1 is longer than str2, print "str1 is longer".
# # If str2 is longer than str1, print "str2 is longer".
# # If both have equal length, print "Both are of equal length".
# str1 = 'lorem t'
# str2 = 'ipsum dolor'
# if len(str1) > len(str2):
#     print("str1 is longer")
# elif len(str1) < len(str2):
#     print("str2 is longer")
# else:
#     print("Both are of equal length")



# # 3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# # Prints "Access Granted" if user_id is in valid_ids.
# # Prints "Access Denied" if user_id is not in valid_ids.
# valid_ids = [101, 102, 103]
# user_id = 105
# if user_id in valid_ids:
#     print("Access Granted")
# else:  
#     print("Access Denied")

# # 4.Given a variable value that could be of any type, write a conditional statement that:
# # Prints "String Detected" if value is a string.
# # Prints "Integer Detected" if value is an integer.
# # Prints "Unknown Type" for any other type.
# value = 123
# if isinstance(value, str):
#     print("String Detected")
# elif isinstance(value, int):
#     print("Integer Detected")
# else:
#     print("Unknown Type")


# # 5.Given x = 7 and y = 14, write nested conditional statements that print:
# # "x and y are both even" if both x and y are even numbers.
# # "Only y is even" if only y is even.
# # "Neither x nor y are even" if both are odd.
# x = 7
# y = 14
# if x % 2 == 0 and y % 2 == 0:
#     print("x and y are both even")
# elif y % 2 == 0:
#     print("Only y is even")
# else:
#     print("Neither x nor y are even")

#     Write a program that displays a numbers 1 to 50 inside a list.
list = []
for i  in range(1, 51): 
    list.append(i)
    print(list)


# From 1 above display the ones divisible by 7 or 5 inside a list.
lst = []
for i  in range(1, 51):
    if i % 7 == 0 or i % 5 == 0:
        lst.append(i)
print(list)


# Find sum and average of values in the range between 10 to 40.



sum =  0
count = 0
for i in range(10, 41):
    sum += i
    count += 1
    average = sum / count
print(sum)
print(average)
    

# Put in a list the first 10 odd numbers between 10 to 50. 
odd_numbers = []

for i in range(10, 51):
        if i % 2 != 0:
            odd_numbers.append(i)
            ls=  odd_numbers[0:10]
print(ls) 
   

# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")  
     
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even_count = 0
for i in range(1, 51):
    if i % 2 == 0:
        even_count += 1
print(even_count)
print(f"Total even numbers: {even_count}")


# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above. 

   
# ls1 = [("Jay", 20), ("Mo", 30), ("Mya",32)]
# total = sum(age for name, age in ls1)
# print(total)


