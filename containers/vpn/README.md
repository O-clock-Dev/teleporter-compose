# VPN image

## run client

`docker run -d --name=vpn --cap-add=NET_ADMIN -e VPN_SERVER=profy12-server.eddi.cloud -e IP_PRIV=10.0.0.2/24 -e KEY_VPN_SERVER=jV5CfW+4x5EAlPCPewmPXTmWP9Qjc91e59cdLr9csS8= -e KEY_PRIV=YAxh/JVTqIJi0LnW6rNzRpAi62rvh8ZG9j/h0nx7YGw= -p 51820:51820/udp --restart unless-stopped monwg`


