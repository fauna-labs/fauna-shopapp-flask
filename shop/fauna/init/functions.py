
# Functions are not supported by python driver. Here is plain FQL

# check if categories exists
# CreateFunction({
#     "name": "check_if_categories_exists",
#     "role": "server",
#     "body": Query(
#         Lambda(
#             "categories_ids",
#             All(
#             Map(
#                 Var("categories_ids"),
#                 Lambda("id", Exists(Ref(Collection("categories"), Var("id"))))
#             )
#             )
#         )
#     )
# })

# purchase product
# CreateFunction({
#     "name": "purchase",
#     "role": "server",
#     "body": Query(
#         Lambda(
#             "productRef",
#             Let(
#             {
#                 product: Get(Var("productRef")),
#                 productPrice: Select(["data", "price"], Var("product")),
#                 productQuantity: Select(["data", "quantity"], Var("product")),
#                 customerBalance: Select(["data", "balance"], Get(CurrentIdentity()))
#             },
#             If(
#                 And(
#                 GTE(Var("customerBalance"), Var("productPrice")),
#                 GT(Var("productQuantity"), 0)
#                 ),
#                 Do(
#                 Update(CurrentIdentity(), {
#                     data: {
#                     balance: Subtract(Var("customerBalance"), Var("productPrice"))
#                     }
#                 }),
#                 Update(Var("productRef"), {
#                     data: { quantity: Subtract(Var("productQuantity"), 1) }
#                 }),
#                 Create(Collection("orders"), {
#                     data: {
#                     customer: CurrentIdentity(),
#                     product: Var("productRef"),
#                     status: "purchased",
#                     statusAt: Now()
#                     }
#                 })
#                 ),
#                 Abort("Not sufficient funds or product sold out")
#             )
#             )
#         )
#     )
# })

# get order status history
# CreateFunction({
#   "name": "get_order_status_history",
#   "role": "server",
#   "body": Query(
#     Lambda(orderRef => 
#       Map(
#         Filter(
#           Select(
#             ["data"],
#             Paginate(Events(orderRef))
#           ),
#           Lambda(event => 
#             And(
#               Equals(Select(["action"], event), "update"),
#               ContainsField("status", Select(["data"], event)),
#               ContainsField("statusAt", Select(["data"], event))
#             )
#           )
#         ),
#         Lambda(history => Select(["data"], history))
#       )
#     ))
# })
