import random

countN = int(input("Enter amount of N list elements:"))
countM = int(input("Enter amount of M list elements:"))

n = [random.randint(1, 10) for i in range(0, countN)]
m = [random.randint(1, 10) for i in range(0, countM)]
a = []
print("generated lists:" )
print(n)
print(m)

if len(n) <= len(m):
    for i in range(0, len(n), 1):
        if a.count(n[i]) > 0:
            continue
        elif m.count(n[i]) > 0:
            a.append(n[i])
else:
    for i in range(0, len(m), 1):
        if a.count(m[i]) > 0:
            continue
        elif n.count(m[i]) > 0:
            a.append(m[i])

print("Duplicated elements:"+str(a))
