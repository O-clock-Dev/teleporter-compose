#!/bin/bash

# Variables
HOST="${POSTGRES_HOST:-teleporter-postgres}"
USER="${POSTGRES_USER:-postgres}"
PASSWORD="${POSTGRES_PASSWORD:-postgres}"
BACKUP_DIR="/backup"

# Get the day of the week
DAY=$(date +%A | awk '{print tolower($0)}')

# Check if an argument is provided for on-demand backup
if [ "$1" == "--save" ]; then
  # Generate a backup with the current date in the filename
  DATE_INSTANT=$(date +%Y-%m-%d_%H-%M-%S)
  docker exec -e PGPASSWORD="$PASSWORD" $HOST pg_dumpall --host=$HOST --username=$USER > "$BACKUP_DIR/postgres-$DATE_INSTANT.sql"
  if [ $? -eq 0 ]; then
    gzip "$BACKUP_DIR/postgres-$DATE_INSTANT.sql"
    echo "On-demand backup created for $DATE_INSTANT."
  else
    echo "On-demand backup failed."
    rm -rf "$BACKUP_DIR/postgres-$DATE_INSTANT.sql"
  fi
  exit 0
fi

# Check if today's backup already exists
if [ -f "$BACKUP_DIR/postgres-$DAY.sql.gz" ]; then
  # Check if the file was modified today
  if [ "$(date -r "$BACKUP_DIR/postgres-$DAY.sql.gz" +%Y-%m-%d)" == "$(date +%Y-%m-%d)" ]; then
    echo "Backup for $DAY already exists."
    exit 0
  fi
fi

# Generate a backup
docker exec -e PGPASSWORD="$PASSWORD" $HOST pg_dumpall --host=$HOST --username=$USER > "$BACKUP_DIR/postgres-$DAY.sql"
if [ $? -eq 0 ]; then
  gzip "$BACKUP_DIR/postgres-$DAY.sql"
  echo "Backup for all databases successful for $DAY."
else
  echo "Backup for all databases failed for $DAY."
  rm -rf "$BACKUP_DIR/postgres-$DAY.sql"
  exit 1
fi

# Delete old backups if they exist
find $BACKUP_DIR -type f -name "postgres-*.sql.gz" -mtime +6 -exec rm {} \;

echo "Backup rotation successful."