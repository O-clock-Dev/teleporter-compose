#!/bin/bash

echo "# MySQL backup"
bash /scripts/backup-mysql.sh

echo "# PGSQL backup"
bash /scripts/backup-pgsql.sh

echo "# MongoDB backup"
bash /scripts/backup-mongodb.sh

echo "# Sleeping for 4 hours.. zzzZzZzZzz.."
sleep 14400