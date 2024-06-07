import os
import docker
import requests
from jinja2 import Template
from logs_config import (
    configure_logs,
)  # Assurez-vous que votre configuration de logs est correcte

# Configuration des variables d'environnement par défaut
PROMO = os.getenv("PROMO", "hati")
CLIENT_NAME = os.getenv("VPN_NAME", "aurelien-bras")

# Création du logger
logger = configure_logs()

# Chemin absolu du fichier de configuration HAProxy
template_haproxy_path = "config/haproxy/haproxy_template.j2"
ha_proxy_config = "config/haproxy/haproxy.cfg"
bookmark_template_path = "config/homepage/bookmarks_template.j2"
bookmark_list_path = "config/homepage/bookmarks.yaml"


def get_vpn_clients():
    """
    Récupérer la liste des clients VPN depuis l'API
    """
    url = f"http://vpn.eddi.cloud/promo_list/{PROMO}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a échoué
        logger.info(f"Requête envoyée à {url}")
        dict_clients = response.json()
        logger.debug(f"Réponse reçue : {dict_clients}")
        return dict_clients
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des clients VPN : {e}")
        return None


def create_haproxy_config(clients):
    """Charger le modèle Jinja depuis le fichier haproxy_template.j2 et générer la configuration HAProxy"""

    try:
        with open(template_haproxy_path) as file:
            template = Template(file.read())
            logger.info("Modèle Jinja haproxy chargé avec succès.")
    except FileNotFoundError:
        logger.error("Le fichier haproxy_template.j2 n'existe pas.")
        exit(1)
    except Exception as e:
        logger.error(f"Erreur lors de la lecture du fichier de modèle : {e}")
        exit(1)

    # Convertir le dictionnaire en une liste de tuples (name, ip) et supprimer le client actuel
    clients.pop(CLIENT_NAME, None)
    clients_list = list(clients.items())

    logger.debug(f"Clients pour inserer sur le template haproxy : {clients_list}")

    # Rendre le modèle Jinja avec les valeurs spécifiées
    haproxy_config = template.render(clients=clients_list)
    logger.debug("Configuration HAProxy générée avec succès")

    # Écrire la configuration HAProxy générée dans un fichier
    try:
        with open(ha_proxy_config, "w") as file:
            file.write(haproxy_config)
        logger.info("Configuration HAProxy générée avec succès.")

    except Exception as e:
        logger.error(
            f"Erreur lors de l'écriture du fichier de configuration HAProxy : {e}"
        )
        exit(1)
    # restart the Haproxy container
    try:
        d_cli = docker.from_env()
        ct = d_cli.containers.get("teleporter-haproxy")
        ct.restart()
    except Exception as e:
        logger.error(f"Erreur lors du reload haproxy : {e}")
        exit(1)


def prepare_clients_list_to_bookmarks(clients):
    """Préparer la liste des clients VPN pour la page d'accueil"""
    # on ne prends que les clefs des clients
    clients_list_url = clients.keys()
    # replace les tirets par des espaces et on met en majuscule
    clients_list = [client.replace("-", " ").title() for client in clients_list_url]
    # on construit la liste des clients avec les keys clients list et valeurs les clients list url
    clients_list = list(zip(clients_list, clients_list_url))

    logger.debug(f"Clients VPN : {clients_list}")
    return clients_list


def create_homepage_bookmarks_list(clients):
    """Charger le modèle Jinja depuis le fichier bookmarks_template.j2 et générer la liste de bookmarks"""
    clients_list = prepare_clients_list_to_bookmarks(clients)
    try:
        with open(bookmark_template_path) as file:
            template = Template(file.read())
            logger.info("Modèle Jinja bookmarks chargé avec succès.")
    except FileNotFoundError:
        logger.error("Le fichier bookmarks_template.j2 n'existe pas.")
        exit(1)
    except Exception as e:
        logger.error(f"Erreur lors de la lecture du fichier de modèle : {e}")
        exit(1)
    # On rend le modèle Jinja avec les valeurs spécifiées
    ctx = {"clients": clients_list, "promo": PROMO}
    bookmarks_list = template.render(ctx)
    logger.debug("Liste de bookmarks générée avec succès")
    # Écrire la liste de bookmarks générée dans un fichier
    try:
        with open(bookmark_list_path, "w") as file:
            file.write(bookmarks_list)
        logger.info("Liste de bookmarks générée avec succès.")

    except Exception as e:
        logger.error(
            f"Erreur lors de l'écriture du fichier de liste de bookmarks : {e}"
        )
        exit(1)


if __name__ == "__main__":
    if clients := get_vpn_clients():
        create_haproxy_config(clients)
        create_homepage_bookmarks_list(clients)
        exit(0)
    else:
        logger.error("Impossible de générer la configuration HAProxy.")
        exit(1)
