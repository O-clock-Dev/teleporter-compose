# Teleporte Compose Documentation

> [!NOTE]  
> 🇬🇧 [Documentation available in english](README.md)

Bienvenue dans la documentation de **Teleporte Compose**. Vous trouverez ici toutes les informations dont vous avez besoin pour comprendre, installer et utiliser ce projet.

> [!IMPORTANT]  
> Notre documentation est un travail en cours. Soyez patient ou n'hésitez pas à [contribuer](#contribuer).

## Table des matières

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Utilisation](#utilisation)
4. [Contribuer](#contribuer)
5. [Licence](#licence)

## Introduction

Ce projet vise à offrir une [Internal Developer Platform](https://internaldeveloperplatform.org/what-is-an-internal-developer-platform/) à des fins éducatives, mais il peut également être adapté à d'autres usages.

## Installation

Pour installer ce projet, veuillez vous référer au [README](../README.md) racine.

## Utilisation

### Utilisation des DevContainers avec VSCode

Pour utiliser les DevContainers avec VSCode, vous devez d'abord installer l'extension "[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)" ou le pack d'extensions "[Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)". Ces extensions vous permettent de travailler avec des conteneurs, des machines virtuelles ou des environnements distants directement depuis VSCode.

Voici deux cas d'utilisation courants des DevContainers avec VSCode :

1. **Attacher VSCode à un conteneur en cours d'exécution**
2. **Utiliser un DevContainer défini dans un dépôt Git**

> [!TIP] 
> Les DevContainers combinés à VSCode offrent un moyen puissant de normaliser les environnements de développement au sein d'une équipe, tout en conservant les avantages du travail avec un IDE local complet.
> N'hésitez pas à explorer les différentes options de configuration des DevContainers pour les adapter à vos besoins spécifiques. La documentation officielle de VSCode est une excellente ressource pour aller plus loin.

#### Attacher VSCode à un conteneur en cours d'exécution

Pour attacher un DevContainer à un conteneur en cours d'exécution, suivez ces étapes :

1. Assurez-vous d'avoir installé l'extension "Dev Containers" ou le pack d'extensions "Remote Development Extension Pack" dans votre VS Code.
2. Ouvrez la palette de commandes dans VS Code (Ctrl+Shift+P ou Cmd+Shift+P sur macOS).
3. Tapez "Remote-Containers: Attach to Running Container" et sélectionnez-le dans la liste.
4. VS Code affichera une liste des conteneurs en cours d'exécution. Choisissez le conteneur auquel vous souhaitez vous attacher.
5. Après avoir sélectionné le conteneur, VS Code se rechargera et s'attachera au conteneur en cours d'exécution.
6. Vous pouvez maintenant interagir avec le conteneur via l'interface de VS Code, modifier des fichiers, exécuter des commandes et déboguer votre application comme si elle s'exécutait localement.

> [!TIP]
> En attachant un DevContainer à un conteneur en cours d'exécution, vous pouvez tirer parti de l'environnement isolé et des dépendances spécifiques du conteneur tout en utilisant votre IDE préféré. Cette approche est particulièrement utile lorsque vous travaillez avec des conteneurs existants ou lorsque vous devez déboguer rapidement un problème dans un environnement conteneurisé.

##### Vidéo pratique : Attacher à un conteneur en cours d'exécution

Vous pouvez facilement attacher VSCode à un conteneur Docker déjà en cours d'exécution sur votre machine. Cela vous permet de développer dans l'environnement isolé du conteneur.

Pour voir comment procéder en détail, regardez cette vidéo :

![Attacher VSCode à un conteneur en cours d'exécution](https://github.com/O-clock-Dev/teleporter-compose/assets/126659374/71df8064-6cfa-414d-8e4d-ceac2b90fed3)

#### Utiliser un DevContainer défini dans un dépôt Git

Si vous avez un répertoire de projet qui inclut un fichier `devcontainer.json`, vous pouvez facilement l'ouvrir dans un DevContainer en utilisant VS Code. Le fichier `devcontainer.json` définit la configuration de l'environnement de développement, y compris l'image de base, les paramètres de VS Code, les extensions, etc. Pour ouvrir le répertoire dans un DevContainer, suivez ces étapes :

1. Assurez-vous d'avoir installé l'extension "Dev Containers" ou le pack d'extensions "Remote Development Extension Pack" dans votre VS Code.
2. Ouvrez le répertoire du projet dans VS Code soit en utilisant le menu "File > Open Folder", soit en exécutant la commande `code /chemin/vers/votre/projet` dans votre terminal.
3. Une fois le répertoire ouvert dans VS Code, vous devriez voir une notification dans le coin inférieur droit indiquant qu'un fichier de configuration DevContainer a été détecté.
4. Cliquez sur le bouton "Reopen in Container" dans la notification ou ouvrez la palette de commandes (Ctrl+Shift+P ou Cmd+Shift+P sur macOS) et sélectionnez "Remote-Containers: Reopen in Container".
5. VS Code construira le DevContainer en fonction de la configuration du fichier `devcontainer.json` et rouvrira le répertoire à l'intérieur du conteneur.
6. Une fois le processus de construction terminé, vous pouvez commencer à développer dans l'environnement DevContainer. Toutes les extensions spécifiées dans la configuration seront automatiquement installées et les paramètres seront appliqués.

> [!TIP]
> En utilisant un fichier `devcontainer.json`, vous pouvez vous assurer que tous ceux qui travaillent sur le projet ont le même environnement de développement, quelle que soit leur configuration locale. Cette approche permet de minimiser les problèmes liés à l'environnement et facilite la contribution rapide des nouveaux membres de l'équipe au projet.

##### Vidéo pratique : Utiliser une configuration DevContainer

De nombreux projets incluent une configuration DevContainer directement dans leur dépôt Git (comme dans l'exemple du dossier `code/node/test-app/`). Cela permet à tous les développeurs de travailler dans un environnement normalisé.

Pour apprendre à utiliser une telle configuration, suivez le tutoriel dans cette vidéo :

![Utiliser une préconfiguration devcontainer.json](https://github.com/O-clock-Dev/teleporter-compose/assets/126659374/3741a5b7-878c-4b90-888e-8dfd4b42342e)

#### Qu'est-ce que les DevContainers ?

La [spécification DevContainers](https://containers.dev/) est un standard ouvert qui permet de définir et de partager de manière cohérente des environnements de développement entre différents outils et plateformes. En tirant parti de cette spécification, vous pouvez vous assurer que tous les développeurs d'un projet ont accès à la même configuration, quel que soit leur environnement local. La spécification prend en charge un large éventail de fonctionnalités, telles que la spécification de l'image de base, la configuration des paramètres de VS Code, l'installation d'extensions, etc. L'adoption de la spécification DevContainers peut grandement simplifier le processus d'intégration des nouveaux membres de l'équipe et réduire le temps passé sur les problèmes liés à l'environnement.

## Contribuer

Les contributions sont les bienvenues ! Veuillez lire les [directives de contribution](../CONTRIBUTING.md) pour plus de détails.

## Licence

Ce projet est sous licence AGPLv3. Voir le fichier [LICENSE](../LICENSE) pour plus de détails.
