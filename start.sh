#!/bin/bash

echo "Instalando dependências do sistema..."
apt-get update && apt-get install -y libzbar0

echo "Iniciando a aplicação..."
uvicorn main:app --host 0.0.0.0 --port $PORT