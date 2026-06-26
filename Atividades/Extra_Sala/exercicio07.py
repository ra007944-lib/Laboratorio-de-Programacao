#Exercicio "O separador Par/impar dinâmico"

pares = []
impares = []
print("Digite 10 números inteiros únicos: ")

while len(pares)+len(impares)<10:
    num = int(input("Número: "))
    if num in pares or num in impares:
        print("Esse número já foi digitado! Tente outro")
        continue
    if num % 2 == 0: 
        pares.append(num)
    else:
        impares.append(num)

print(f"\nVetor de pares: {pares}")
print(f"\nVetor de pares: {impares}")

