FROM alpine
RUN apk add --update --no-cache wireguard-tools openssh tcpdump iproute2-ss vim
RUN mkdir /root/.ssh/
COPY authorized_keys /root/.ssh/authorized_keys
WORKDIR /opt/vpn

# Le but est de le remplacer a terme par un mount bind
COPY . .


ENTRYPOINT ["./entrypoint.sh"]

