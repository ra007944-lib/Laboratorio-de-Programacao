#

nomes_originais = []
for i in range(5):
    nome = input(f"Digite o {i+1} nome:")
    nomes_originais.append(nome)

nomes_invertidos = []
for i in range(1,6):
    nomes_invertidos.append(nomes_originais[-i]) 

print(f"\nLista original: {nomes_originais}")
print(f"\nLista original: {nomes_invertidos}")