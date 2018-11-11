a = [1, 4, 7, 10, 11]


def sorted(list, i):
    if i != 0:
        if list[i] < list[i-1]:
            print("List is not sorted.")
            exit(0)
        else:
            return sorted(list, i-1)


a = sorted(a, len(a)-1)
print("List is sorted!!!")