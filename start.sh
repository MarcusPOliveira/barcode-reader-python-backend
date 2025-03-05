#!/bin/bash

echo "Baixando e configurando o ZBar..."

# Baixa a biblioteca libzbar.so para um diretório acessível
curl -L -o /usr/local/lib/libzbar.so https://github.com/mchehab/zbar/raw/master/zbar/libzbar.so

# Garante que a biblioteca seja reconhecida pelo sistema
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

echo "Iniciando a aplicação..."
uvicorn main:app --host 0.0.0.0 --port $PORT