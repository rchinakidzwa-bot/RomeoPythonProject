from typing import List
print("=================================================")
print("Question 1")
print("=================================================")

while True:
#while True:
#Interger
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("That is not a valid number. Please try again.")

    print("Your age is:", age)

print("=================================================")
print("Question 2")
print("=================================================")

#List
fruits = ["Mango", "Banana", "Apple", "Pineapple", "Orange"]

with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

with open("fruits.txt", "r") as file:
    for line in file:
        print(line.strip())

print("=================================================")
print("Question 3")
print("=================================================")
# ---- Part i: Students and marks ----

students = {"Romeo": 78,"Rob": 85,"Ronny": 92,"Talent": 67,"Miranda": 88}

print("Students and their marks:")
for name in students:
    print(name, ":", students[name])

# Find the student with the highest mark
top_name = ""
top_mark = 0
for name in students:
    if students[name] > top_mark:
        top_mark = students[name]
        top_name = name

print("Student with the highest mark:", top_name, "with", top_mark)
