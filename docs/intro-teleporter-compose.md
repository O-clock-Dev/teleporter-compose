---
marp: true
theme: gaia
_class: lead
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
paginate: true

---
### Objectifs pédagogiques
- Pourquoi un nouveau Téléporteur ?
- Présenter l'interface du Téléporteur compose
- Installer Docker Desktop
- Installation du Teleporteur
- Expérience apprenant: demo
- Expérience formateur, projection

---
<!---
footer: "Oclock"
-->
### Pourquoi un nouveau Téléporteur ?

- Virtualbox est un logiciel parfois capricieux qui est gourmand en performance et exclut les Mac.
- Cela engendre aussi énormément de support pour Tommy, comme on peut le constater à chaque fois qu'on le remplace quand il part en congé.
- Le processus de génération du Téléporteur via Ansible et Packer était un pas en avant, mais reste compliqué à maintenir et à mettre à jour, en particulier à cause de la version Cloud en parallèle.

---

### Les solutions

- Docker s'installe facilement (via Docker Desktop) sous tout les OS et fonctionne de la même manière partout.
- On laisse le système hôte gérer la partie graphique et on a besoin de (beaucoup) moins de ressources (2x moins de RAM par exemple et un usage CPU très bas)
- La mise à jour est plus facile. Si on doit changer une version de node, il n'y a qu'une ligne à changer dans le fichier compose.yml.
- Objectif secondaire : Ne plus avoir besoin de VM cloud et économiser entre 3 et 4K€ par mois.

---
### Les compromis
- On perd la solution rapide de visionnage de l'écran ... mais on peut utiliser Rustdesk à la place en cas de besoin, ça tombe bien on a même notre propre serveur.
- Il y a un VScode intégré au Teleporteur compose, mais il est plutôt là pour le formateur car la version Docker ne permet pas d'utiliser liveshare, il faut donc que l'étudiant installe VSC sur son poste.
---
### L'interface apprenant

- Le [dépôt Github](https://github.com/O-clock-Dev/teleporter-compose).
- L'interface apprenant via [http://localhost](http://localhost).
- On utilise notre FS local dans les containers, donc possibilité d'utiliser le vscode de notre poste.
- Pas besoin d'installation locale de node, php, apache ou autre -> le Teleporteur nous les apporte via les containers.
- Une application de terminal permet de visualiser et d'accéder aux autres conteneurs, au cas où une opération doit être faite dessus
---
### Installer Docker Desktop

- Une application multiplaforme à installer.
- Dépendance WSL2 pour Windows.
- Possibilité d'utiliser directement Docker Engine sous Linux.
- Docker cli dispo directement dans le système d'exploitation.


---
### Installation du Teleporteur

- Installer avec `git clone` et `docker compose up --build`.
- Test et visualisation de l'interface http://localhost, debugs éventuels.

---
### Expérience apprenant : demo

- Un petit tour de l'interface Homepage sur localhost et des différents composants
- Les mots de passe des bases de données sont les mêmes que sur le Téléporteur, il y a aussi généralement un accès root:root
- Démonstration de l'explorateur de fichier bien plus stylé que Cloud Commander.
- Un tour dans le terminal et une démonstration de la commande `teleport` avec auto-complétion intégrée.


