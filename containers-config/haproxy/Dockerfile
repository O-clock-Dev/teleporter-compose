FROM haproxy:lts-alpine

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY templates/503-custom.http /usr/local/etc/haproxy/errors/503-custom.http

USER root
