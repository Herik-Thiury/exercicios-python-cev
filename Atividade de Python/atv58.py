from random import randint

sorteio = randint(0, 10)
contador = 1

entrada = int(input("Digite um número: "))

while entrada != sorteio:
    entrada = int(input("Errou, tente novamente! "))
    contador += 1
    
print(f"Você acertou em {contador} tentativas!")    