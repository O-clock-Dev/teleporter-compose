#!/bin/sh

## echo de wg-oclock.conf

CONFIG_FILE="/etc/wireguard/wg-oclock.conf"

touch $CONFIG_FILE

echo "[Interface]" >> $CONFIG_FILE
echo "Address = ${IP_PRIV}/${VPN_WILDCARD}" >> $CONFIG_FILE
echo "ListenPort = ${VPN_LOCAL_PORT}" >> $CONFIG_FILE
echo "PrivateKey = ${KEY_PRIV}" >> $CONFIG_FILE
echo "DNS = 1.1.1.1" >> $CONFIG_FILE
echo "" >> $CONFIG_FILE
echo "[Peer]" >> $CONFIG_FILE
echo "PublicKey = ${KEY_VPN_SERVER}" >> $CONFIG_FILE
echo "AllowedIPs = 10.0.0.0/22" >> $CONFIG_FILE
echo "Endpoint = ${VPN_SERVER}:${VPN_SERVER_PORT}" >> $CONFIG_FILE
echo "PersistentKeepalive = 25" >> $CONFIG_FILE

wg-quick up wg-oclock
#

# sleep 5s
# echo "Activation de l'interface wg0"
# ip link add dev wg0 type wireguard
# sleep 2s
# echo "Activation de l'IP ${IP_PRIV}"
# ip address add dev wg0 ${IP_PRIV}/${VPN_WILDCARD}
# echo "Activation du listen port"
# wg set wg0 listen-port ${VPN_LOCAL_PORT}
# 
# echo "Activation de la clé privée"
# echo ${KEY_PRIV} > privkey
# chmod 600 privkey
# wg set wg0 private-key ./privkey
# echo "Configuration du serveur ${VPN_SERVER}"
# wg set wg0 peer ${KEY_VPN_SERVER} allowed-ips 0.0.0.0/0 endpoint ${VPN_SERVER}:${VPN_SERVER_PORT} persistent-keepalive 25
# echo "On active l'interface"
# sleep 2s
# ip link set up dev wg0

iptables -t nat -I PREROUTING -i wg-oclock -d ${IP_PRIV} -p tcp --dport 80 -j DNAT --to-destination 10.200.0.200
#iptables -t nat -I PREROUTING -d ${IP_PRIV} -p tcp --dport 22 -j DNAT --to-destination 10.200.0.222
# En attendant de faire du routage plus propre
#iptables -t nat -I POSTROUTING -o eth0 -j MASQUERADE


# Pour que les containers puissent joindre les autres membre du VPN et tout particulièrement le proxy sock (pourrait être limité à l'ip source de celui ci).
iptables -t nat -I POSTROUTING -o wg-oclock -j MASQUERADE

# The run the only service of this container : ssh
chmod 600 /root/.ssh/authorized_keys
mkdir -p /run/sshd
ssh-keygen -A
/usr/sbin/sshd -D -e -f /etc/ssh/sshd_config -o PermitRootLogin=yes
