#very basic calculator

'''number=float(input("Enter the first Number for Calculation "))
number_2=float(input("Enter the second Number for Calculation "))

decide=int(input("1--Addition\n2--Subtraction\n3--Multiplication\n4--Divission\n5--Floor division"))
match decide:
    case 1:
        print("Addition of two numbers is:",number+number_2)
        
    case 2:
        print("Subtraction of two numbers is:",number-number_2)
       
    case 3:
        print("Multiplication of two numbers is:",number*number_2)
        
    case 4:
        if number_2==0 or number==0:
            print("Can't divide by zero")
        print("division of two numbers is:",number/number_2)
      
    case 5:
        print("floor division of two numbers is:",number//number_2)
      
    case _:
        print("INVALID INPUT")

        
#different approach

number=int(input("Enter the first Number for Calculation "))
number_2=int(input("Enter the second Number for Calculation "))
print("Addition of two numbers is:",number+number_2)
print("Subtraction of two numbers is:",number-number_2)
print("Multiplication of two numbers is:",number*number_2)
print("division of two numbers is:",number/number_2)
print("floor division of two numbers is:",number//number_2)'''


#direct method
n = int(input("How many variables are included? "))
variables = {}

for i in range(n):
    var_name = input(f"Enter the name of variable {i + 1}: ")
    var_value = int(input(f"Enter the value of {var_name}: "))
    variables[var_name] = var_value

expression = input("Enter the expression: ")
result = eval(expression, variables)
print(f"Result: {result}")


