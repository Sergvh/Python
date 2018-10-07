num = int(input("Enter number please:"))
fib_1=1
fib_2=1

for _ in range(num):
    print(str(fib_1))
    fib_1, fib_2 =fib_2, fib_1+fib_2