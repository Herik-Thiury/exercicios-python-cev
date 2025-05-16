feminino = ""
masc = ""
sexo = str(input("Digite seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Digite seu sexo: [M/F] ")).strip().upper()[0]
if sexo == "F":
    print("Sexo Feminino registrado com sucesso!")
if sexo == "M":
    print("Sexo Masculino registrado com sucesso!")  