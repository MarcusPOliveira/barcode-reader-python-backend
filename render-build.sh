#!/usr/bin/env bash

# Instala dependências do sistema
apt-get update && apt-get install -y libzbar0

# Cria links físicos necessários
mkdir -p /usr/local/lib
ln -sf /usr/lib/x86_64-linux-gnu/libzbar.so.0 /usr/local/lib/libzbar.so

# Verifica a instalação
ls -l /usr/lib/x86_64-linux-gnu/libzbar* /usr/local/lib/libzbar*

# Instala dependências Python
pip install -r requirements.txt