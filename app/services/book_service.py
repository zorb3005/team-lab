from app.storage.json_storage import JSONStorage

storage = JSONStorage()

def add_book(title):
    books = storage.read()
    if title in books:
        print("A book with that title already exists")
        return
    books.append(title)
    storage(books)
    print("A book was added.")

def delete_book(title):
    books = storage.read()
    if title not in books:
        print("No such book.")
        return
    books.remove(title)
    storage.write(books)
    print("A book was deleted.")

def list_books():
    books = storage.read()
    if not books:
        print("There is no books.")
    else:
        for book in books:
            print(f"- {book}")
def get_book(title, storage):
    books = storage.read()
    if title in books:
        print(f"A book was found: {title}")
    else:
        print("Book not found.")
