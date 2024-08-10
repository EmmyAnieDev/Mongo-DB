import pprint
from bson.objectid import ObjectId

from db import test_collection, person_collection

printer = pprint.PrettyPrinter()


def insert_test_doc():
    test_document = {
        "name": "Emmy",
        "type": "Test"
    }

    inserted_id = test_collection.insert_one(test_document).inserted_id        # inserts a single document into a collection.
    print(inserted_id)

# insert_test_doc()


def find_all_people():
    people = person_collection.find()      # use to find/get all the document in the collection

    for person in people:
        printer.pprint(person)

# find_all_people()


def find_person():
    person = person_collection.find_one({'first_name': 'Jessica'})
    if not person:
        print('person not found')
    printer.pprint(person)

# find_person()


def count_all_people():
    count = person_collection.count_documents(filter={})
    print('person count is', count)

# count_all_people()


def get_person_by_id(person_id):

    _id = ObjectId(person_id)              # convert a string to objectId
    person = person_collection.find_one({'_id': _id})
    printer.pprint(person)

# get_person_by_id('668527771beeea7c639dfe8e')


def get_age_range(min_age, max_age):
    query = {'$and': [               # $and is the logical AND operator, ensuring that both conditions must be met.
        {'age': {'$gte': min_age}},  # Selects documents where 'age' is greater than or equal to min_age
        {'age': {'$lte': max_age}}  # Selects documents where 'age' is less than or equal to max_age
    ]}

    people = person_collection.find(query).sort('age')
    for person in people:
        printer.pprint(person)

# get_age_range(20, 25)


def project_columns():
    columns = {'_id': 0, 'first_name': 1, 'last_name': 1}     # '0' will not get the users id, '1' will get their names
    people = person_collection.find({}, columns)

    for person in people:
        printer.pprint(person)

# project_columns()


def update_person_by_id(person_id):
    _id = ObjectId(person_id)

    # Uncomment the following lines if you want to perform multiple updates at once
    # all_update = {
    #     '$set': {'new_field': True},               # $set operator is used to update the value of a field in a document. If the field does not exist, it will create it.
    #     '$inc': {'age': 1},                       # $inc operator increments the value of a field by a specified amount.
    #     '$rename': {'first_name': 'replaced_first_name', 'last_name': 'replaced_last_name'}          # $rename operator renames a field.
    # }
    # person_collection.update_one({'_id': _id}, all_update)

    person_collection.update_one({'_id': _id}, {'$unset': {'new_field': ''}})        # The $unset operator in MongoDB is used to delete a field from a document.


# update_person_by_id('668527771beeea7c639dfe8e')


def replace_one(person_id):    # use this when a person want to change all other field but keeping same user id
    _id = ObjectId(person_id)

    new_doc = {
        'first_name': 'changed',
        'last_name': 'edited',
        'age': 28
    }

    person_collection.replace_one({'_id': _id}, new_doc)

# replace_one('668527771beeea7c639dfe8e')


def delete_person_by_id(person_id):
    _id = ObjectId(person_id)

    person_collection.delete_one({'_id': _id})
   # person_collection.delete_many()  # to delete all documents

# delete_person_by_id('668527771beeea7c639dfe91')