#Exercicio o Histório Balancete de caixa

historico = []
while True:
    valor=float(input("Digite o Valor da Operação (0 para sair). R$ "))
    if valor == 0:
        break
    historico.append(valor)
    
for i in range(len(historico) -1, -1, -1 ):
    if abs(historico[i]) > -5.0 and abs(historico[i]) < 5.0:
        del historico[i] 

saldo_final = sum(historico)
print("-"*30)
print(f"Histórico filtrado: {historico} ")
print(f"Salto final do caixa: R$ {saldo_final:.2f}")