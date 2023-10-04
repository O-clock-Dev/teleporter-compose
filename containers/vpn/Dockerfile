FROM ubuntu

RUN apt update && apt install -y iproute2 tcpdump vim iptables wireguard iputils-ping && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/vpn/


# Le but est de le remplacer a terme par un mount bind
COPY entrypoint.sh /opt/vpn/



ENTRYPOINT ["./entrypoint.sh"]

CMD ["sleep","inifinity"]


