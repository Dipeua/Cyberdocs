La possibilité de relayer des identifiants peut être donnée à une machine ou un utilisateur de service, s'il possède au moins un attibut SPN.

Il existe trois manières d’autoriser une machine ou un compte de service de prendre la place d’un utilisateur pour communiquer avec un ou plusieurs autre(s) service(s) :

[Unconstrained Delegation](../Attacking%20Kerberos/Unconstrained%20Delegation.md)

- Délégation sans contrainte
Le serveur ou le compte de service qui se voit attribuer le droit `Unconstrained Delegation` est en mesure de se faire passer pour un utilisateur pour communiquer avec n’importe quel service sur n’importe quelle machine.

**Kerberos Constrained Delegation**
- Délégation contrainte
Si une machine ou un compte de service possède le flag `Constrained Delegation`, alors une liste de services autorisés sera associée à ce droit.

**Resource Based Kerberos Constrained Delegation - RBCD**
- Délégation contrainte basée sur les ressources
Dans la `Constrained Delegation`, c’est au niveau du serveur qui délègue qu’on indique la liste des SPN autorisés, dans le cas du `RBCD`, c’est au niveau des services finaux qu’on indique la liste des services qui peuvent communiquer avec eux via délégation.

---
Comment est-ce qu’une machine ou un compte peut se faire passer pour un utilisateur auprès d’une ressource ?

