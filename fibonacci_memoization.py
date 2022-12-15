def Fibonacci(n,memo):
    if n < 0:
        print('Incorrect input')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        val = Fibonacci(n-1, memo) + Fibonacci(n-2, memo)
        memo[n] = val
        return val
