palavra = input("Digite uma palavra: ").lower() #lower força letras minusculas
contador_vogais = 0
for letra in palavra:
    if letra in "aeiou": 
        contador_vogais += 1
print(f"A palavra contém {contador_vogais} vogais ")