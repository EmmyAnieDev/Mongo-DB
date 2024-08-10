import pprint

from db import production_db

printer = pprint.PrettyPrinter()


def fuzzy_matching():
    result = production_db.book.aggregate([
        {
            "$search": {
                "index": "language_search",
                "text": {
                    "query": "histry",
                    "path": "title",
                    "fuzzy": {}
                }
            }
        }
    ])

    printer.pprint(list(result))

# fuzzy_matching()


def basic_search():
    result = production_db.book.aggregate([
        {
            "$search": {
                "index": "language_search",
                "text": {
                    "query": "History",
                    "path": "title"
                }
            }
        }
    ])

    printer.pprint(list(result))

# basic_search()


def synonym_search():
    result = production_db.book.aggregate([
        {
            "$search": {
                "index": "language_search",
                "text": {
                    "query": "before",
                    "path": "title",
                    "synonyms": "mapping"
                }
            }
        }
    ])

    printer.pprint(list(result))

# synonym_search()


def autocomplete_search():
    result = production_db.book.aggregate([
        {
            "$search": {
                "index": "language_search",
                "autocomplete": {
                    "query": "to kill a",  # if you want to do multiple, can use an array here.
                    "path": "title",
                    "tokenOrder": "sequential",  # we can also use "any". if we don't want the words arranged.
                    "fuzzy": {}
                }
            }
        },
        {
            "$project": {"_id": 0, "title": 1}     # show or project only the desired fields
        }
    ])

    printer.pprint(list(result))

# autocomplete_search()



# ,
#   "synonyms": [
#     {
#       "analyzer": "lucene.english",
#       "name": "mapping",
#       "source": {
#         "collection": "synonyms"
#       }
#     }
#   ]