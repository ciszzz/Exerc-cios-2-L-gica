nomeVelho = ""
idadeVelho = 0

for i in range(5):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    if idade > idadeVelho:
        idadeVelho = idade
        nomeVelho = nome

print("A pessoa mais velha é:", nomeVelho)
print("Idade:", idadeVelho)