#!/bin/bash

echo "Activation de l'interface wg0"
ip link add dev wg0 type wireguard
echo "Activation de l'IP ${IP_PRIV}"
ip address add dev wg0 ${IP_PRIV}
echo "Activation du listen port"
wg set wg0 listen-port 51820
echo "Activation de la clé privée"
echo ${KEY_PRIV} > privkey
chmod 600 privkey
wg set wg0 private-key ./privkey
echo "Configuration du serveur ${VPN_SERVER}"
wg set wg0 peer ${KEY_VPN_SERVER} allowed-ips 0.0.0.0/0 endpoint ${VPN_SERVER}:48332 persistent-keepalive 25
echo "On active l'interface"
ip link set up dev wg0

#wg-quick up
sleep infinity
