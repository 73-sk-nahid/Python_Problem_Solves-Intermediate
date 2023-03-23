# fibonacci Series Using Recursion

def fibonacci(n):
    if (n <= 1) :
        return n
    else:
        return (n-1) + (n-2)

a = int(input("Enter a positive Number: "))
for i in range(a):
    print(fibonacci(i))