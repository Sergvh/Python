import random

count = int(input("Enter amount of list elements:"))

a = [random.randint(1,200) for i in range(0, count)]

for i in range(0,count-1, 1):
    min = i
    for j in range(i+1, count, 1):
        if a[min] > a[j]:
            min = j

    if min != i:
        a[i], a[min] = a[min], a[i]

print("sorted list:"+str(a)+"\n \n")

wanted = int(input("Enter wanted number from list:"))
k = len(a)//2
while k != 1:
    if a[k] == wanted:
        print("wanted found: "+str(a[k]))
        break
    elif a[k] > wanted:
        k //= 2
    else:
        k = (len(a)-k) // 2+ k