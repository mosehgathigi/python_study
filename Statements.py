# marks =
# 90=>100 A
# 80=>90 B
# 70=>80 C
# 60=>70 D
# 50=>60 E
# 0=>50 F

# if elif else
marks = int(input('Enter marks: '))
if marks >= 90:
    print('Grade: A')

# 80=>90 B
elif marks >= 80 and marks <= 90:
    print('Grade: B')
    # 70=>80 C
elif marks >= 70 and marks <= 80:
    print('Grade: C')
# 60=>70 D
elif marks >= 60 and marks <= 70:
    print('Grade: D')
    # 50=>60 E
elif marks >= 50 and marks <= 60:
    print('Grade: E')   
    # else 0=>50 F  
else:
    print('Fail')
         

# 60and above print you are an elder
# 18 and above adult
# else minor

age = int(input('age: '))
if age >= 60:
    print('You are an elder')
elif age >= 18:
    print('You are an adult')
else:
    print('You are a minor')    


# if age  is
age1=int(input("enter your age: "))
if age>=18:
  licenses=input("do you have a license yes/no: ").lower().strip()
  if licenses=="yes":
    print("eligible to drive")
  else:
     print("you are not eligible to drive")
else:
  print("you are to young to drive")


# Write a program that:
# =>Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above $50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low.
creditScore = int(input('Credit Score: '))
income = int(input('Annual Income: '))
if creditScore > 700:
    if income > 50000:
      print('Loan approved.')
    else:
      print('Income requirement not met.')
else:
   print('Credit score too low.')



    
    

