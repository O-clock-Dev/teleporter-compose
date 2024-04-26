FROM ubuntu

RUN set -x \
    && apt update \
    && apt install -y iproute2 tcpdump vim iptables wireguard iputils-ping openssh-server netcat-openbsd \
    && apt install -y ca-certificates curl gnupg \
    && install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    && chmod a+r /etc/apt/keyrings/docker.gpg \
    && echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt update \
    && apt -y install docker-ce-cli \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/vpn

# Le but est de le remplacer a terme par un mount bind
COPY containers-config/vpn/ .


ENTRYPOINT ["./entrypoint.sh"]

CMD ["sleep","infinity"]