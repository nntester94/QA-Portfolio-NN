class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def describe(self):
        print(f'"{self.title}" by {self.author} , ({self.year})')

book1 = Book("Harry Potter", "J.K.Rowling", "1997")
book2 = Book("Princess diaries", "Jack", "2004")


book1.describe()
book2.describe()