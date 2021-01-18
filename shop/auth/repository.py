from faunadb import query as q
from shop.fauna.client import fauna


def login(email, password):
    return fauna.query(
        q.login(q.match(q.index('user_by_email'), email), {"password": password})
    )
