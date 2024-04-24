FROM haproxy:lts-alpine

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY templates/503.html /usr/local/etc/haproxy/errors/503.html

USER root
