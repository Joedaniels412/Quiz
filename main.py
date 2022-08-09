import time
print("Joe's super duper mega quiz\n")

quest1 = ["2060", "2080ti", "3050", "1080ti", "3080"]
quest2 = ["Antonov 225", "Airbus A380", "Boeing 747", "Airbus A350", "Boeing 777"]
quest3 = ["Python", "Java", "C", "C++", "C#"]
quest4 = ["Steve Jobs", "Jeff Bezos", "Warren Buffett", "Bill Gates", "Mark Zuckerberg"]
quest5 = ["Manchester", "London", "Birmingham", "Leeds", "Liverpool"]

total = "Score! = "
score = 0

print("A - " + (quest1[0]))
print("B - " + (quest1[1]))
print("C - " + (quest1[2]))
print("D - " + (quest1[3]))
print("E - " + (quest1[4]))
print("")
question1 = input("Which one of these graphics cards is the most powerful?\n")

while True:
    if question1 == "E":
        print("Correct!\n")
        score = score + 1
    elif question1 == "e":
        print("Correct!\n")
        score = score + 1
    elif question1 == "3080":
        print("Correct!\n")
        score = score + 1
    else:
        print("Incorrect\n")
    break

print("A - " + (quest2[0]))
print("B - " + (quest2[1]))
print("C - " + (quest2[2]))
print("D - " + (quest2[3]))
print("E - " + (quest2[4]))
print("")

question2 = input("What is the largest passenger aircraft in the world?\n")

while True:
    if question2 == "B":
        print("Correct!\n")
        score = score + 1
    elif question2 == "b":
        print("Correct!\n")
        score = score + 1
    elif question2 == "Airbus A380":
        print("Correct!\n")
        score = score + 1
    else:
        print("Incorrect\n")
    break

print("A - " + (quest3[0]))
print("B - " + (quest3[1]))
print("C - " + (quest3[2]))
print("D - " + (quest3[3]))
print("E - " + (quest3[4]))
print("")

question3 = input("What language was this quiz written in?\n")

while True:
    if question3 == "A":
        print("Correct!\n")
        score = score + 1
    elif question3 == "a":
        print("Correct!\n")
        score = score + 1
    elif question3 == "Python":
        print("Correct!\n")
        score = score + 1
    else:
        print("Incorrect\n")
    break

print("A - " + (quest4[0]))
print("B - " + (quest4[1]))
print("C - " + (quest4[2]))
print("D - " + (quest4[3]))
print("E - " + (quest4[4]))
print("")

question4 = input("Out of the list, which of these people co-founded Microsoft?\n")

while True:
    if question4 == "D":
        print("Correct!\n")
        score = score + 1
    elif question4 == "d":
        print("Correct!\n")
        score = score + 1
    elif question4 == "Bill Gates":
        print("Correct!\n")
        score = score + 1
    else:
        print("Incorrect\n")
    break

print("A - " + (quest5[0]))
print("B - " + (quest5[1]))
print("C - " + (quest5[2]))
print("D - " + (quest5[3]))
print("E - " + (quest5[4]))
print("")

question5 = input("What is the capital city of the UK?\n")

while True:
    if question5 == "B":
        print("Correct!\n")
        score = score + 1
    elif question5 == "b":
        print("Correct!\n")
        score = score + 1
    elif question5 == "London":
        print("Correct!\n")
        score = score + 1
    else:
        print("Incorrect\n")
    break

print(total, score)
time.sleep(20)