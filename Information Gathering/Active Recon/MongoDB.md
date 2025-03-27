# MongoDB

Le service tourne sur la machine sur le port 27117, 27017

Connecting to MongoDB : Interact with a MongoDB database

```sh
mongosh mongodb://127.0.0.1:27017
```

Check which databases exist

```sh
show databases
```

**Creating a Database**

> MongoDB does not create a database until you first store data in that database. We can "switch" to a new database called `academy` by using the use command:

```sh
use academy
```

List all collections in a database

```sh
show collections
```

**Inserting Data**

> Similarly to creating a database, MongoDB only creates a collection when you first insert a document into that collection. We can insert data into a collection in several ways `single` and `multiple`

Insert a single document into the apples collection

```sh
academy> db.apples.insertOne({type: "Granny Smith", price: 0.65})
{
  acknowledged: true,
  insertedId: ObjectId("63651456d18bf6c01b8eeae9")
}
```

Insert multiple documents into the apples collection

```sh
academy> db.apples.insertMany([{type: "Golden Delicious", price: 0.79}, {type: "Pink Lady", price: 0.90}])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId("6365147cd18bf6c01b8eeaea"),
    '1': ObjectId("6365147cd18bf6c01b8eeaeb")
  }
}
```

**Selecting Data**

> Let's say we wanted to check the price of Granny Smith apples. One way to do this is by specifying a document with fields and values we want to match:

```sh
academy> db.apples.find({type: "Granny Smith"})
{
  _id: ObjectId("63651456d18bf6c01b8eeae9"),
  type: 'Granny Smith',
  price: 0.65
}
```

Or perhaps we wanted to list all documents in the collection. We can do this by passing an empty document

```sh
academy> db.apples.find({})
[
  {
    _id: ObjectId("63651456d18bf6c01b8eeae9"),
    type: 'Granny Smith',
    price: 0.65
  },
  {
    _id: ObjectId("6365147cd18bf6c01b8eeaea"),
    type: 'Golden Delicious',
    price: 0.79
  },
  {
    _id: ObjectId("6365147cd18bf6c01b8eeaeb"),
    type: 'Pink Lady',
    price: 0.90
  }
]
```

**Advanced queries, with query operators in MongoDB** 

- `$eq` 	Matches values which are equal to a specified value 	`type: {$eq: "Pink Lady"}`

- `$gt` 	Matches values which are greater than a specified value 	`price: {$gt: 0.30}`

- `$gt`e 	Matches values which are greater than or equal to a specified value 	`price: {$gte: 0.50}`

- `$in` 	Matches values which exist in the specified array 	`type: {$in: ["Granny Smith", "Pink Lady"]}`

- `$lt` 	Matches values which are less than a specified value 	`price: {$lt: 0.60}`

- `$lte` 	Matches values which are less than or equal to a specified value 	`price: {$lte: 0.75}`

- `$nin` 	Matches values which are not in the specified array 	`type: {$nin: ["Golden Delicious", "Granny Smith"]}`  	

- `$and` 	Matches documents which meet the conditions of both specified queries 	`$and: [{type: 'Granny Smith'}, {price: 0.65}]` 

- `$not` 	Matches documents which do not meet the conditions of a specified query 	`type: {$not: {$eq: "Granny Smith"}}` 	

- `$nor` 	Matches documents which do not meet the conditions of any of the specified queries 	`$nor: [{type: 'Granny Smith'}, {price: 0.79}]`  	

- `$or` 	Matches documents which meet the conditions of one of the specified queries 	`$or: [{type: 'Granny Smith'}, {price: 0.79}]` 

- `$mod` 	Matches values which divided by a specific divisor have the specified remainder 	`price: {$mod: [4, 0]}` 	

- `$regex` 	Matches values which match a specified RegEx 	`type: {$regex: /^G.*/}` 	

- `$where` 	Matches documents which satisfy a JavaScript expression 	`$where: 'this.type.length === 9'`

**Removing Documents**

Removing a document is very similar to selecting documents.

```sh
academy> db.apples.remove({price: {$lt: 0.8}})
{ acknowledged: true, deletedCount: 2 }
```

---

Interragir avec MongoDB

```sh
mongo --port 27117 [DATABASE] --eval "db.admin.find().forEach(printjson);"
```

Let's proceed to replacing the existing hash with the one we created.

```sh
mkpasswd -m sha-512 Password1234
```

```sh
mongo --port 27117 [DATABASE] --eval 'db.admin.update({"_id":
ObjectId("61ce278f46e0fb0012d47ee4")},{$set:{"x_shadow":"SHA_512_HASH_GENERATED"}})'
```


