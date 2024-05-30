#!/bin/sh

echo "# MySQL backup"
sh /scripts/backup-mysql.sh

echo "# PGSQL backup"
sh /scripts/backup-pgsql.sh

echo "# MongoDB backup"
sh /scripts/backup-mongodb.sh

echo "# Sleeping for 4 hours.. zzzZzZzZzz.."
sleep 14400