Masquer secret.zip dans laptop.jpg

```sh
steghide embed -cf laptop.jpg -ef secret.zip
steghide embed -cf laptop.jpg -ef secret.zip -sf laptop2.jpg
```

Extraire le fichier secret.zip de laptop2.jpg

```sh
steghide extract -sf laptop2.jpg
```
