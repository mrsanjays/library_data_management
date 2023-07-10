class LibraryItem:
    def __init__(self):
        self.__id = None
        self.title = None
        self.year = None

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def library(self):
        print(f"Available book id is {self.id} and title is {self.title} Published in {self.year}")

class Book(LibraryItem):

    def __init__(self):
        super().__init__()
        self.author = None

    def author_name(self):
        print(f"Author name is {self.author}")

class Magazine(Book):
    def __init__(self):
        super().__init__()

        self.issue = None

    def author_name(self, year):
        print(f"This book was issued in the year {year}")


if __name__ == "__main__":
    book = Magazine()
    book.title="Python"
    book.id=231
    book.year=1989
    book.author="Charles"
    print(book.title,book.id,book.year,book.author)
    obj=LibraryItem()
    obj.set_id(23)
    obj.title="Java"
    obj.year=2000
    print(obj.get_id())
    obj.library()
