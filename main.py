import time


def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."

    if n == 1:
        return 0

    if n == 2:
        return 1

    first = 0
    second = 1

    for _ in range(2, n):
        temp = first
        first = second
        second = temp + second

    return second


start_time = time.time()
result = fibonacci(10)
end_time = time.time()

execution_time = end_time - start_time

print(f"The 10th Fibonacci number is: {result}")
print(f"Execution time: {execution_time} seconds")
