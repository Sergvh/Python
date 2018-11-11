num = int(input("Enter number please:"))
a = []
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


while num > 0:
    a.append(fib(num))
    num -= 1

print(a[::-1])
