cont = ("zero", "um", "dois", "tres", "cinco",
        "seis", "sete", "oito", "nove", "dez", 
        "onze", "doze", "treze", "quatorze", "quinze",
        "dezeseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    entrada = int(input("Digite um número entre 0 e 20: "))
    if 0 <= entrada <= 20:
        break
    print("Tente novamente. ", end="")
print(f"Você digitou o número {cont[entrada]}")        