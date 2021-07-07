
from faunadb import query as q


def init(client):

  client.query(q.create_function({
    "name": "check_if_categories_exists",
    "role": "server",
    "body": q.query(
        q.lambda_(
            "categories_ids",
            q.all(
            q.map_(
                q.lambda_("id", q.exists(q.ref(q.collection("categories"), q.var("id")))),
                q.var("categories_ids"),
            )
            )
        )
    )
  }))

  client.query(
    q.create_function({
    "name": "purchase",
    "role": "server",
    "body": q.query(
        q.lambda_(
            "productRef",
            q.let(
            {
                "product": q.get(q.var("productRef")),
                "productPrice": q.select(["data", "price"], q.var("product")),
                "productQuantity": q.select(["data", "quantity"], q.var("product")),
                "customerBalance": q.select(["data", "balance"], q.get(q.current_identity()))
            },
            q.if_(
                q.and_(
                q.gte(q.var("customerBalance"), q.var("productPrice")),
                q.gt(q.var("productQuantity"), 0)
                ),
                q.do(
                q.update(q.current_identity(), {
                    "data": {
                    "balance": q.subtract(q.var("customerBalance"), q.var("productPrice"))
                    }
                }),
                q.update(q.var("productRef"), {
                    "data": { "quantity": q.subtract(q.var("productQuantity"), 1) }
                }),
                q.create(q.collection("orders"), {
                    "data": {
                      "customer": q.current_identity(),
                      "product": q.var("productRef"),
                      "status": "purchased",
                      "statusAt": q.now()
                    }
                })
                ),
                q.abort("Not sufficient funds or product sold out")
            )
            )
        )
    )
})
  )

  client.query(
    q.create_function({
  "name": "get_order_status_history",
  "role": "server",
  "body": q.query(
    q.lambda_("orderRef" ,
      q.map_(
        q.lambda_("history", q.select(["data"], q.var("history"))),
        q.filter_(
          q.lambda_("event", 
            q.and_(
              q.equals(q.select(["action"], q.var("event")), "update"),
              q.contains_field("status", q.select(["data"], q.var("event"))),
              q.contains_field("statusAt", q.select(["data"], q.var("event")))
            )
          ),
          q.select(
            ["data"],
            q.paginate(q.events(q.var("orderRef")))
          ),
        ),
      )
    ))
})

  )
  