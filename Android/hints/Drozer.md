**Aide-mémoire de base de Drozer**

Exploitation du fournisseur de contenu

```c
run app.provider.info -a package_name

run scanner.provider.finduris -a package_name

run app.provider.query uri

run app.provider.update uri --selection conditions selection_arg column data

run scanner.provider.sqltables -a package_name

run scanner.provider.injection -a package_name

run scanner.provider.traversal -a package_name
```

Exploitation des services

```c
run app.service.info -a package_name

run app.service.start --action action --component package_name component_name

run app.service.send package_name component_name --msg what arg1 arg2 --extra type key value --bundle-as-obj
```

