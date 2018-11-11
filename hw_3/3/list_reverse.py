import random

count = int(input("Enter amount of list elements:"))

a = [random.randint(1, 100) for i in range(0, count)]

print("generated list:"+str(a)+"\n \n")


def reverse(list, i):
    if i == len(list) // 2:
        return list
    a[i], a[count-1-i] = a[count-1-i], a[i]
    i += 1
    return reverse(list, i)


a = reverse(a, 0)

print(a)
