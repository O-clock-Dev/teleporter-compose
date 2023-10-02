# Le téléporteur containerisé

L'idée de ce projet est de fournir un téléporteur iso fonctionnel avec l'actuel qui repose sur une base de virtualisation Docker et donc qui s'appuierai sur Docker Desktop pour s'executer sur les 3 OS : Windows, MacOS, et bien sûr Linux.

## Architecture du projet

Le projet s'appuerait sur un ensemble de containers orchestré par un Docker Compose. Il nous faut distinguer deux types de containers :

- les containers de service : VPN, Proxy, SSH, File explorer, monitoring pour permettre à chaque étudiant de partager son travail, accéder au lan via un proxy, aux formateurs d'accéder aux VM's etc.
- les containers applicatifs : Appache/PHP, MySQL, MongoDB, PostgreSQL, Node, etc. Maintenus par la team système et la team péda

Les containers de services :

- vpn avec un Wireguard et un système d'initialisation de clé publique. Il permettra aussi de rediriger les flux entrants de services (web, bdd, file explorer, ssh, etc).
- ssh pour un accès SSH au filesystem
- file explorer pour accéder avec un clicodrome au filesystem
- monitoring et visualisation des logs web avec goaccess

Les containers applicatifs :

- Caddy
- PHP
- Node
- MySQL
- MongoDB
- PostgreSQL
- Redis
- PhpMyAdmin
- Adminer

### L'initialisation

Le container de service VPN va devoir initialiser l'essentiel du setup. Il doit prendre en argument :

- le nom de promo
- le pseudo github de l'étudiant

Il y aura une API basé sur un serveur Redis qui permettra de :
- gérer les affectation d'IP au VPN
- gérer l'activation d'une clé publique étudiant
- gérer une liste d'étudiant par Promo
- modifier les entrées DNS des étudiants

### Le réseau

L'interconnexion réseau doit permettre de prendre le contrôle et d'accéder aux containers de services étudiants, si possible en le limitant par promotion.

La promotion serait donc un argument de lancement et permettrait après vérification, d'affecter une IP au VPN.

### Le DNS

Une zone tp.lan va être créé, chaque client aura des crédentials pour modifier/ajouter des infos dedans.

## Planning

- Démo fonctionnelle pour le 12 octobre, avec :
   * les containers de services principaux
   * un container applicatif web

## TODO

- [ ] monter un petit serveur Wireguard ARN, chez AWS.
- [ ] build une image docker qui se connecte sur le serveur wireguard
- [ ] rediriger le port entrant 80


