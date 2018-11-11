count = int(input("Enter amount of list elements:"))

a = []

for i in range(1, count, 1):
    if (i % 2 == 0 and i % 3 == 0) or (i % 2 != 0 and i % 5 == 0):
        a.append(i)

print("generated list:" + str(a))
