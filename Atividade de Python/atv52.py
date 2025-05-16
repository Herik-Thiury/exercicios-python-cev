num = int(input(""))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Não é primo")
            break
    else:
        print("É primo")
elif num == 0:
    print("É zero")        
elif num == 1:
    print("É 1")
else:
    print("Não é negativo")