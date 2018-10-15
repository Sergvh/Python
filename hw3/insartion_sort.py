import random

count = int(input("Enter amount of list elements:"))

a = [random.randint(1, 100) for i in range(0, count)]

print("generated list:" + str(a) + "\n \n")

for i in range(1, count, 1):
    tmp = a[i]
    j = i - 1
    while j >= 0:
        if tmp < a[j]:
            a[j + 1] = a[j]
            a[j] = tmp
            j -= 1
        else:
            break

print("sorted list: " + str(a))
