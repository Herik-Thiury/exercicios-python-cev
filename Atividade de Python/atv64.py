print("Digite quantos números quiser, se quiser parar, digite 999")
n1 = ""
c = 0
s = 0
while n1 != 999:
    n1 = int(input(""))
    c += 1
    if n1 != 999:
        s += n1
    if n1 == 999:
        c -= 1    
print(f"Você digitou {c} números. E a soma entre eles foi: {s}")