nome = input("Informe seu nome: ")
anonascimento = int(input("Informe o ano de nascimento: "))
anoatual = int(input("Informe o ano atual: "))

idade = anoatual - anonascimento 

if(idade >= 16):
    print("Você já pode votar")

