n = int(input("Enter number :"))
def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Enter a number greater than 0")
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        print(a)
        print(b)
        for n in range(1,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(n)
