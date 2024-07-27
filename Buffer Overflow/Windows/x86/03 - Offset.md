> Offset: C'est chercher a quel moment nous pouvons casser correctement le programmme

> C'est chercher ou exactement nous ecrasons l'EIP

on utilise le nombre trouver lors du fuzzing
`msf-pattern_create l {3000}`

Ce qui vas genere des caracteres aleatoire que l'on vas utiliser dans le fichier (`offset.py`)

On execute puis on recuprer l'adresse EIP pour retrouver l'offset
`msf-pattern_offset -l {3000} -q {386F4337}`

Cela nous retourne un offset qui vas nous permettre de controller l'EIP