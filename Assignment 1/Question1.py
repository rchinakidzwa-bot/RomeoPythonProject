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
