import random

count = int(input("Enter amount of list elements:"))

a = [random.randint(1,200) for i in range(0, count)]

print("generated list:"+str(a)+"\n \n")

for i in range(0,count-1, 1):
    max = i
    for j in range(i+1, count, 1):
        if a[max] < a[j]:
            max = j

    if min != i:
        a[i], a[max] = a[max], a[i]

print("sorted list:"+str(a))