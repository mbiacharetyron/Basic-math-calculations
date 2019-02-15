# Program to comput simple math operations

#Function to add two numbers
def add(num1, num2):
    return num1 + num2

#Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

#Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

#Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return pow(num1, num2)

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
1 for addition
2 for subtraction
3 for multiplication
4 for division
5 for power
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '1':
        print(number_1, '+', number_2, '=',
          add(number_1, number_2))

    elif operation == '2':
        print(number_1, '-', number_2, '=',
          subtract(number_1, number_2))

    elif operation == '3':
        print(number_1, '*', number_2, '=',
          multiply(number_1, number_2))

    elif operation == '4':
        print(number_1, '/', number_2, '=',
          divide(number_1, number_2))
        
    elif operation == '5':
        print(number_1, '^', number_2, '=',
          power(number_1, number_2))
    
    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input("Do you want to calculate again? \n Please type Y for YES or N for NO.\n")

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()
