#11. Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days 
# TODAY use if else n loops
from datetime import datetime
date_of_birth = input("Enter date of birth (dd/mm/yyyy): ")
date_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y")
today = datetime.today()
age = today - date_of_birth
print(f'Age: {age.days // 365} years, {age.days % 365// 30} months, {age.days % 30} days')
  