Les protections de mémoire modernes 

- DEP (Data Execution Prevention)
- ASLR (Address Space Layout Randomization) 
- Canarie


## CPU Registers

### Registres de données

| **Registre 32 bits** | **Registre 64 bits** | Name        | **Description**                                                                                                                                                                                        |
| -------------------- | -------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `EAX`                | `RAX`                | Accumulator | L'accumulateur est utilisé en entrée/sortie et pour les opérations arithmétiques. (Used in arthmetic operation)                                                                                        |
| `EBX`                | `RBX`                | Base        | La base est utilisée dans l'adressage indexé. (Used as a pointer to data)                                                                                                                              |
| `ECX`                | `RCX`                | Counter     | Le compteur est utilisé pour faire pivoter les instructions et compter les boucles. (Used in shift/rotate instruction and loops)                                                                       |
| `EDX`                | `RDX`                | Data        | Les données sont utilisées pour les E/S et dans les opérations arithmétiques pour les opérations de multiplication et de division impliquant de grandes valeurs. (Used in arthmetic operation and I/O) |

### Registres de pointeurs

| **Registre 32 bits** | **Registre 64 bits** | Name                | **Description**                                                                                                                                                                                                                                                   |
| -------------------- | -------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ESP`                | `RSP`                | Stack Pointer       | Le pointeur de pile pointe vers le haut de la pile. (Pointer to the top of the stack)                                                                                                                                                                             |
| `EBP`                | `RBP`                | Base Pointe         | Le pointeur de base est également connu sous le nom `Stack Base Pointer`de `Frame Pointer`pointeur qui pointe vers la base de la pile. (Pointer to the base of the stack (aka Stack Pointer, or Frame pointer))                                                   |
| `EIP`                | `RIP`                | Instruction Pointer | Le pointeur d'instruction stocke l'adresse de décalage de la prochaine instruction à exécuter. (Controls the program execution by storing a pointer to the address of the next instruction that will be executed: It tells the CPU where the next instruction is) |

### Registres d'indexation

| **Enregistrer 32 bits** | **Enregistrer 64 bits** | Name         | **Description**                                                                                                                                             |
| ----------------------- | ----------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ESI`                   | `RSI`                   | Source Index | L'index source est utilisé comme pointeur à partir d'une source pour les opérations sur les chaînes. (Used as a pointer to source in stream operation)      |
| `EDI`                   | `RDI`                   | Destination  | La destination est utilisée comme pointeur vers une destination pour les opérations sur les chaînes. (Used as a pointer to destination in stream operation) |


## Endianness

Lors des opérations de chargement et de sauvegarde dans les registres et les mémoires, les octets sont lus dans un ordre appelé `endianness`. 

L'endianité se distingue entre les formats `little-endian` et le `big-endian`

Exemple avec les valeurs suivantes :

- Adresse:`0xffff0000`
- Mot:`\xAA\xBB\xCC\xDD`

| **Adresse mémoire** | **0xffff0000** | **0xffff0001** | **0xffff0002** | **0xffff0003** |
| ------------------- | -------------- | -------------- | -------------- | -------------- |
| `big-endian`        | AA             | BB             | CC             | DD             |
| `little-endian`     | DD             | CC             | BB             | AA             |

Ceci est très important pour que nous puissions entrer notre code dans le bon ordre plus tard lorsque nous devrons indiquer au CPU vers quelle adresse il doit pointer.

> L'un des aspects les plus importants d'un débordement de tampon basé sur la pile est de contrôler le `instruction pointer`( `EIP`) afin que nous puissions lui dire à quelle adresse il doit sauter. 
