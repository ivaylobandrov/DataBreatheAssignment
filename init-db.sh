#!/bin/bash

# Import CSV data
for file in /csv/*.csv; do
    table=$(basename "$file" .csv)  # Extract table name from file
    psql -U $POSTGRES_USER -d $POSTGRES_DB -h $POSTGRES_HOST -c "\\copy $table FROM '$file' CSV HEADER"
done

echo "Data ingestion completed"

# Start the PostgreSQL service
docker-entrypoint.sh postgres
