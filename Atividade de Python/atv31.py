kms = int(input("Digite a quantidade de kms da sua viagem: "))

if kms <= 200:
    resultado1 = kms * 0.50
    print(resultado1)
else:
    resultado2 = kms * 0.45
    print(resultado2)
