str = input("Enter the word:")

for i in range(0, len(str)//2, 1):
    if str[i] != str[-1-i]:
        print("Your word is non polindrome")
        quit()
print("Your word IS polindrome!!!")
