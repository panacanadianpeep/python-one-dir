# import modedules

import time
import random

# variables

name = input("What is your name")
stregnth = 1
intellgence = 1
speech = 1
job = "1"
meele = 1
shooting = 1
food = 0
water = 0
building = 1
fixing=1
print("What was your job before the acropolis 1. Mechanic(fixing up 1) 2. Construction worker(building up 1)")
job_question = input("3. Guard(shooting+1) 4. Engineer(Intelligence up 1) and 5. politician(speech up 1)")
valid1=False
while valid1 == False:
    if job == "1" or "Mechanic":
        valid1 = True
        job = "Mechanic"
        fixing = fixing+1
        valid1=True
    elif job == "2" or "Constrution worker":
        valid1 = True
        job = "Construction worker"
        building=building+1
        valid1 = True
    elif job == "3" or "Guard":
        job = "Guard"
        shooting=shooting+1
        meele=meele+1
        valid1 = True
    elif job == "4" or "Engineer":
        valid1 = True
        intellgence=intellgence+1
        job="Engineer"
    elif job == "5" or "Politician":
        valid1 = True
        job = "Mechanic"
        speech = speech+1
    else:
        job_input = input("Enter valid job")

print("Your name is", name, "and your job is", job)
# episode 1

# day 1
print("You open your eyes. You see two bodys, which look dead. You recognize the person. You shout for Sally.")
time.sleep(1)
print("It doesn't work. You then see another body, which you call out for your wife Samantha.")
time.sleep(4)
print("It was a warm sunny day. On a highway, a minivan appears with Sally and one other man.")
time.sleep(2)
print("The man name was carl. ")

