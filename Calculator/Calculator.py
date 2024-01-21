if __name__ == "__main__":

    #Prints a welcome message
    print("Welcome to the TAMID Calculator \n")

    #Runs the application untils user inputs n
    while True:

        #user inputs whether they want to calculate something
        userInput = input("Would you like to calculate something (y/n): ")

        #Asks user for two numbers and an operation and calculates the results
        if userInput == "y":
            firstNumberInput = input("\nPlease enter the first number: ")
            secondNumberInput = input("Please enter the second number: ")
            functionInput = input("Please enter your function:")
            mathResult = 0
            #Checks if input is valid and the second number is not zero in divison
            try:
                if secondNumberInput != "0":
                    #Computes the numbers with operation and prints out the result
                    mathResult = eval((firstNumberInput) + (functionInput) + (secondNumberInput))
                    print(f"\nYour result was: {mathResult}! \n")
                else:
                    raise ZeroDivisionError
            except ZeroDivisionError:
                print("\nYou cannot divide by 0!\n")
                continue
            except NameError:
                print("\nInvalid Input. Please make sure both inputs are numbers and the function is valid.\n")
                continue
            
        #exits the program
        elif userInput == "n":
            break