from bson.objectid import ObjectId

from db import person_collection, production_db


# we have to be sure if the address will be referenced by just 1 person then we can embed it, however if needed by multiple persons then create a separate collection. for "one-to-many relationship".  or if it's one-to-one relationship

person = {
    '_id': ObjectId('668527771beeea7c639dfe8e'),
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'address': {
        '_id': ObjectId('668527771beeea7c639dfe8f'),
        'street': '123 Main St',
        'number': 'Apt 4B',
        'city': 'Springfield',
        'country': 'USA',
        'zip': '01101'
    }
}


address = {
    '_id': ObjectId('668527771beeea7c639dghtj'),
    'street': '456 Elm St',
    'number': 1234,
    'city': 'Shelbyville',
    'country': 'USA',
    'zip': 54321
}


def add_address_embed(person_id, person_address):
    _id = ObjectId(person_id)

    person_collection.update_one({'_id': _id}, {'$addToSet': {'addresses': person_address}})    # $addToSet, make the addresses an array, add the field if it does not already exist, and also will ensure the address is added only if it does not already exist in the array.

# add_address_embed('668527771beeea7c639dfe90', address)


def add_address_relationship(person_id, person_address):
    _id = ObjectId(person_id)

    person_address = person_address.copy()
    person_address['owner_id'] = person_id

    address_collection = production_db.address       # create as separate address collection in the database
    address_collection.insert_one(person_address)

# add_address_relationship('668527771beeea7c639dfe8d', address)