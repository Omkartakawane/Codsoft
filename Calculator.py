#The following Functions are for peforming basic calculation!!
def add(number_1,nnumber_2):
    return number_1 + nnumber_2
def subtract(number_1,number_2):
    return number_1 - number_2
def divide(number_1,number_2):
    return number_1 / number_2
def multiply(number_1,number_2):
    return number_1 * number_2
while (1):
    print("***Hey,Welcome to a simple calculator***")
    print("Please select an operation to perform:\n")
    print("1.Addition\n""2.Subtraction\n""3.Division\n""4.Multiply\n")
    operation=int(input("Enter the operation number which you want to perform:\n"))
    number_1=int(input("Enter the first number:\n"))
    number_2=int(input("Enter the second number:\n"))

    if operation == 1:
        print(number_1,"+",number_2,"=",add(number_1,number_2))
    elif operation == 2:
        print(number_1,"-",number_2,"=",subtract(number_1,number_2))
    elif operation == 3:
        print(number_1,"/",number_2,"=",divide(number_1,number_2))
    elif operation == 4:
        print(number_1,"*",number_2,"=",multiply(number_1,number_2))
    else:
        print("Invalid Input Please Enter A Valid Choice!!!")