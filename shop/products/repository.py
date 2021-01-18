from faunadb import query as q
from shop.fauna.client import FaunaClient, fauna


def get_products(name=None, category=None, sort_by=None, size=5, after=None, before=None):
    sortDic = { 
        "price_asc":  q.index('products_sort_by_price_asc'),
        "price_desc": q.index('products_sort_by_price_desc'),
        "name_asc": q.index('products_sort_by_name_asc'),
        'created_at_asc': q.index('products_sort_by_created_asc')
    }

    matches = []
    if(name):
        matches.append(q.match(q.index('products_search_by_name'), name))

    if(category):
        matches.append(q.match(
            q.index('products_search_by_category'),
            q.ref(q.collection('categories'), category)
        ))

    if(len(matches) == 0):
        matches.append(q.documents(q.collection('products')))

    print(after)
    print('>>')
    return fauna.query(
        q.map_(
            lambda _, ref: q.get(ref),
            q.paginate(
                q.join(
                    q.intersection(matches),
                    sortDic[sort_by or 'name_asc']
                ),
                size=size,
                after=after,
                before=before
            )
            
        )
    )

def find_product(product_ref):
    return fauna.query(q.get(q.ref(q.collection('products'), product_ref)))

def create_product(secret, name, price, quantity, categories):
    client = FaunaClient(secret=secret)
    return client.query(
        q.if_(
            q.call('check_if_categories_exists', categories),
            q.create(q.collection('products'), {"data": { 
                "name": name,
                "price": price,
                "quantity":quantity,
                "createdAt": q.now(),
                "categories": list(map(
                    lambda category: q.ref(q.collection("categories"), category),
                    categories
                ))
             }}),
            q.abort('Categories not found'),
        )
    )

def update_product(secret, ref, data):
    client = FaunaClient(secret=secret)
    if(data.get("categories") == None):
        return client.query(q.update(
            q.ref(q.collection('products'), ref),
            { "data": data }
        ))
    
    return client.query(
        q.if_(
            q.call('check_if_categories_exists', data.get("categories")),
            q.update(
                q.ref(q.collection('products'), ref),
                { "data": {
                    **data,
                    "categories": list(map(
                        lambda category: q.ref(q.collection("categories"), category),
                        data.get("categories")
                    ))
                } }
            ),
            q.abort('Categories not found'),
        )
    ) 
    
def purchase(secret, product_ref):
    client = FaunaClient(secret=secret)
    return  client.query(q.call('purchase', q.ref(q.collection('products'), product_ref)))
    