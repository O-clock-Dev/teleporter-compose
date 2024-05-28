#!/bin/bash

# Variables
HOST="${MONGODB_HOST:-teleporter-mongodb}"
USER="${MONGO_INITDB_ROOT_USERNAME:-root}"
PASSWORD="${MONGO_INITDB_ROOT_PASSWORD:-root}"
BACKUP_DIR="/backup"

# Check if mongodb-org-tools is present
if ! dpkg -s mongodb-org-tools &> /dev/null
then
    apt update
    DEBIAN_FRONTEND=noninteractive apt install -y gnupg curl
    curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-7.0.list
    apt update
    DEBIAN_FRONTEND=noninteractive apt install mongodb-org-tools -y
fi

# Get the day of the week
DAY=$(date +%A | awk '{print tolower($0)}')

# Check if an argument is provided for on-demand backup
if [ "$1" == "--save" ]; then
  # Generate a backup with the current date in the filename
  DATE_INSTANT=$(date +%Y-%m-%d_%H-%M-%S)
  mongodump --host $HOST --username $USER --password "$PASSWORD" --out "$BACKUP_DIR/mongodb-$DATE_INSTANT"
  if [ $? -eq 0 ]; then
    tar -zcvf "$BACKUP_DIR/mongodb-$DATE_INSTANT.tar.gz" "$BACKUP_DIR/mongodb-$DATE_INSTANT"
    rm -rf "$BACKUP_DIR/mongodb-$DATE_INSTANT"
    echo "On-demand backup created for $DATE_INSTANT."
  else
    echo "On-demand backup failed."
  fi
  exit 0
fi

# Check if today's backup already exists
if [ -f "$BACKUP_DIR/mongodb-$DAY.tar.gz" ]; then
  # Check if the file was modified today
  if [ "$(date -r "$BACKUP_DIR/mongodb-$DAY.tar.gz" +%Y-%m-%d)" == "$(date +%Y-%m-%d)" ]; then
    echo "Backup for $DAY already exists."
    exit 0
  fi
fi

# Generate a backup
mongodump --host $HOST --username $USER --password "$PASSWORD" --out "$BACKUP_DIR/mongodb-$DAY"
if [ $? -eq 0 ]; then
  tar -zcvf "$BACKUP_DIR/mongodb-$DAY.tar.gz" "$BACKUP_DIR/mongodb-$DAY"
  rm -rf "$BACKUP_DIR/mongodb-$DAY"
  echo "Backup for all databases successful for $DAY."
else
  echo "Backup for all databases failed for $DAY."
  exit 1
fi

# Delete old backups if they exist
find $BACKUP_DIR -type f -name "mongodb-*.tar.gz" -mtime +6 -exec rm {} \;

echo "Backup rotation successful."
