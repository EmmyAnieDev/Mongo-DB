from db import production_db


def create_book_collection():
    book_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["title", "authors", "publish_date", "type", "copies"],
            "properties": {
                "title": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "authors": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "objectId",
                        "description": "must be an objectId and is required"
                    }
                },
                "publish_date": {
                    "bsonType": "date",
                    "description": "must be a date and is required"
                },
                "type": {
                    "enum": ["Fiction", "Non-Fiction"],
                    "description": "can only be one of the enum values and is required"
                },
                "copies": {
                    "bsonType": "int",
                    "minimum": 0,
                    "description": "must be an integer greater than or equal to 0 and is required"
                }
            }
        }
    }

    try:
        production_db.create_collection('book')
    except Exception as e:
        print(e)

    production_db.command('collMod', 'book', validator=book_validator)     # updates the schema validation rules for the "book" collection in the "production_db" database

# create_book_collection()


def create_author_collection():
    author_validator = {
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['first_name', 'last_name', 'date_of_birth'],
            'properties': {
                'first_name': {
                    'bsonType': 'string',
                    'description': 'must be a string and is required'
                },
                'last_name': {
                    'bsonType': 'string',
                    'description': 'must be a string and is required'
                },
                'date_of_birth': {
                    'bsonType': 'date',
                    'description': 'must be a date and is required'
                }
            }
        }
    }

    try:
        production_db.create_collection('author')
    except Exception as e:
        print(e)

    production_db.command('collMod', 'author', validator=author_validator)

# create_author_collection()