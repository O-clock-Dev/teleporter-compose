#!/bin/sh

# Variables
HOST="${MONGODB_HOST:-teleporter-mongodb}"
USER="${MONGO_INITDB_ROOT_USERNAME:-root}"
PASSWORD="${MONGO_INITDB_ROOT_PASSWORD:-root}"
BACKUP_DIR="/backup"

# Get the day of the week
DAY=$(date +%A | awk '{print tolower($0)}')

# Check if an argument is provided for on-demand backup
if [ "$1" == "--save" ]; then
  # Generate a backup with the current date in the filename
  DATE_INSTANT=$(date +%Y-%m-%d_%H-%M-%S)
  docker exec $HOST mongodump --username $USER --password $PASSWORD --archive > "$BACKUP_DIR/mongodb-$DATE_INSTANT.bson"
  if [ $? -eq 0 ]; then
    cd $BACKUP_DIR && tar -zcf mongodb-$DATE_INSTANT.bson.gz mongodb-$DATE_INSTANT.bson
    rm -rf "$BACKUP_DIR/mongodb-$DATE_INSTANT.bson"
    echo "On-demand backup created for $DATE_INSTANT."
  else
    echo "On-demand backup failed."
    rm -rf "$BACKUP_DIR/mongodb-$DATE_INSTANT.bson"
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
docker exec $HOST mongodump --username $USER --password $PASSWORD --archive > "$BACKUP_DIR/mongodb-$DAY.bson"
if [ $? -eq 0 ]; then
  cd $BACKUP_DIR && tar -zcf mongodb-$DAY.bson.gz mongodb-$DAY.bson
  rm -rf "$BACKUP_DIR/mongodb-$DAY.bson"
  echo "Backup for all databases successful for $DAY."
else
  echo "Backup for all databases failed for $DAY."
  rm -rf "$BACKUP_DIR/mongodb-$DAY.bson"
  exit 1
fi

# Delete old backups if they exist
find $BACKUP_DIR -type f -name "mongodb-*.tar.gz" -mtime +6 -exec rm {} \;

echo "Backup rotation successful."
