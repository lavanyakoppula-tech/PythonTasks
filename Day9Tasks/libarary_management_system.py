# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)


# Derived class
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)   # call parent constructor
        self.file_size = file_size

    def display_ebook(self):
        self.display_book()               # reuse parent method
        print("File Size:", self.file_size)


# Main function
def main():
    ebook = EBook("Python Programming", "John Doe", "5MB")
    ebook.display_ebook()


# Entry point
if __name__ == "__main__":
    main()
