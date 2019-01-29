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


print("Please select an operation you would like to perorm: \n" \
       "(1.) for addition\n" \
       "(2.) for subtraction\n" \
       "(3.) for multiplication\n" \
       "(4.) for division\n"
       "(5.) for power")

#Take input from the user

select = input("Select operations from 1 through 5:\n ")

number_1 = int(input("Enter first number:  \n"))
number_2 = int(input("Enter second number:  \n"))

if select == '1':
    print(number_1, '+', number_2, '=',
          add(number_1, number_2))
    
elif select == '2':
    print(number_1, '-', number_2, '=',
          subtract(number_1, number_2))

elif select == '3':
    print(number_1, '*', number_2, '=',
          multiply(number_1, number_2))

elif select == '4':
    print(number_1, '/', number_2, '=',
          divide(number_1, number_2))
    
elif select == '5':
    print(number_1, '^', number_2, '=',
          power(number_1, number_2))

else:
        print("Invalid Input")
    

def again():
    calc_again = input("Do you want to Calculate again? \n Please type Y for YES or N for NO")

    if calc_again.upper() == 'Y':
        select()
    elif calc_again.upper() == 'N':
        print("See you Later.")
    else:
        again()
