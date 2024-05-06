FROM ubuntu

RUN set -x \
    && apt update \
    && apt -qq --no-install-recommends install -y iproute2 tcpdump vim iptables wireguard iputils-ping openssh-server netcat-openbsd openssh-server\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/vpn/


# Le but est de le remplacer a terme par un mount bind
COPY entrypoint.sh /opt/vpn/
COPY authorized_keys /root/.ssh/authorized_keys

RUN chmod 600 /root/.ssh/authorized_keys

ENTRYPOINT ["./entrypoint.sh"]

CMD ["sleep","infinity"]
