#Exercicio o "Split" Manual (Substituição de Strings)

frase = input("Digite uma frase: ")+" "
palavra_atual = ""
lista_palavras = []

for caractere in frase: 
    if caractere !=" ": 
        palavra_atual +=caractere
    else: 
        if palavra_atual !="":
            lista_palavras.append(palavra_atual)
            palavra_atual=""

print(f"\nVetor de palavras gerado: {lista_palavras}")
