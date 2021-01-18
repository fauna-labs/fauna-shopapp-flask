from faunadb import query as q
from shop.fauna.client import FaunaClient


def get_orders(secret, after=None, before=None, size=5):
    client = FaunaClient(secret=secret)
    return client.query(
        q.map_(
            lambda ref: q.get(ref),
            q.paginate(q.documents(q.collection('orders')), size=size, after=after, before=before)
        )
    )

def find_order(secret, order_ref):
    client = FaunaClient(secret=secret)
    return client.query(
        q.let(
            {
                "order": q.get(q.ref(q.collection("orders"), order_ref)),
                "status_history": q.call("get_order_status_history", q.select(["ref"], q.var("order")))
            }, 
            {
                "ref": q.select(["ref"], q.var("order")),
                "data": q.merge(q.select(["data"], q.var("order")), {"status_history": q.var("status_history")})
            }
        )
    )

def update_status(secret, order_ref, status):
    client = FaunaClient(secret=secret)
    return client.query(
        q.update(
            q.ref(q.collection('orders'), order_ref),
            {"data": {
                "status": status,
                "statusAt": q.now()
            }}
        )
    )
