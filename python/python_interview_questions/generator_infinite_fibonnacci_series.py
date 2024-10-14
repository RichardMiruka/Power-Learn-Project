#Generate an infinite fibonacci series by using Generator

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

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