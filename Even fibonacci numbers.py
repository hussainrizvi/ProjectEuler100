
def fib(to=10):    #Generator function
    a = 1
    b = 2
    while a < to:
        yield a    #Usage of yield statement understood
        a,b = b, a+b

evenFib = sum([i for i in fib(4000000) if i % 2 == 0])
print(evenFib)