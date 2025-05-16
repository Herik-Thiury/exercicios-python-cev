from datetime import date
atual = date.today().year
maioridade = 0
menoridade = 0
for c in range(1, 8):
    nasc = int(input("Em que ano a pessoa nasceu? "))
    idade = atual - nasc
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f"{maioridade} Pessoas são de maiores e {menoridade} Pessoas são de menores.")        