import sqlite3

try:
    # Connect to the database.
    # The database file is created automatically if it does not exist.
    connection = sqlite3.connect("school.db")

    cursor = connection.cursor()

    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            programme TEXT NOT NULL,
            age INTEGER
        )
    """)

    # Clear old demonstration data to avoid duplicate records
    cursor.execute("DELETE FROM students")

    # Insert multiple records
    student_data = [
        ("Romeo", "BBMIT", 41),
        ("Israel", "Information Technology", 26),
        ("Tsitsidzashe", "Business Management", 31)
    ]

    cursor.executemany("""INSERT INTO students (name, programme, age)VALUES (?, ?, ?)""", student_data)

    # Save the changes
    connection.commit()

    # Retrieve records from the table
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("Student Records")
    print("-" * 50)

    for student in students:
        print(
            f"ID: {student[0]}, "
            f"Name: {student[1]}, "
            f"Programme: {student[2]}, "
            f"Age: {student[3]}"
        )

except sqlite3.Error as error:
    print("A database error occurred:", error)

finally:
    # Close the database connection
    if "connection" in locals():
        connection.close()
        print("\nDatabase connection closed.")