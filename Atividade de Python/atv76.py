preços = ("Lápis", 1.75, 
          "Borracha", 2.00, 
          "Caderno", 15.90)
print("-"*30)
print("     LISTAGEM DE PRODUTOS        ")
print("-"*30)
for i in range(0, len(preços)):
    if i % 2 == 0:
        print(f"{preços[i]:.<30}", end="")
    else:
        print(f"R${preços[i]:>5}")
