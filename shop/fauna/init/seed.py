from faunadb import objects
from faunadb import query as q
from shop.fauna.client import FaunaClient
from shop.fauna.init import collections, functions, roles, seed_data
from shop.settings import FAUNA_ADMIN_SECRET

fauna = FaunaClient(secret=FAUNA_ADMIN_SECRET)


collections.init(fauna)
functions.init(fauna)
seed_data.seed(fauna)
roles.create_roles(fauna)
