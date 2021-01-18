from faunadb import query as q
from shop.fauna.client import fauna


def get_categories():
    return fauna.query(
        q.map_(
            lambda ref: q.get(ref),
            q.paginate(q.documents(q.collection('categories')))
        )
    )
