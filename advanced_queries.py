import pprint

from db import production_db

printer = pprint.PrettyPrinter()


# print books that has letter a in title.
def find_letter_in_title(letter):
    books_containing_letter_a = production_db.book.find({"title": {"$regex": letter}})
    returned_books = list(books_containing_letter_a)
    printer.pprint(returned_books)
    print(len(returned_books))

# find_letter_in_title('a')


def print_authors_and_books():

    # Perform an aggregation query on the 'author' collection
    authors_and_books = production_db.author.aggregate([
        {
            # Use the $lookup stage to perform a left outer join with the 'book' collection
            "$lookup": {
                "from": "book",              # The collection to join with ('book')
                "localField": "_id",         # The field from the 'author' collection to match (author's _id)
                "foreignField": "authors",   # The field from the 'book' collection to match (book's authors field)
                "as": "books"                # The name of the new array field to add to each author document (books)
            }
        }
    ])


    printer.pprint(list(authors_and_books))

# print_authors_and_books()


def print_authors_book_count():

    authors_book_count = production_db.author.aggregate([
        {
            "$lookup": {
                "from": "book",
                "localField": "_id",
                "foreignField": "authors",
                "as": "books"
            }
        },
        {
            "$addFields": {      # Add a new field 'total_books' to each document, which is the size of the 'books'(author books) array
                "total_books": {"$size": "$books"}
            }
        },
        {
            "$project": {"first_name": 1, "last_name": 1, "total_books": 1, "_id": 0}     # show or project only the desired fields
        }
    ])

    printer.pprint(list(authors_book_count))

# print_authors_book_count()


def print_books_with_old_authors(lesser_age, bigger_age):
    # Perform an aggregation query on the 'book' collection
    books_with_old_authors = production_db.book.aggregate([
        {
            # Use the $lookup stage to join the 'book' collection with the 'author' collection
            # This matches books with their authors based on the authors' IDs
            "$lookup": {
                "from": "author",          # The collection to join with
                "localField": "authors",   # Field from the 'book' collection
                "foreignField": "_id",     # Field from the 'author' collection
                "as": "authors"            # Output array field
            }
        },
        {
            # Calculate the age of each author based on their birthdate
            "$set": {
                "authors": {
                    # $map allows transformation of each element in the 'authors' array
                    "$map": {
                        "input": "$authors",  # The array to iterate over
                        "in": {               # Transformation for each element
                            "age": {
                                # Calculate the age using $dateDiff
                                "$dateDiff": {
                                    "startDate": "$$this.date_of_birth",  # Author's birthdate
                                    "endDate": "$$NOW",                   # Current date
                                    "unit": "year"                        # Unit for difference calculation
                                }
                            },
                            "first_name": "$$this.first_name",   # Include the author's first name
                            "last_name": "$$this.last_name"      # Include the author's last name
                        }
                    }
                }
            }
        },
        {
            # Filter the books to include only those with authors whose age falls within the specified range
            "$match": {
                "$and": [
                    {"authors.age": {"$gte": lesser_age}},  # Author's age must be greater than or equal to 'lesser_age'
                    {"authors.age": {"$lte": bigger_age}}   # Author's age must be less than or equal to 'bigger_age'
                ]
            }
        },
        {
            # Sort the results by age in ascending order
            "$sort": {
                "authors.age": 1  # Sort by 'age' in ascending order (1 for ascending, -1 for descending)
            }
        }
    ])

    # Pretty print the list of books with authors that match the criteria
    printer.pprint(list(books_with_old_authors))

print_books_with_old_authors(100, 150)