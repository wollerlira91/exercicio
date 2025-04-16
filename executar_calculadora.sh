

#!/bin/bash

# Verifica se o Python está instalado
if command -v python3 &>/dev/null; then
    python3 calculadora.py
elif command -v python &>/dev/null; then
    python calculadora.py
else
    echo "Python não está instalado. Por favor, instale o Python para executar o programa."
    exit 1
fi

