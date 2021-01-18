FaunaDB simple shop API demonstration
=============

## Description 
This is a simple shop API server that use [FaunaDB](https://docs.fauna.com/) as database.
Features overview:
- Authentication using [FaunaDB authentication](https://docs.fauna.com/fauna/current/tutorials/authentication/user)
- Only admin can access create and update product, update order status api. [FaunaDB ABAC](https://docs.fauna.com/fauna/current/tutorials/authentication/abac)
- Only customer can purchase product. Customer can access only list of own orders [FaunaDB ABAC](https://docs.fauna.com/fauna/current/tutorials/authentication/abac)
- Using [FaunaDB Functions](https://docs.fauna.com/fauna/current/tutorials/basics/functions) encapsulate purchase logic with all conditions (user has enough balance, product is still available) and flow (decrement product quantity, subtract product price from user balance and create order document ).
- Using [FaunaDB Temporality](https://docs.fauna.com/fauna/current/tutorials/temporality) return order status history witch time when status has been changed

## Table of Contents
* [Prerequisites](#prerequisites)
* [Installation](#installation)

## Prerequisites
You will need to have Python with [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) and [Git](https://git-scm.com/) installed on your machine.

I would recommend using Python 3, but Python 2 should work just fine.


## Installation
Steps required to install project and how to get the development environment running:

First clone the application code into any directory on your disk:
```
$ cd /path/to/my/workspace/
$ git clone !!!!!update to my link
$ cd shop
```

Create a virtual Python environment in a directory named `venv`, activate the virtualenv and install required dependencies using `pip`:
```
$ virtualenv -p `which python3` venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Now we need to create account at FaunaDB. Please follow this [instruction](https://docs.fauna.com/fauna/current/start/cloud?lang=javascript#create-db)
Using dashboard, go to Security section and create ADMIN and SERVER tokens.
Admin token is required to init database (create roles for application)
Server token is required for db connection from application
Create `.env` file at `shop` directory with following content
```
FAUNA_ADMIN_SECRET=
FAUNA_SERVER_SECRET=
```
And run script to initialize collection, indexes, roles and seed some data
```
python shop/fauna/init/int.py
```
Current faunaDB python driver doesn't support `CreateFunction` feature, so go to Shell page at your dashboard and run command from file `shop/fauna/functions.py`

Finally, run application
```
python shop/app.py
```

Now you should be able to open SwaggerUI by accesing http://localhost:8888/api/ at your browser

