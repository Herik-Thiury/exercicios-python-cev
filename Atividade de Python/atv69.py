contador_Idade = 0
contador_Homem = 0
contador_mulher = 0
while True:
    while True:
        try:
            idade = int(input("Quantos anos você tem? "))
            if idade > 0:
                break
            else:
                print("Idade inválida! Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro")        
            
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Qual seu sexo? [M/F] ")).strip().upper()[0]
        print("")

    if idade > 18:
        contador_Idade += 1

    if sexo == "M":
        contador_Homem += 1
         
    if sexo == "F" and idade < 20:
        contador_mulher += 1           

    proximo = " "
    while proximo not in "SN":
        proximo = str(input("Quer continuar? ")).strip().upper()[0]   
        print("")
    if proximo == "N":
        break   	

    
print(f"{contador_Idade} Pessoas tem mais de 18 anos")  
print("")
print(f"{contador_Homem} Pessoas do sexo masculino")   
print("")
print(f"{contador_mulher} Mulheres tem menos de 20 anos")   