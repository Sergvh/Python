import random

count = int(input("Enter amount of list elements:"))

a = [random.randint(1, 100) for i in range(0, count)]

print("generated list:"+str(a)+"\n \n")


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] >= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


def mergesort(list):
    if len(list) < 2:
        return list
    middle = int(len(list) / 2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)


a = mergesort(a)
print(a)
