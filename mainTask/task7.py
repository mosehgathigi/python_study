
#7.  Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
marks = int(input("Enter your marks: "))
if marks > 79:
    print("Grade: A")
elif marks >= 60 and marks <= 79:
    print("Grade: B")
elif marks >= 50 and marks <= 59:
    print("Grade: C")
elif marks >= 40 and marks <= 49:
    print("Grade: D")
else:
    print("Grade: E")
