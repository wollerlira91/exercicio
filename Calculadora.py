import sys

# Verifica se o usuário forneceu dois números e uma operação
if len(sys.argv) != 4:
    print("Uso: python3 <script.py> <num1> <operacao> <num2>")
    print("Operações disponíveis: +, -, x, /")
    sys.exit(1)

num1 = sys.argv[1]
operacao = sys.argv[2]
num2 = sys.argv[3]

# Verifica se os números são válidos
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Erro: Ambos os operandos devem ser números válidos.")
    sys.exit(1)

# Executa a operação
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == 'x':
    resultado = num1 * num2
elif operacao == '/':
    if num2 == 0:
        print("Erro: Divisão por zero não permitida.")
        sys.exit(1)
    resultado = num1 / num2
else:
    print("Erro: Operação inválida. Use +, -, x ou /.")
    sys.exit(1)

print(f"Resultado: {resultado}")