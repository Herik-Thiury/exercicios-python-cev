import random

numeros = random.sample(range(1, 101), 5)

tupla = tuple(numeros)
maior = max(tupla)
menor = min(tupla)

print(f"Eu sorteei esses números: {tupla}")
print(f"E o menor valor é {menor} e o maior é {maior}")