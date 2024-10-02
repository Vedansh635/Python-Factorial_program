def factorial(n):
    """
    This function calculates the factorial of a given number.
    
    A factorial of a number is the product of all positive integers less than or equal to that number.
    For example, factorial of 5 (5!) = 5*4*3*2*1 = 120
    
    The base case is when n is 0 or 1, where the factorial is defined to be 1.
    """
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 'Factorial is not defined for negative numbers'
    else:
        return n* factorial(n-1)

number = int(input("Enter the number: "))
print(factorial(number)) 
# All code is written by me , except comments .
