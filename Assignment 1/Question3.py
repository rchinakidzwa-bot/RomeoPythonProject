print("=================================================")
print("Question 3 (i)")
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
