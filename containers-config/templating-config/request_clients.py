# module to make requests to the VPN api

import os
import requests
from jinja2 import Template
from logs_config import configure_logs

PROMO = os.getenv("PROMO", "hati")

logger = configure_logs()  # Create logger

logger.info(f"Using promo: {PROMO}")


############# Chemin du fichier de configuration HAProxy #############
ha_proxy_config_file_relatif_path = "../containers-config/haproxy/haproxy.cfg"
path = os.path.dirname(os.path.abspath(__file__))

ha_proxy_config = os.path.join(
    os.path.dirname(__file__), ha_proxy_config_file_relatif_path
)

######################################################################


##############Chemin vpn.env #########################################
# Chemin relatif du fichier vpn.env par rapport au répertoire du script Python
chemin_relatif_vpn_env = "vpn.env"

# Chemin absolu jusqu'au répertoire du script
repertoire_script = os.path.dirname(os.path.abspath(__file__))

# Chemin absolu du fichier vpn.env
chemin_absolu_vpn_env = os.path.join(repertoire_script, chemin_relatif_vpn_env)

# Ouvrir et lire le contenu du fichier vpn.env
with open(chemin_absolu_vpn_env, "r") as f:
    contenu_vpn_env = f.read()

# Faire quelque chose avec le contenu du fichier vpn.env
# Par exemple, imprimer son contenu
print("Contenu du fichier vpn.env :")
print(contenu_vpn_env)
######################################################################


def get_vpn_clients():
    url = f"http://vpn.eddi.cloud/promo_list/{PROMO}"
    response = requests.get(url)
    logger.info(f"Requesting clients from {url}")
    logger.info(f"Response: {response.json()}")
    print(response.json())
    return response.json()


# Charger le modèle Jinja depuis le fichier
with open("haproxy_template.cfg") as file:
    template = Template(file.read())

# Récupérer les clients VPN
clients = get_vpn_clients()

context = {"clients": clients}


# Rendre le modèle Jinja avec les valeurs spécifiées
haproxy_config = template.render(context)

with open(ha_proxy_config_file_relatif_path, "w") as file:
    file.write(haproxy_config)

if __name__ == "__main__":
    get_vpn_clients()
