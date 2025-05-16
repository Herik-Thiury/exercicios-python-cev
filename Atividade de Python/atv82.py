lista = []
listap = []
listai = []

while True:
    numero = int(input("Digite um valor: "))
    lista.append(numero)

    if numero % 2 == 0:
        listap.append(numero)
    else:
        listai.append(numero)    

    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp in "N":
        break

print(f"Você digitou: {lista}")   
print(f"Números pares: {listap}")    
print(f"Números ímpares: {listai}") 