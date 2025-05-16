#Variáveis
soma_idade = 0
media = 0
maior_idade = 0
nome_velho = ""
menor_idade = 0
for c in range(1,5):
    print(f"Pessoa {c}")
    nome = str(input("Qual seu nome? ")).strip()
    idade = int(input("Qual sua idade? "))
    sexo = str(input("Qual seu sexo? [M/F]? ")).strip().upper()
    soma_idade += idade
    media = soma_idade / 4
    if c == 1 and sexo in "Mm":
        maior_idade = idade
        nome_velho = nome
    if sexo in "Mm" and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if idade < 20 and sexo in "Ff":
        menor_idade += 1
print(f"{media:.0f}")
print(f"O homem mais velho tem {maior_idade} anos e seu nome é {nome_velho}")
print(f"{menor_idade} mulheres tem menos de 20 anos")