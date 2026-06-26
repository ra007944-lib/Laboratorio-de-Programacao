while True:
    num = int(input("Digite um número (0 - para sair):"))
    if num == 0: # "==" é usado para comparação
        print("Encerrando...")
        break; #trava o while
    if num >= 10 and num <=50:
        print("Dado válido!")
    else:
        print("Dado inválido!")