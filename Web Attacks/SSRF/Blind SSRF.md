Pour détecter les vulnérabilités SSRF aveugles il faut utiliser des techniques hors bande OAST qui déclenche une requête HTTP vers un système externe que vous contrôlez et de surveiller les interactions réseau avec ce système.

Un outil de journalisation HTTP externe pour surveiller les requêtes telles que 
- https://requestbin.com/r/
- Burp Collaborator

> Si une requête HTTP entrante est observée en provenance de l'application, elle est alors vulnérable au SSRF mais ne constitue pas en soi une voie d'exploitation

Mais peut toujours être exploité pour rechercher d'autres vulnérabilités sur le serveur lui-même ou sur d'autres systèmes back-end.

- Vous pouvez balayer aveuglément l'espace d'adresses IP interne `192.168.x.x`  en envoyant des charges utiles conçues pour détecter des vulnérabilités bien connues.

> Une autre façon d'exploiter les vulnérabilités SSRF aveugles consiste à inciter l'application à se connecter à un système sous le contrôle de l'attaquant et à renvoyer des réponses malveillantes au client HTTP qui établit la connexion.

