from fastapi import FastAPI,Body

app = FastAPI()
book = {
    1: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction"},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Classic"},
    3: {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian"},
    4: {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "genre": "Romance"},
    5: {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "genre": "Fiction"},
    6: {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851, "genre": "Adventure"},
    7: {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy"},
    8: {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869, "genre": "Historical"},
    9: {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866, "genre": "Philosophical"},
    10: {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988, "genre": "Fiction"},
}



@app.get('/book/{book_author}/')
def first_app(book_author:str,category:str):
    book_to_return=[]
    for b in book.values():
        if b["author"].casefold() == book_author.casefold() and b["genre"].casefold() == category.casefold():
            book_to_return.append(b)
        

    return book_to_return

@app.post("/add_book/{book_id}/")
def add_book(book_id: int, new_book: Body()): # type: ignore
    book[book_id] = new_book.dict()  # Correct way to add a book
    return {"message": "Book added successfully", "data": book[book_id]}