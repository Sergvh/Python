import random

count = int(input("Enter amount of list elements:"))

a = [random.randint(1,200) for i in range(0, count)]

print("generated list:"+str(a)+"\n \n")

for i in range(0,count-1, 1):
    min = i
    for j in range(i+1, count, 1):
        if a[min] > a[j]:
            min = j

    if min != i:
        a[i], a[min] = a[min], a[i]

print("sorted list:"+str(a))