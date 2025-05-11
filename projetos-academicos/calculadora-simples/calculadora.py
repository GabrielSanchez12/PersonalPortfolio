def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("Escolha a operação: + - * /")
operacao = input("Operação: ")
x = float(input("Primeiro número: "))
y = float(input("Segundo número: "))

if operacao == "+":
    print(somar(x, y))
elif operacao == "-":
    print(subtrair(x, y))
elif operacao == "*":
    print(multiplicar(x, y))
elif operacao == "/":
    print(dividir(x, y))
else:
    print("Operação inválida")
