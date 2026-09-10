print("=================================================")
print("Question 2")
print("=================================================")

#List
fruits = ["Mango", "Banana", "Apple", "Pineapple", "Orange"]

with open("../Practice/fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

with open("../Practice/fruits.txt", "r") as file:
    for line in file:
        print(line.strip())


