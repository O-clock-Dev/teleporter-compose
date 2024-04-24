FROM haproxy:lts-alpine

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY templates/503.http /usr/local/etc/haproxy/errors/503.http

USER root
