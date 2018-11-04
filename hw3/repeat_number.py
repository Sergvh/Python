import random

count = int(input("Enter amount of list elements more then 15:"))

a = [random.randint(1, 10) for i in range(0, count)]

print("generated list:"+str(a)+"\n \n")
flag = 0
for i in range(0, count-1, 1):
    if flag == 0:
        for j in range(i+1, count, 1):
            if a[i] == a[j]:
                print("match found:" + str(a[j]))
                flag = 1
            break
    else:
        break
