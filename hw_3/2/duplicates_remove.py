import random

count = int(input("Enter amount of list elements:"))

a = [random.randint(1, 10) for i in range(0, count)]

print("generated list:" + str(a) + "\n \n")

for i in range(0, count, 1):
    j = i + 1
    while j <= len(a)-1:
        if a[i] == a[j]:
            a.pop(j)
        else:
            j += 1

print("Duplicates are removed: "+str(a))
