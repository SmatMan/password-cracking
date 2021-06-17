import random
import string
import itertools
import time
import json

alpha = dict(enumerate(string.ascii_lowercase))

password = input("Password: ").lower()

maxLength = len(password)

passwords = {}

starttime = time.time()

for iterator in itertools.count():
    temp = ""

    for i in range(maxLength):
        tempCharGen = random.choice(alpha)
        temp = temp + tempCharGen
    passwords[temp] = iterator
    print("testing: " + temp)
    if temp == password:
        break
    else:
        continue

print(temp)
print(time.time() - starttime)

with open('passwords.txt', 'w') as f:
    f.write(str(json.dumps(passwords, indent=4)))
    f.write(
        f"\nThis program took {time.time() - starttime} seconds to complete.")
