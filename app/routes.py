from flask import Blueprint, jsonify

class Book:
    
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "mobys dick", "huge whale"),
    Book(2, "the war and the peace", "so much happening"),
    Book(3, "the bible", "the word of god"),
    Book(4, "The Legend of Zelda: The Wind Waker Official Strategy Guide", "all the tips and tricks you need to win the game")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description,
        })
    return jsonify(books_response)