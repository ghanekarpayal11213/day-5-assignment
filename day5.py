# Function to calculate the factorial of a number
def factorial(num):
    if num == 0:
        return 1
    else:
        fact = 1
        for i in range(1, num+1):
            fact *= i
        return fact

# Main program
number = int(input("Enter a number: "))
if number < 0:
    print("Factorial cannot be calculated for negative numbers")
else:
    result = factorial(number)
    print("The factorial of", number, "is", result)





