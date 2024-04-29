FROM alpine
RUN apk add --update --no-cache wireguard-tools openssh tcpdump iproute2-ss vim iptables
RUN mkdir /root/.ssh/
COPY authorized_keys /root/.ssh/authorized_keys
WORKDIR /opt/vpn
COPY entrypoint.sh /opt/vpn/entrypoint.sh
RUN chmod +x /opt/vpn/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

