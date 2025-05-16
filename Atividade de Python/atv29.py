velocidade = int(input("Digite a velocidade em kms do carro: "))

if velocidade > 80:
    multa = velocidade * 7
    print(f"O valor da sua multa foi: {multa:.2f}Km/h")
else:
    print("Você não foi multado!")    
