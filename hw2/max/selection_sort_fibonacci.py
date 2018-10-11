import random

count = int(input("Enter amount of list elements:"))

fib_1 = 1
fib_2 = 1
lst = []

for _ in range(count * 5):
    lst.append(fib_1)
    fib_1, fib_2 = fib_2, fib_1 + fib_2

print("Fibonacci list generate: "+str(lst))

a = [random.choice(lst) for i in range(0, count)]

print("generated list:" + str(a) + "\n \n")

for i in range(0, count - 1, 1):
    min = i
    for j in range(i + 1, count, 1):
        if a[min] > a[j]:
            min = j

    if min != i:
        a[i], a[min] = a[min], a[i]

print("sorted list:" + str(a))
