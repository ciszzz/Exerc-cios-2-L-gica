somaPar = 0
somaImpar = 0
quantPar = 0
quantImpar = 0

for i in range(10):
    numeros = int(input("Insira um número: "))

    if numeros % 2 == 0:
        print("Número par:", numeros)
        somaPar += numeros
        quantPar += 1
    else:
        print("Número ímpar:", numeros)
        somaImpar += numeros
        quantImpar += 1

print("Quantidade de números pares:", quantPar)
print("Quantidade de números ímpares:", quantImpar)
print("Soma dos números pares:", somaPar)
print("Soma dos números ímpares:", somaImpar)


