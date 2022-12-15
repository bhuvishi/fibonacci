def Fibonacci(n):
    if n < 0:
        print('Incorrect input')
    elif n == 0:
        return 0
    else: 
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a+b
            a = b
            b = c
        return c


