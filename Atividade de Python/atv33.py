entrada1 = int(input(""))
entrada2 = int(input(""))
entrada3 = int(input(""))

menor = entrada1
if entrada2 < entrada1 and entrada2 < entrada3:
    menor = entrada2
if entrada3 < entrada1 and entrada3 < entrada2:
    menor = entrada3

maior = entrada1
if entrada2 > entrada1 and entrada2 > entrada3:
    maior = entrada2
if entrada3 > entrada1 and entrada3 > entrada2:
    maior = entrada3
print(f"Menor = {menor}")    
print(f"Maior = {maior}")        