Sample shop API using Fauna and Python
=============

#### Table of Contents
* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Installation](#installation)

## Overview
This is the backend API service for a sample e-commerce application that uses [Fauna](https://docs.fauna.com/) as a database.

Features include:
- Authentication using [Fauna's built-in authentication methods](https://docs.fauna.com/fauna/current/tutorials/authentication/user)
- Authorization using [Fauna built-in ABAC](https://docs.fauna.com/fauna/current/tutorials/authentication/abac):
    * Only the Admin role is authorized for API requests to create or update products, or update order status.
    * The Customer role can only purchase products, and access his own list of orders.
- Sensitive purchase logic encapsulated server-side using [Fauna's User-Defined Functions](https://docs.fauna.com/fauna/current/tutorials/basics/functions): 
    * All conditions (user has a high enough balance, product is still available)
    * All actions (decrement product quantity, subtract product price from user balance, and create order document).
- Order status history is provided using [Fauna's built-in temporality](https://docs.fauna.com/fauna/current/tutorials/temporality).


## Prerequisites
* You will need to have Python with [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) and [Git](https://git-scm.com/) installed on your machine.
* I would recommend using Python 3, but Python 2 should work.


## Installation
To install the project and get the development environment running:

1. First, clone the application code into any directory on your disk:
```
$ cd /path/to/my/workspace/
$ git clone https://github.com/fireridlle/faunadb-shop.git
$ cd faunadb-shop
```

2. Create a virtual Python environment in a directory named `venv`, activate the virtualenv, and install required dependencies using `pip`:
```
$ virtualenv -p `which python3` venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

3. Rename `.env.sample` to `.env`

4. [Sign up for free](https://dashboard.fauna.com/accounts/register) or [log in](https://dashboard.fauna.com/accounts/login) at [dashboard.fauna.com](https://dashboard.fauna.com/accounts/register).
    * Click [CREATE DATABASE], name it "shopapp", select a region group (e.g., "Classic"), and click [CREATE].
    * Click the [SECURITY] tab at the bottom of the left sidebar, and [NEW KEY]. 
    * Create a Key with the default Role of "Admin" selected, and paste the secret into into your `.env` file's `FAUNA_SECRET_ADMIN_KEY`. We'll use this key during setup to seed the database with schema and sample data.
    * Create another key, but this time select "Server" from the "Role" dropdown. Paste the secret into your `.env` file's `FAUNA_SECRET_SERVER_KEY` field. The application will use this key to access the database.

5. Run the script to initialize collections, indexes, roles, and seed some data.
```
python -m shop.fauna.init.seed
```

6. In your [Fauna Dashboard](https://dashboard.fauna.com), click the [Shell] tab in the left sidebar, and then [Open File] to run this command from file `shop/fauna/functions.py`

7. Start the application
```
python -m shop.app
```

8. Open the Swagger documentation at [http://localhost:8888/api/](http://localhost:8888/api/). 

9. To test the requests via the Swagger UI, use any of the account credentials listed [here](https://github.com/fireridlle/faunadb-shop/blob/master/shop/fauna/init/seed_data.py#L54).
