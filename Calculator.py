#Simple Calculator with a bunch of if and else 
print("This calculator can only do math for two numbers")
#Input your first number
print("Please enter First Number\n")
FirstNumber = float(input())
#Input your second number
print("Please enter Second Number\n")
SecondNumber = float(input())

#Input the number for your operation 
print("Which operation do you want to do ")
print("Press 1 for addition ")
print("Press 2 for subtraction ")
print("Press 3 for multiplication ")
print("Press 4 for division ")

Operation = int(input())
#Method to run which one you want 
def Solveit(Operation):
    if Operation == 1 :
     print ("The two numbers added will give you; " ,FirstNumber + SecondNumber)#Answers

    elif Operation == 2:
     print ("The first number minus the second number will give you ;",FirstNumber - SecondNumber)#Answers

    elif Operation == 3:
     print ("The two numbers multiplied will give you; " ,FirstNumber * SecondNumber)#Answers

    elif Operation == 4:
     print ("The first number divided by the second number will give you ; " ,FirstNumber / SecondNumber)#Answers

    else :
      print ("Choose a number between 1 , 2 , 3 and 4")
#Call method
Solveit(Operation)

