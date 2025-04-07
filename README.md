#!/bin/bash

# Verifica se o usuário forneceu dois números e uma operação
if [ $# -ne 3 ]; then
    echo "Uso: $0 <num1> <operacao> <num2>"
    echo "Operações disponíveis: +, -, x, /"
    exit 1
fi

num1=$1
operacao=$2
num2=$3

# Verifica se os números são válidos
if ! [[ "$num1" =~ ^[0-9]+([.][0-9]+)?$ ]] || ! [[ "$num2" =~ ^[0-9]+([.][0-9]+)?$ ]]; then
    echo "Erro: Ambos os operandos devem ser números válidos."
    exit 1
fi

# Executa a operação
case $operacao in
    +)
        resultado=$(echo "$num1 + $num2" | bc -l)
        ;;
    -)
        resultado=$(echo "$num1 - $num2" | bc -l)
        ;;
    x)
        resultado=$(echo "$num1 * $num2" | bc -l)
        ;;
    /)
        if [ "$num2" == "0" ]; then
            echo "Erro: Divisão por zero não permitida."
            exit 1
        fi
        resultado=$(echo "$num1 / $num2" | bc -l)
        ;;
    *)
        echo "Erro: Operação inválida. Use +, -, x ou /."
        exit 1
        ;;
esac

echo "Resultado: $resultado"
