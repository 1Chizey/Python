def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b 
def divide(a, b):
    return a / b 

#create a dictionary operation that assigns the functions
operation = {"+": add, "-": subtract, "*": multiply, "/": divide}

#create a function 'calculator' that prompt the user to input the first number
def calculator():
    should_continue = True
    first_number = float(input("Enter the first number: "))
    #use a for loop to print the available operation symbols.
    print("these are the available operations")
    for operation_symbol in operation.keys():
        print(operation_symbol)

    while should_continue:
    #inside the while loop prompt the user to select an operation symbol.
        operation_symbol = input("pick an operation: ")
    #if the operation symbol is not in the operations dictionary, print an error message and continue to
    #the next iteration of the loop.
        if operation_symbol not in operation:
            print("Invalid operation")
            continue
        else:
            #prompt the user to input the second number.
            second_number = float(input("Enter the second number: "))

            #if the operation symbol is the operation dictionary, assign the corresponfing function to 
            #the variable 'calculation_function'
            calculation_function = operation[operation_symbol]

            #perform the calculation by calling the 'calculation fuction on the two input numbers and 
            #store the result in a variable 'answer'
            answer = calculation_function(first_number, second_number)
            #print the equation and the result of the calculation.
            print(f"{first_number} {operation_symbol} {second_number} = {answer}")


            #Ask the user if they would like to continue using the result as the first number for further calculations
            choice = input("Do you want to contine with the result as the first number? (yes/no): ")

            #if the user choose to start a new calculation, set the 'should_continue' variable to false and call
            #the 'calculator' function to start a new calculation.
            if choice == "yes":
                first_number = answer
            elif choice == "no":
                should_continue = False
                calculator()
            elif choice == "stop":
                print("Thank you for using the calculator")
                break
            else:
                print("invalid choice, The choices are (yes or no and stop")
#call the calculator function to start the calculator program.
calculator()