from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.objects import Ref
from shop.settings import FAUNA_SERVER_SECRET

fauna = FaunaClient(secret=FAUNA_SERVER_SECRET)


maxNgrams = list(range(50))
def wordPartsGenerator(word):
    return q.let({
        "indexes": q.map_(
            # Reduce this array if you want less ngrams per word.
            # Setting it to [ 0 ] would only create the word itself, Setting it to [0, 1] would result in the word itself
            # and all ngrams that are one character shorter, etc..
            lambda index: q.subtract(q.length(word), index),
            maxNgrams
        ),
        "indexesFiltered": q.filter_(
            # left min parts length 3
            lambda l: q.gte(l, 3),
            q.var('indexes')
        ),
        "ngramsArray": q.distinct(q.union(q.map_(
            lambda l: q.ngram(q.lowercase(word), l, l),
            q.var('indexesFiltered')
        )))
    },
    q.var('ngramsArray')
    )
