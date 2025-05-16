reta1 = float(int(input("")))
reta2 = float(int(input("")))
reta3 = float(int(input("")))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("É um triangulo!")
else:
    print("Não é um triângulo!")    