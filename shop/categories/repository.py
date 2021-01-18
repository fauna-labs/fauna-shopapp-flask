from faunadb import query as q
from shop.fauna.client import fauna


def get_categories(after=None, before=None, size=5):
    return fauna.query(
        q.map_(
            lambda ref: q.get(ref),
            q.paginate(q.documents(q.collection('categories')), size=size, after=after, before=before)
        )
    )
