
print("=================================================")
print("Question 1")
print("=================================================")

while True:

#Interger

    age_input = input("Enter your age: ")
    try:
        age = int(age_input)

        break

    except ValueError:
        print("That is not a valid number. Please try again.")

print(f"Thank you for your age. You are {age} years old.")


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

# ---- Part 1: Students and marks ----

students = {"Ronny": 78,"Rob": 85,"Romeo": 92,"Talent": 67,"Miranda": 88}

print("Students and their marks:")
for name in students:
    print(name, ":", students[name])

# Student with the highest mark

top_name = ""
top_mark = 0
for name in students:
    if students[name] > top_mark:
        top_mark = students[name]
        top_name = name

print("Student with the highest mark:", top_name, "with", top_mark)

#======== Part 2 ===================

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book1 = Book("BBMIT Crash Course", "Romeo Chinakidzwa", 25.99)
book2 = Book("UnderGrad", "Tatenda Chinakidzwa", 34.50)

print("\nBook 1 details:")
book1.display_details()

print("\nBook 2 details:")
book2.display_details()

print("=================================================")
print("Question 4")
print("=================================================")

from datetime import datetime
from collections import Counter


def find_peak_usage(logs):

    if not logs:
        return None

    hours = []


    for timestamp in logs:
        login_time = datetime.fromisoformat(timestamp)
        hours.append(login_time.hour)


    hour_counts = Counter(hours)


    highest_count = max(hour_counts.values())


    peak_hours = [
        hour for hour, count in hour_counts.items()
        if count == highest_count
    ]


    return min(peak_hours)


logs = ["2026-08-04T13:21:18","2026-08-04T13:45:10","2026-08-04T09:15:20","2026-08-04T13:55:30",
        "2026-08-04T09:35:40","2026-08-04T16:10:00"]

peak_hour = find_peak_usage(logs)

print("Peak login hour:", peak_hour)