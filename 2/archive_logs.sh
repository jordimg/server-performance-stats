#!/bin/bash

# Directorio de logs y directorio de archivos comprimidos
LOG_DIR="/var/log"
ARCHIVE_DIR="/var/log/archive"
RETENTION_DAYS=30  # Días antes de eliminar logs antiguos

# Crear el directorio de archivos archivados si no existe
mkdir -p "$ARCHIVE_DIR"

# Obtener la fecha actual
TIMESTAMP=$(date +"%Y-%m-%d")

# Comprimir los logs en un solo archivo
tar -czf "$ARCHIVE_DIR/logs-$TIMESTAMP.tar.gz" "$LOG_DIR"/*.log 2>/dev/null

# Eliminar logs antiguos en el directorio de archivos archivados
find "$ARCHIVE_DIR" -type f -name "*.tar.gz" -mtime +$RETENTION_DAYS -exec rm {} \;

echo "Archivos de logs comprimidos y archivados en $ARCHIVE_DIR"
