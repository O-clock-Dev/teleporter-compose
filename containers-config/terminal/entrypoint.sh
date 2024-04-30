#!/bin/bash

# Exit script on any error
set -e

# Setup MySQL credentials
echo "[client]
host=teleporter-mariadb
user=root
password=${MARIADB_ROOT_PASSWORD}" > ~/.my.cnf

# Ensure the .my.cnf file is only accessible by the user
chmod 600 ~/.my.cnf

# Execute the ttyd terminal emulator
exec /usr/bin/ttyd -t fontSize=16 -t titleFixed='Terminal' -W bash
