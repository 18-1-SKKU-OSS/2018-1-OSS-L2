def fibonacci_R(num):
    #this function calculates fibonacci using recursion
    if num > 1:
        return fibonacci_R(num-1) + fibonacci_R(num-2)
    else:
        return num


def fibonacci_L(num):
    #this function calculates fibonacci using loop
    a = 1
    b = 1
    for i in range(num-1):
        a = b
        b = a+b
    return a


def fibonacci_M(num):
    #this function calculates fibonacci using memoization
    def fib(n):
        if n > 1:
            return fib(n-1) + fib(n-2)
        else:
            return n
        
    def memoize(function, arg):
        memo = {}
        if arg not in memo:
            memo[arg] = function(arg)
            return memo[arg]
    return memoize(fib, num)

    
class Memoize:
    #this function calculates fibonacci using memoization as decorator
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]
@Memoize
def fibonacci_MM(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
