import random

names = ["Kai", "Seb", "Beb", "Friday", "Saturday"]
random = random.shuffle(names)

for i in range(1):
    print(names.pop())

print("gets")

for i in range(1):
    print(names.pop())