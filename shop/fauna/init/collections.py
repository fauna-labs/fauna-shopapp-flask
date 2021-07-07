from faunadb import query as q
from shop.fauna.client import wordPartsGenerator


def create_collection(client):
    collections = ["products", "users", "orders", "categories"]
    client.query(q.map_(
        lambda collection_name: q.if_(
            q.exists(q.collection(collection_name)),
            True,
            q.create_collection({ "name": collection_name })
        ),
        collections
    ))

def create_indexes(client):
    indexes = [
        {
            "name": "user_by_email",
            "source": q.collection("users"),
            "terms": [{ "field": ["data", "email"] }],
        },
        {
            "name": "products_search_by_name", 
            "source": {
                "collection": q.collection('products'),
                "fields": {
                    "wordparts": q.query(lambda product: wordPartsGenerator(q.select(['data', 'name'], product)))
                }
            },
            "terms": [{"binding": 'wordparts'}],
        },
        {
            "name": "products_search_by_category", 
            "source": q.collection('products'),
            "terms": [{"field": ["data", "categories"]}],
        },
        {
            "name": "products_sort_by_name_asc", 
            "source": q.collection('products'), 
            "terms": [{ "field": ["ref"] }],
            "values": [
                {"field": ["data", "name"]},
                {"field": ["ref"]},
            ]
        },
        {
            "name": "products_sort_by_price_asc", 
            "source": q.collection('products'), 
            "terms": [{ "field": ["ref"] }],
            "values": [
                {"field": ["data", "price"]},
                {"field": ["ref"]},
            ]
        },
        {
            "name": "products_sort_by_price_desc", 
            "source": q.collection('products'), 
            "terms": [{ "field": ["ref"] }],
            "values": [
                {"field": ["data", "price"], "reverse": True},
                {"field": ["ref"]},
            ]
        },
        {
            "name": "products_sort_by_created_asc", 
            "source": q.collection('products'), 
            "values": [
                {"field": ["data", "createdAt"]},
                {"field": ["ref"]},
            ]
        }
    ]

    client.query(q.map_(
        lambda index: q.if_(
            q.exists(q.index(q.select(["name"], index))),
            True,
            q.create_index(index)
        ),
        indexes
    ))

def init(client):
    create_collection(client)
    create_indexes(client)
