from abc import ABC, abstractmethod


class FileHandler(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        """Read information from a file."""
        pass

    @abstractmethod
    def write(self, data):
        """Write information to a file."""
        pass


class TextFileHandler(FileHandler):
    def read(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()
                print("Text file content:")
                print(content)
                return content

        except FileNotFoundError:
            print(f"Text file '{self.filename}' was not found.")

        except OSError as error:
            print("An error occurred while reading the text file:", error)

    def write(self, data):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(data)

            print("Text data written successfully.")

        except OSError as error:
            print("An error occurred while writing the text file:", error)


class BinaryFileHandler(FileHandler):
    def read(self):
        try:
            with open(self.filename, "rb") as file:
                content = file.read()
                print("Binary file content:", content)
                return content

        except FileNotFoundError:
            print(f"Binary file '{self.filename}' was not found.")

        except OSError as error:
            print("An error occurred while reading the binary file:", error)

    def write(self, data):
        try:
            with open(self.filename, "wb") as file:
                file.write(data)

            print("Binary data written successfully.")

        except TypeError:
            print("Binary data must be supplied as bytes.")

        except OSError as error:
            print("An error occurred while writing the binary file:", error)


# Demonstrate the text file handler
text_handler = TextFileHandler("notes.txt")
text_handler.write("Python supports abstract classes.")
text_handler.read()

print()

# Demonstrate the binary file handler
binary_handler = BinaryFileHandler("data.bin")
binary_handler.write(b"Binary file information")
binary_handler.read()