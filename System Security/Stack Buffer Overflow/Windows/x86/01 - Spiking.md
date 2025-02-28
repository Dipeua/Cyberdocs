> Spiking: Ce sont des methodes utiliser pour rechercher un type de vulnerabiliter dans nos programmes ou une partie vulnerable d'un programme. 

NB: Le serveur vulnerable est en marche et Immunity aussi

* Toute les commandes sont des point d'entrer du BOF on les teste un a un et voir quel se casse.

* Focus sur la commande TRUN.

```sh
└─$ nc -nv 192.168.1.130  9999
(UNKNOWN) [192.168.1.130] 9999 (?) open
Welcome to Vulnerable Server! Enter HELP for help.
HELP
Valid Commands:
HELP
STATS [stat_value]
RTIME [rtime_value]
LTIME [ltime_value]
SRUN [srun_value]
TRUN [trun_value]
GMON [gmon_value]
GDOG [gdog_value]
KSTET [kstet_value]
GTER [gter_value]
HTER [hter_value]
LTER [lter_value]
KSTAN [lstan_value]
EXIT
```

Execution: 

regarder les fihiers .spk

```sh
generic_send_tcp host port file.spk 0 0
```

si le programme plante, c'est une preuve d'une vulnerabiliter