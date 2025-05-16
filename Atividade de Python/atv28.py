from random import randint
computador = randint(0, 5)

entrada = int(input("Qual número estou pensando?: "))
print("Processando...")

if entrada == computador:
    print("Acertou!")
else:
    print(f"Errou :( Pensei no número {computador})")