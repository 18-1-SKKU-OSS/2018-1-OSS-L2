def fibonacci(num):
    if num > 1:
        return fibonacci(num-1) + fibonacci(num-2)
    else:
        return num

print(fibonacci(10))
