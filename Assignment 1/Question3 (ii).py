print("=================================================")
print("Question 3 (ii)")
print("=================================================")

class Book:
    # Constructor used to initialize the book details
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Method used to display the book details
    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print(f"Price: ${self.price:.2f}")


# Instantiate two Book objects
book1 = Book("BBMIT Crash Course", "Romeo Chinakidzwa", 25.99)
book2 = Book("UnderGrad", "Tatenda Chinakidzwa", 34.50)

# Display the first book
print("Book 1 Details:")
book1.display_details()

# Display the second book
print("\nBook 2 Details:")
book2.display_details()
