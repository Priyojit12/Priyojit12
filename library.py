# print("heelo world")

class library:
    def __init__(self):
        self.nobooks = 0 
        self.books = []
    def add(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)
    def info(self):
        print(f"number of books is {self.nobooks}. the books are:-")
        for books in self.books:
            print(books)

l1 = library()
l1.add("a song of ice and fire")
l1.add("lord of the rings")
l1.add("harry potter")
l1.info()

