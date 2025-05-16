primeiro = int(input(""))
razao = int(input(""))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end= "- ")