salario = int(input("Digite seu salário: "))

porc1 = salario * 0.10 + salario
porc2 = salario * 0.15 + salario

if salario > 1250:
    print(porc1)
else:
    print(porc2)  