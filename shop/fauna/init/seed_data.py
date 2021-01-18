from faunadb import query as q


def seed_categories(client):
    client.query(q.map_(
        lambda categoryRef: q.delete(categoryRef),
        q.paginate(q.documents(q.collection('categories')))
    ))

    categories = [
        {"name": "Phones"},
        {"name": "Laptops"},
        {"name": "Watches"},
        {"name": "Apple"}
    ]

    return client.query(q.map_(
        lambda category: q.create(q.collection('categories'), {"data": category}),
        categories
    ))

def seed_products(client, categoryRefs):
    client.query(q.map_(
        lambda productRef: q.delete(productRef),
        q.paginate(q.documents(q.collection('products')))
    ))
    products = [
        {"name": "Apple IPhone 12 mini", "price": 999, "createdAt": q.now(), "quantity": 13, "categories": [categoryRefs[0]["ref"], categoryRefs[3]["ref"]]},
        {"name": "Apple IPhone 12", "price": 1199, "createdAt": q.now(), "quantity": 13, "categories": [categoryRefs[0]["ref"], categoryRefs[3]["ref"]]},
        {"name": "Apple IPhone 12 PRO", "price": 1399, "createdAt": q.now(), "quantity": 13, "categories": [categoryRefs[0]["ref"], categoryRefs[3]["ref"]]},
        {"name": "Apple IPhone 11 PRO", "price": 1139, "createdAt": q.now(), "quantity": 13, "categories": [categoryRefs[0]["ref"], categoryRefs[3]["ref"]]},
        {"name": "Apple IPhone 11", "price": 969, "createdAt": q.now(), "quantity": 100, "categories": [categoryRefs[0]["ref"], categoryRefs[3]["ref"]]},
        {"name": "Apple Macbook PRO", "price": 2399, "createdAt": q.now(), "quantity": 7, "categories": [categoryRefs[1]["ref"], categoryRefs[3]["ref"]]},
        {"name": "Apple Apple Watch Series 6", "price": 399, "createdAt": q.now(), "quantity": 7, "categories": [categoryRefs[2]["ref"], categoryRefs[3]["ref"]]},
        {"name": "Apple Watch SE", "price": 279, "createdAt": q.now(), "quantity": 7, "categories": [categoryRefs[2]["ref"], categoryRefs[3]["ref"]]},
        {"name": "Apple Watch Series 3", "price": 199, "createdAt": q.now(), "quantity": 7, "categories": [categoryRefs[2]["ref"], categoryRefs[3]["ref"]]},
        {"name": "Xiaomi 9", "price": 999, "createdAt": q.now(), "quantity": 13, "categories": [categoryRefs[0]["ref"]]},
        {"name": "Xiaomi 8", "price": 999, "createdAt": q.now(), "quantity": 13, "categories": [categoryRefs[0]["ref"]]},
        {"name": "Emporio Armani AR1732", "price": 300, "createdAt": q.now(), "quantity": 29, "categories": [categoryRefs[2]["ref"]]},
        {"name": "Diesel DZ4318", "price": 340, "createdAt": q.now(), "quantity": 29, "categories": [categoryRefs[2]["ref"]]},
        {"name": "Casio GST-B100", "price": 600, "createdAt": q.now(), "quantity": 2, "categories": [categoryRefs[2]["ref"]]},
    ]

    client.query(q.map_(
        lambda product: q.create(q.collection('products'), {"data": product}),
        products
    ))

def seed_users(client):
    client.query(q.map_(
        lambda userRef: q.delete(userRef),
        q.paginate(q.documents(q.collection('users')))
    ))
    users = [
        {"data": {"email": "admin@shop.com", "type": "admin"}, "credentials": {"password": "111111"}},
        {"data": {"email": "customer@shop.com", "balance": 1000, "type": "customer"}, "credentials": {"password": "111111"}},
        {"data": {"email": "rich_customer@shop.com", "balance": 100000, "type": "customer"}, "credentials": {"password": "111111"}},
    ]

    client.query(q.map_(
        lambda user: q.create(q.collection('users'), user),
        users
    ))


def seed(client):
    seed_products(client, seed_categories(client))
    seed_users(client)
