# Les conditions

```sh
if [[ condition ]]; 
then
	#statements

elif [[ condition ]]; 
then
	#statements
else
	#statements
fi
```

# Les boucles

```sh
for (( i = 0; i < 10; i++ )); do
	#statements
done

# ou encore

for i in words; do
	#statements
done
```


```sh
while [[ condition ]]; do
	#statements
done
```

# Les fonctions

```sh
function_name (){
	#statements
}

function_name $ARGS
```
