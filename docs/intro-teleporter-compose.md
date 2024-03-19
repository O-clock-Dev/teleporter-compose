---
marp: true
theme: gaia
_class: lead
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
paginate: true

---
### Objectifs pédagogiques

- Présenter l'interface du teleporteur compose
- Installer Docker Desktop
- Installation du Teleporteur
- Expérience apprenant, demo
- Expérience formateur, projection

---
<!---
footer: "Oclock"
-->
### L'interface apprenant

- Le [dépôt Github](https://github.com/O-clock-Dev/teleporter-compose).
- L'interface apprenant via [http://localhost](http://localhost).
- On utilise notre FS local dans les containers, donc possibilité d'utiliser le vscode de notre poste.
- Pas besoin d'installation locale de node, php, apache ou autre -> le Teleporteur nous les apporte via les containers.

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


