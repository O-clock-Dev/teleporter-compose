#!/bin/sh


# Should be removed when issue #9 on vpn-compose will be fixed.
VPN_SERVER_PORT=${VPN_LOCAL_PORT}

sleep 5s
echo "Activation de l'interface wg0"
ip link add dev wg0 type wireguard
sleep 2s
echo "Activation de l'IP ${IP_PRIV}"
ip address add dev wg0 ${IP_PRIV}/${VPN_WILDCARD}
echo "Activation du listen port"
wg set wg0 listen-port ${VPN_LOCAL_PORT}

echo "Activation de la clé privée"
echo ${KEY_PRIV} > privkey
chmod 600 privkey
wg set wg0 private-key ./privkey
echo "Configuration du serveur ${VPN_SERVER}"
wg set wg0 peer ${KEY_VPN_SERVER} allowed-ips 0.0.0.0/0 endpoint ${VPN_SERVER}:${VPN_SERVER_PORT} persistent-keepalive 25
echo "On active l'interface"
sleep 2s
ip link set up dev wg0

iptables -t nat -I PREROUTING -i wg0 -d ${IP_PRIV} -p tcp --dport 80 -j DNAT --to-destination 10.200.0.200
#iptables -t nat -I PREROUTING -d ${IP_PRIV} -p tcp --dport 22 -j DNAT --to-destination 10.200.0.222
# En attendant de faire du routage plus propre
#iptables -t nat -I POSTROUTING -o eth0 -j MASQUERADE


# Pour que les containers puissent joindre les autres membre du VPN et tout particulièrement le proxy sock (pourrait être limité à l'ip source de celui ci).
iptables -t nat -I POSTROUTING -o wg0 -j MASQUERADE

# The run the only service of this container : ssh
chmod 600 /root/.ssh/authorized_keys
mkdir -p /run/sshd
ssh-keygen -A
/usr/sbin/sshd -D -e -f /etc/ssh/sshd_config -o PermitRootLogin=yes
