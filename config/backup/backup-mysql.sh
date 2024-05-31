#!/bin/sh

# Variables
HOST="${MARIADB_HOST:-teleporter-mariadb}"
USER="${MARIADB_USER:-root}"
PASSWORD="${MARIADB_ROOT_PASSWORD:-root}"
BACKUP_DIR="/backup"

# Get the day of the week
DAY=$(date +%A | awk '{print tolower($0)}')

# Check if an argument is provided for on-demand backup
if [ "$1" == "--save" ]; then
  # Generate a backup with the current date in the filename
  DATE_INSTANT=$(date +%Y-%m-%d_%H-%M-%S)
  docker exec $HOST mariadb-dump --user $USER --password="$PASSWORD" --all-databases --single-transaction > "$BACKUP_DIR/mysql-$DATE_INSTANT.sql"
  if [ $? -eq 0 ]; then
    gzip "$BACKUP_DIR/mysql-$DATE_INSTANT.sql"
    echo "On-demand backup created for $DATE_INSTANT."
  else
    echo "On-demand backup failed."
    rm -rf "$BACKUP_DIR/mysql-$DATE_INSTANT.sql"
  fi
  exit 0
fi

# Check if today's backup already exists
if [ -f "$BACKUP_DIR/mysql-$DAY.sql.gz" ]; then
  # Check if the file was modified today
  if [ "$(date -r "$BACKUP_DIR/mysql-$DAY.sql.gz" +%Y-%m-%d)" == "$(date +%Y-%m-%d)" ]; then
    echo "Backup for $DAY already exists."
    exit 0
  fi
fi

# Generate a backup
docker exec $HOST mariadb-dump --user $USER --password="$PASSWORD" --all-databases --single-transaction > "$BACKUP_DIR/mysql-$DAY.sql"
if [ $? -eq 0 ]; then
  gzip "$BACKUP_DIR/mysql-$DAY.sql"
  echo "Backup for all databases successful for $DAY."
else
  echo "Backup for all databases failed for $DAY."
  rm -rf "$BACKUP_DIR/mysql-$DAY.sql"
  exit 1
fi

# Delete old backups if they exist
find $BACKUP_DIR -type f -name "mysql-*.sql.gz" -mtime +6 -exec rm {} \;

echo "Backup rotation successful."
