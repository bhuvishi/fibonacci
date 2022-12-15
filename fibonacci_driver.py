import fibonacci_dynamic
import fibonacci_memoization
import fibonacci_recursion
import time


def get_fib_and_time(n, fib_fn):
    duration = 0
    for i in range(1000):
        start_time = time.time()
        fib_n = fib_fn(n_as_int)
        end_time = time.time()
        duration += end_time - start_time
    return fib_n, duration / 1000


success = False
while not success:
    user_input = input('Enter a number for the fibonacci series: ')
    try:
        n_as_int = int(user_input)
        fib_n, duration_dynamic = get_fib_and_time(n_as_int, fibonacci_dynamic.Fibonacci)
        fib_n, duration_memoization = get_fib_and_time(n_as_int, lambda x: fibonacci_memoization.Fibonacci(x, {}))
        fib_n, duration_recursion = get_fib_and_time(n_as_int, fibonacci_recursion.Fibonacci)
        print(duration_memoization/ duration_recursion, duration_dynamic / duration_recursion)
        success = True
    except ValueError:
        print('You did not enter an integer')