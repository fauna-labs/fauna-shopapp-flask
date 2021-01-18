from faunadb import objects
from faunadb import query as q


def create_roles(client):
    roles = [
        {
            "name": "admin",
            "membership": [
                {
                    "resource": q.collection("users"),
                    "predicate": q.query(lambda ref: q.equals(q.select(["data", "type"], q.get(ref)), "admin"))
                }
            ],
            "privileges": [
                {
                    "resource": q.collection("categories"),
                    "actions": {
                        "read": True,
                        "create": True,
                        "write": True
                    }
                },
                {
                    "resource": q.collection("products"),
                    "actions": {
                        "read": True,
                        "write": True,
                        "create": True
                    }
                },
                {
                    "resource": q.collection("users"),
                    "actions": {
                        "read": True,
                        "create": True,
                        "write": True
                    }
                },
                {
                    "resource": q.collection("orders"),
                    "actions": {
                        "read": True,
                        "write": True,
                        "create": True
                    }
                }
            ]
        },
        {
            "name": "customer",
            "membership": [
                {
                    "resource": q.collection("users"),
                    "predicate": q.query(lambda ref: q.equals(q.select(["data", "type"], q.get(ref)), "customer"))
                }
            ],
            "privileges": [
                {
                    "resource": objects.Ref("purchase", objects.Ref("functions")),
                    "actions": {
                        "call": True
                    }
                },
                {
                    "resource": objects.Ref("get_order_status_history", objects.Ref("functions")),
                    "actions": {
                        "call": q.query(lambda ref: q.equals(q.current_identity(), q.select(["data", "customer"], q.get(ref)))),
                    }
                },
                {
                    "resource": q.collection("users"),
                    "actions": {
                        "read": q.query(lambda ref: q.equals(q.current_identity(), ref)),
                        "write": q.query(lambda ref: q.equals(q.current_identity(), ref)),
                    }
                },
                {
                    "resource": q.collection("orders"),
                    "actions": {
                        "read": q.query(lambda ref: q.equals(q.current_identity(), q.select(["data", "customer"], q.get(ref)))),
                    }
                }
            ]
            }
    ]
    client.query(q.map_(
        lambda role: q.create_role(role),
        roles
    ))
