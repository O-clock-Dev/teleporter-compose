# module to make requests to the VPN api

import os
import requests
from jinja2 import Template
from logs_config import configure_logs

PROMO = os.getenv("PROMO", "hati")
CLIENT_NAME = os.getenv("VPN_NAME", "nuno-marcelino")
IP_PRIV = os.getenv("VPN_IP_PRIV", "10.0.2.183")

logger = configure_logs()  # Create logger

logger.info(f"Using promo: {PROMO}")


############# Chemin du fichier de configuration HAProxy #############
ha_proxy_config_file_relatif_path = "haproxy.cfg"
path = os.path.dirname(os.path.abspath(__file__))

ha_proxy_config = os.path.join(
    os.path.dirname(__file__), ha_proxy_config_file_relatif_path
)

######################################################################


def get_vpn_clients():
    """
    Send a request to the VPN API to get the list of clients and their IP addresses
    delete the name of the client that is making the request
    """
    url = f"http://vpn.eddi.cloud/promo_list/{PROMO}"
    response = requests.get(url)
    logger.info(f"Requesting clients from {url}")
    logger.info(f"Response: {response.json()}")
    dict_clients = response.json()
    del dict_clients[CLIENT_NAME]
    return dict_clients


# Charger le modèle Jinja depuis le fichier
with open("haproxy_template.cfg") as file:
    template = Template(file.read())

# Récupérer les clients VPN
clients = get_vpn_clients()
# Convertir le dictionnaire en une liste de tuples (name, ip)
clients = clients.items()


# Rendre le modèle Jinja avec les valeurs spécifiées
haproxy_config = template.render(clients)

with open(ha_proxy_config_file_relatif_path, "w") as file:
    file.write(haproxy_config)
