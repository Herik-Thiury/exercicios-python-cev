lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite o valor {c + 1}: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]    
        elif lista[c] < menor:
            menor = lista[c]    
print(f"Você digitou: {lista}")

print(f"O maior número é: {maior} na posição")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}")
        print("")

print(f"O menor número é: {menor} na posição")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}")