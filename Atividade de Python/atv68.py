from random import randint

print("Vamos jogar Par ou Ímpar!")

v = 0
while True:
    maquina = randint(0,10)
    analisador = int(input("Digite 1 para PAR e 2 para ÍMPAR: "))
    jogo = int(input("Agora digite um número: "))
    
    s = jogo + maquina
    print(f"Eu escolhi = {maquina}")
    print(f"A soma de {jogo} + {maquina} é: {s}")
    if analisador == 1:
        if s % 2 == 1:
            print("Você perdeu, tente novamente")
            break
        if s % 2 == 0:
            print("Voce ganhou!")
            v += 1
    if analisador == 2:
        if s % 2 == 1:
            print("Você ganhou!")
            v += 1
        if s % 2 == 0:
            print("Você perdeu, tente novamente")
            break  
print(f"Número de vitórias: {v}")