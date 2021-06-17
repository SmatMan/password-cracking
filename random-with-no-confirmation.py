import random
import string

alpha = dict(enumerate(string.ascii_lowercase))

password = input("Password: ").lower()

maxLength = len(password)


while True:
    temp = ""

    for i in range(maxLength):
        tempCharGen = random.choice(alpha)
        temp = temp + tempCharGen
    print("testing: " + temp)
    if temp == password:
        break
    else:
        continue

print(temp)
