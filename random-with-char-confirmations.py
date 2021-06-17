import random
import string

alpha = dict(enumerate(string.ascii_letters))

password = input("Password: ")

maxLength = len(password)

temp = ""

for i in range(maxLength):
    while True:
        tempCharGen = random.choice(alpha)
        print(temp + ", testing: " + tempCharGen)
        if tempCharGen == password[i]:
            break
        else:
            continue

    temp = temp + tempCharGen
    print(temp)

print(temp)
