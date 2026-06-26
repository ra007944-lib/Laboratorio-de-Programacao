#3 - Faça um programa que percorre um vetor e imprime na tela a média dos valores do vetor e o 
# valor mais próximo da média. Exemplo:
#Vetor:[2.5, 7,5, 10.0, 4.0]
#Média: 6.0
#Valor mais próximo da média: 7.5

vetor=[2.5, 7,5, 10.0, 4.0]
#soma = sum(vetor) vai somar tudo que tem no vetor
soma = 0
for valor in vetor:
    soma += valor
media = soma / len(vetor) #vair achar a media 

proximo_da_media = vetor[0]
menor_distancia = abs(vetor[0] - media) #abs serve para dar valor absoluto
for valor in vetor:
    distancia_atual = abs(valor - media) 
    if distancia_atual < menor_distancia:
        menor_distancia = distancia_atual
        proximo_da_media = valor

print(f"Vetor: {vetor}")
print(f"Média: {media:.1f}")
print(f"Valor mais próximo da média: {proximo_da_media}")

print(media)

