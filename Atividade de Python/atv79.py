listanum = []

while True:
    n = int(input(""))
    if n not in listanum:
        listanum.append(n)
    else:
        print("Valor ja existe!")  

    p = str(input("Quer continuar? [S/N] "))
    if p in "Nn":
        break
listanum.sort()
print(listanum)        