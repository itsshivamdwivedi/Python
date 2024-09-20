class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []
    def addbooks(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)
    def showinfo(self):
        print(f"The library has {self.nobooks}books and the books are {self.books}")
l1 = library()
l1.addbooks("book1")
l1.addbooks("book2")
l1.addbooks("book3")
l1.addbooks("book4")
l1.showinfo()