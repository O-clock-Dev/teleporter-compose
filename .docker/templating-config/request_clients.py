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
services_template_path = "config/homepage/services_template.j2"
services_file_path = "config/homepage/services.yaml"


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

def create_services_config(clients):
    """Generate homepage/services.yml from template"""

    try:
        with open(services_template_path) as file:
            template = Template(file.read())
            logger.info("Modèle Jinja de services chargé avec succès.")
    except FileNotFoundError:
        logger.error(f"Le fichier ${template_services_path} n'existe pas.")
        exit(1)
    except Exception as e:
        logger.error(f"Erreur lors de la lecture du fichier de modèle : {e}")
        exit(1)

    # Convertir le dictionnaire en une liste de tuples (name, ip) et supprimer le client actuel
    clients.pop(CLIENT_NAME, None)
    clients_list = list(clients.items())

    logger.debug(f"Clients pour inserer sur le template de service homepage : {clients_list}")

    # Rendre le modèle Jinja avec les valeurs spécifiées
    services_rendered = template.render(clients=clients_list)
    logger.debug("Configuration de service Homepage générée avec succès")

    # Écrire la configuration de service homepage générée dans un fichier
    try:
        with open(services_file_path, "w") as file:
            file.write(services_rendered)
        logger.info("Configuration de services homepage générée avec succès.")

    except Exception as e:
        logger.error(
            f"Erreur lors de l'écriture du fichier de service homepage : {e}"
        )
        exit(1)

if __name__ == "__main__":
    if clients := get_vpn_clients():
        create_haproxy_config(clients)
        create_services_config(clients)
        exit(0)
    else:
        logger.error("Impossible de générer les configurations.")
        exit(1)
