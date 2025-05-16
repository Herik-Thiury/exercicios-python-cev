listanum = []
v = ""
while True:
    n = int(input("Digite seus valores: "))
    listanum.append(n)

    r = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if r in "Nn":
        break

    if 5 in listanum:
        v = True    
    
listanum.sort(reverse=True)  

print(f"\nVocê digitou: {len(listanum)} números")
print(f"{listanum}")
if 5 in listanum:
    print("O 5 está na lista!")
else:
    print("O 5 não está na lista!")    
