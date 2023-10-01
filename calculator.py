def addition(a,b):
    print("Addition  : ",a+b)

def subtraction(a,b):
    print("Subtraction  : ",a-b)

def multiplication(a,b):
    print("Multiplication  : ",a*b)

def division(a,b):
    if(b==0):
        print("INFINITY")
    else:
        print("Division : ",a/b)

def remainder(a,b):
    if(b==0):
        print("INFINITY")
    else:
        print("Remainder : ",a%b)

def power(a,b):
    print("Power : ",a**b)

while(True):
    choice = int(input("Please make your selection : \n1:ADD\n2:SUBTRACT\n3:MULTIPLY\n4:DIVIDE\n5:REMAINDER\n6:POWER\n**Press 0 to EXIT**\n"))
    if(choice==0):
        print("Successfully Exited")
        break
    first_number=int(input("Enter first number"))
    second_number=int(input("Enter second number"))
    if(choice==1):
        addition(first_number,second_number)
    elif(choice==2):
        subtraction(first_number,second_number)
    elif(choice==3):
        multiplication(first_number,second_number)
    elif(choice==4):
        division(first_number,second_number)
    elif(choice==5):
        remainder(first_number,second_number)
    elif(choice==6):
        power(first_number,second_number)
    else:
        print("Make a valid choice")
  
