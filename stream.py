from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.objects import Ref

client = FaunaClient(
    secret='fnAD3l4SEZACAbxXBR1wGB3hRx4FI8fph21uztQ7',
    domain='db.fauna-preview.com'
)

stream = None
def on_start(event):
    print("started stream at %s"%(event.txn))

def on_version(event):
    print("on_version event at %s"%(event.txn))
    print("    event: %s"%(event.event))

def on_error(event):
    print("Received error event %s"%(event))
options = {"fields": ["document", "diff"]}
stream = client.stream(
    q.ref(q.collection('Status'),'278763355019149825'),
    options,
    on_start=on_start,
    on_version=on_version,
    on_error=on_error
)
stream.start()
