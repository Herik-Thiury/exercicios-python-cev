maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(""))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso        
print(f"O maior peso lindo foi de {maior}, e o menor foi de {menor}.")