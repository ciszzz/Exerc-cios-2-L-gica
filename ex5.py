soma = 0
quantidade = 0

for i in range(5):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        soma += numero
        quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print("A média dos números pares é:", media)
else:
    print("Nenhum número par foi digitado.")
