#Faça um programa que percorre duas listas e intercala os elementos de ambas, formando uma
#  terceira lista. A terceira lista deve começar pelo primeiro elemento da lista menor
#Exemplo:
#Lista1=[1, 2,, 3, 4]  lista2=[10, 20, 30, 40, 50, 60]  lista3= [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]

lista1= [1, 2, 3, 4]
lista2= [10, 20, 30, 40, 50, 60]
lista_intercalada = []

if len(lista1) <= len(lista2): #Colocar qual a maior ou menor
    menor, maior= lista1, lista2
else:
    menor, maior = lista2, lista1

lista_intercalada = []

for i in range(len(maior)): #Intercalar as listas
    if (i < len(menor)):
        lista_intercalada.append(menor[i])
    lista_intercalada.append(maior[i]) 

print(f"Lista1: {lista1}")
print(f"Lista2: {lista2}")
print(f"Lista Intercalada: {lista_intercalada}")