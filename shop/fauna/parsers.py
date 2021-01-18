from faunadb import objects
from faunadb import query as q
from flask_restx import reqparse


class FaunaCursorParser(object):
    def __init__(self, collection, argument="argument"):
        self.collection = collection

    def __call__(self, value):
        splitted = value.split('cursor_ref=')
        if(len(splitted) == 2):
            return q.ref(q.collection(self.collection), splitted[1])
        else:
            return splitted[0]

def getFaunaCursorRequestParser(collection):
    fauna_cursors = reqparse.RequestParser()

    fauna_cursors.add_argument(
        'after', type=FaunaCursorParser(collection=collection), 
        required=False, action='append',
        store_missing=False, help='Value of `after` field from previous request'
    )

    fauna_cursors.add_argument(
        'before', type=fauna_cursor_parser(collection=collection), 
        required=False, action='append',
        store_missing=False, help='Value of `before` field from previous request'
    )

    fauna_cursors.add_argument(
        'size', type=int, required=False,
        choices=[5, 10, 20, 30, 40, 50], store_missing=False, 
        default=5, help='Results per page {error_msg}'
    )

    return fauna_cursors
