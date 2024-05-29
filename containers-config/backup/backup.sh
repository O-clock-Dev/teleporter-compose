#!/bin/bash

# Check if docker.io is present
if ! dpkg -s docker.io &> /dev/null
then
    apt update
    DEBIAN_FRONTEND=noninteractive apt install docker.io -y
fi

echo "# MySQL backup"
bash /scripts/backup-mysql.sh

echo "# PGSQL backup"
bash /scripts/backup-pgsql.sh

echo "# MongoDB backup"
bash /scripts/backup-mongodb.sh

echo "# Sleeping for 4 hours.. zzzZzZzZzz.."
sleep 14400
