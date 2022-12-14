def Fibonacci(n):
    if n < 0:
        print('Incorrect input')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
user_input = input('Enter a number for the fibonacci series: ')
try:
    n_as_int = int(user_input)
except:
    print('You did not enter an integer')

print(Fibonacci(n_as_int))