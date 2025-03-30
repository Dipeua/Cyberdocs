# Buffer Overflows Walkthrough - CyberMentor

- Anatomy of Memory:
	
	Struct de la memoire

		> Kernel: encore appeler "TOP" ==> 11111
		> Stack
		> Heap
		> Data
		> Text: encore appeler "BOTTOM" ==> 00000


- Anatomy of Stack
	
	Structure d'une pile
	
		> ESP(Extended Stack Pointer): encore appeler "TOP"
		> Buffer Space
		> EBP (Extended Base Pointer): encore appeler "BOTTOM"
		> EIP (Extended Instruction Pointer) / Return Address / Adresse de retour

	Explication :
		
		Le BUFFER SPACE s'execute du haut vers le bas.
		Le but du BOF c'est de remplire le BUFFER SPACE avec des caracteres aleatoire ('A') et le EBP, EIP.
		Pour avoir une Attaque BOF on doit emplire le BUFFER SPACE utiliser et ecrire sur le EBP et arriver jusqu'au EIP qui est un pointeur d'address (Instruction suivante | addresse de retour). Ce que l'on peut faire c'est utiliser cette address pour pointer vers une direction que l'on veut. et cette direction peut etre un code malveillant contenant un reverse-shell.


- Buffer Overflows Walkthrough
	
	Etapes pour conduire un depassement tampon
	
		> Spiking
		> Fuzzing
		> Finding the Offset
		> Overwriting the EIP
		> Finding Bad Characters
		> Finding the Right Module
		> Generating Shellcode
		> Root!

	Explication
		
		> Utiliser pour trouver une partie vulnerable d'un programme
		> Une fois la vulnerabiliter trouver, on peut le FUZZER utiliser pour CASSER le programme
		> Si on le casse, on cherche a quel moment nous pouvons le casser correctement (OFFSET)
		> Et on utilise se OFFSET pour ecrasser l'EIP adresse le pointeur de retour
		> Une fois que nous controlons l'EIP, nous devons faire quelques taches de nettoyage:
			- trouver le mauvais caracteres (BAD CARAC)
			- trouver les bons modules (RIGHT MOD)
		> Une fois le mauvais caracteres et le modules sont trouver, nous pouvons generer notre reverse-shell en pointent EIP vers un shellcode malveillant.

Tools to be USED

	>  Kali Linux
	>  Windows 10
	>  Vulnserver (run on port 9999 by default)
	>  Immunity Debugger
