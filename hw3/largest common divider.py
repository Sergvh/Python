a = int(input("enter a number please:"))
b = int(input("enter b number please:"))


while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print("\n Largest common divider is:"+str(a + b))
