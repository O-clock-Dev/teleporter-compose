#!/usr/bin/env bash

eval $(grep -v '^#' vpn.env | sed -e 's/^/export /' -e "s/='/='/" -e "s/=\(.*\)/='\1'/")

docker compose down
docker compose up --build -d
