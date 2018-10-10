import random

count = int(input("Enter amount of list elements:"))

a = [random.randint(1,200) for i in range(0, count)]

print("generated list:"+str(a)+"\n \n")

for i in range(0,count, 1):
    for j in range(0,count-1, 1):
        if (a[j]<a[j+1]):
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp

print("sorted list:"+str(a))
