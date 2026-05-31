#conditional statement
age = 25
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

age = 20
if age >= 18:
    print("you can vote.")
else:
    print("you cannot vote.")



light = "red"
if light == "green":
    print("Go")
elif light == "yellow":
    print("Prepare to stop.")
else:
    print("Stop.")



#Grade students based on their marks
marks = int(input("Enter your marks: "))
if( marks >= 90):
    print("Grade: A")   
elif (marks >= 80 and marks < 90):
    print("Grade: B")
elif (marks >= 70 and marks < 80):
    print("Grade: C")
elif (marks >= 60 and marks < 70):
    print("Grade: D")
else:
    print("You failed the exam.")


#Nesting of if statements
age = int(input("Enter your age: "))
if( age >= 18):
    print("You are an adult.")
    if (age >= 21):
        print("You can drink alcohol.")
    else:
        print("You cannot drink alcohol.")


#nesting of if statements
age = int(input("Enter your age: "))
if age >=18:
    if age >=80:
        print("you can not drive.")
    else:
        print("you can drive.")
else:
    print("you can not drive.")



#QUESTION_1: write a program to check if a number enetered by the user is even or odd
number = int(input("Enter a number: ")) 
remainder = number % 2
if remainder == 0:
    print("The number is even.")
else:
    print("The number is odd.")

