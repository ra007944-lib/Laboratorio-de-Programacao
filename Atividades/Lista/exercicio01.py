import random

vetor1= []
vetor2 = [0,0,0,0,0,0]

for e in range (100):
    vetor1.append(random.randint(1,6))
for i in range (6):
    vetor2[i] = vetor1.count(i+1)
# vetor2[0] = vetor1.count(1)
# vetor2[1] = vetor1.count(2)
# vetor2[2] = vetor1.count(3)
# vetor2[3] = vetor1.count(4)
# vetor2[4] = vetor1.count(5)
# vetor2[5] = vetor1.count(6)
print(vetor1)
print(f"1: {vetor2[0]} | 2: {vetor2[1]} | 3: {vetor2[2]} | 4: {vetor2[3]} | 5: {vetor2[4]} | 6: {vetor2[5]} ")

import random

lancamentos=[]
for i in range(100): #serve para gerar aleatoriamente 100 vezes
    resultado=random.randint(1,6) #vai girar de 1 à 6
    lancamentos.append(resultado)

frequencia = []
for face in range(1,7):
    quantidade = lancamentos.count(face)
    frequencia.append(quantidade) #quantidade de vezes que encontrou em cada face 

print("Vetor de frequências (quantidade de vezes das faces: 1, 2, 3, 4, 5, 6)")
print(frequencia)
print("\nvetor de lançamentos (100 vezes)")
print(lancamentos)