# generate an infinite series of fibonacci by using generator function

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# print first 100 fibonacci numbers
# Loop through the Fibonacci sequence/sequence
# Stop when the number is greater than 100
for i in fib():
    print(i)
    if i > 100: # stop the loop when the fibonnacci number is greater than 100
        break