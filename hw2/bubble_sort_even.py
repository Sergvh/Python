import random

count = int(input("Enter amount of list elements:"))

a =[random.randint(1, 200) for i in range(0, count)]

print("generated list:"+str(a)+"\n \n")

for i in range(0, count, 1):
    #swapped = 0

    for j in range(0, count-1, 1):
        # if (((a[j] > a[j+1]) and (a[j+1] % 2 == 0))) or (((a[j] > a[j+1]) and (a[j+1] % 2 != 0) and (a[j] % 2 != 0))) \
        #         or (((a[j] > a[j+1]) and (a[j+1] % 2 == 0) and (a[j] % 2 == 0))):
        if a[j] > a[j+1]:
            if (a[j] % 2 == 0 and a[j+1] % 2 ==0) or (a[j] % 2 != 0 and a[j+1] % 2 !=0):
                a[j], a[j+1] = a[j+1], a[j]
        elif a[j] % 2 != 0 and a[j+1] %2 == 0:
            a[j], a[j + 1] = a[j + 1], a[j]
        # if (a[j] % 2 != 0) and (a[j] < a[j + 1])):
        #     a[j], a[j + 1] = a[j + 1], a[j]
            #swapped = 1
    #if swapped == 0:
        #break

print("sorted list:"+str(a))
