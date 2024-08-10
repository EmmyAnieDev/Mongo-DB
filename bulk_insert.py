from db import person_collection, production_db
from datetime import datetime
from bson.objectid import ObjectId


def bulk_insert_looping_individually():
    first_names = ["Emily", "Michael", "Sarah", "David", "Jessica", "Daniel"]
    last_names = ["Johnson", "Smith", "Brown", "Lee", "Martinez", "Garcia"]
    ages = [27, 34, 22, 29, 31, 25]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):   # zip returns the items at the corresponding indices as a tuple
        doc = {'first_name': first_name, 'last_name': last_name, 'age': age}
        docs.append(doc)

    person_collection.insert_many(docs)      # inserts a multiple document into a collection.

# bulk_insert_looping_individually()


def bulk_insert_authors():         # this way is better and understandable.

    authors = [      # added first_name, last_name and date_of_birth as required in the "author_validator "schema
        {
            "first_name": "Jane",
            "last_name": "Austen",
            "date_of_birth": datetime(1775, 12, 16)
        },
        {
            "first_name": "Mark",
            "last_name": "Twain",
            "date_of_birth": datetime(1835, 11, 30)
        },
        {
            "first_name": "George",
            "last_name": "Orwell",
            "date_of_birth": datetime(1903, 6, 25)
        },
        {
            "first_name": "Virginia",
            "last_name": "Woolf",
            "date_of_birth": datetime(1882, 1, 25)
        },
        {
            "first_name": "Ernest",
            "last_name": "Hemingway",
            "date_of_birth": datetime(1899, 7, 21)
        },
        {
            "first_name": "Harper",
            "last_name": "Lee",
            "date_of_birth": datetime(1926, 4, 28)
        }
    ]

    authors_collection = production_db.author  # initialize the collection
    author_id = authors_collection.insert_many(authors).inserted_ids        # getting the author's ID


# bulk_insert_authors()


def bulk_insert_books():
    books = [
        {
            "title": "To Kill a Mockingbird",
            "authors": [ObjectId("6689c6a69d788fa8dc161279")],
            "publish_date": datetime(1960, 7, 11),
            "type": "Fiction",
            "copies": 5
        },
        {
            "title": "1984",
            "authors": [ObjectId("6689c592602798f3e6c55fd0")],
            "publish_date": datetime(1949, 6, 8),
            "type": "Fiction",
            "copies": 3
        },
        {
            "title": "Brief History of Time",
            "authors": [ObjectId("60c72b2f4f1a4c5d88f7d517")],
            "publish_date": datetime(1988, 4, 1),
            "type": "Non-Fiction",
            "copies": 4
        },
        {
            "title": "Sapiens: A Brief History of Humankind",
            "authors": [ObjectId("6689c592602798f3e6c55fd4")],
            "publish_date": datetime(2011, 9, 4),
            "type": "Non-Fiction",
            "copies": 6
        },
        {
            "title": "The Great Gatsby",
            "authors": [ObjectId("6689c592602798f3e6c55fd0")],
            "publish_date": datetime(1925, 4, 10),
            "type": "Fiction",
            "copies": 2
        }
    ]


    books_collection = production_db.book
    books_collection.insert_many(books)

# bulk_insert_books()