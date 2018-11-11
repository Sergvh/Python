import random

count = int(input("Enter amount of list elements:"))

a = [random.randint(1, 100) for i in range(0, count)]

print("generated list:"+str(a)+"\n \n")


def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list if x > pivot]
        more = [x for x in list[1:] if x <= pivot]
        return qsort(less) + [pivot] + qsort(more)


print(qsort(a))
