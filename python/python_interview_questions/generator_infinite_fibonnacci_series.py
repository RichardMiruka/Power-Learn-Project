#Generate an infinite fibonacci series by using Generator

def fibonacci():              # The fibonacci function is a generator, 
    a, b = 0, 1
    while True:               # The while True loop ensures the series continues indefinitely
        yield a               # using the yield statement to return the next Fibonacci number each time next() is called
        a, b = b, a + b       # The a, b = b, a + b updates the values for the next Fibonacci number in each iteration.

f1 = fibonacci()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

# Example usage: Print the first 10 Fibonacci numbers
# fib_gen = fibonacci()
# for _ in range(10):
    #print(next(fib_gen))