import os
import requests
import json
from jinja2 import Template
from logs_config import (
    configure_logs,
)  # Assurez-vous que votre configuration de logs est correcte
import time
# Configuration des variables d'environnement par défaut
PROMO = os.getenv("PROMO", "hati")
CLIENT_NAME = os.getenv("VPN_NAME", "aurelien-bras")
IP_PRIV = os.getenv("VPN_IP_PRIV", "10.0.2.183")

# Création du logger
logger = configure_logs()

# Chemin absolu du fichier de configuration HAProxy
ha_proxy_config_file_relatif_path = "./configs/haproxy/haproxy.cfg"
path = os.path.dirname(os.path.abspath(__file__))
ha_proxy_config = os.path.join(path, ha_proxy_config_file_relatif_path)


def get_vpn_clients():
    """
    Récupérer la liste des clients VPN depuis l'API
    """
    url = f"http://vpn.eddi.cloud/promo_list/{PROMO}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a échoué
        logger.info(f"Requête envoyée à {url}")
        dict_clients = json.loads(response.json())
        logger.debug(f"Réponse reçue : {dict_clients}")
        del dict_clients[CLIENT_NAME]  # Supprimer le client actuel
        logger.debug(f"Clients VPN récupérés : {dict_clients}")
        return dict_clients
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des clients VPN : {e}")
        return None


# Charger le modèle Jinja depuis le fichier
try:
    with open("./configs/haproxy/haproxy_template.j2") as file:
        template = Template(file.read())
        logger.info("Modèle Jinja chargé avec succès.")
except FileNotFoundError:
    logger.error("Le fichier haproxy_template.cfg n'existe pas.")
    exit(1)
except Exception as e:
    logger.error(f"Erreur lors de la lecture du fichier de modèle : {e}")
    exit(1)

# Récupérer les clients VPN
clients = get_vpn_clients()
if clients is None:
    logger.error("Impossible de récupérer les clients VPN. Arrêt du script.")
    exit(1)

# Convertir le dictionnaire en une liste de tuples (name, ip)
clients_list = list(clients.items())
logger.debug(f"Clients VPN : {clients_list}")

# Rendre le modèle Jinja avec les valeurs spécifiées
haproxy_config = template.render(clients=clients_list)
logger.debug(f"Configuration HAProxy générée : {haproxy_config}")

# Écrire la configuration HAProxy générée dans un fichier
try:
    with open(ha_proxy_config_file_relatif_path, "w") as file:
        file.write(haproxy_config)
    logger.info("Configuration HAProxy générée avec succès.")
    time.sleep(120)
    exit(0)
except Exception as e:
    logger.error(f"Erreur lors de l'écriture du fichier de configuration HAProxy : {e}")
    time.sleep(120)
    exit(1)
    
    