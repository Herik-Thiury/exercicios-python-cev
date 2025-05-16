num = (int(input("")),
       int(input("")),
       int(input("")),
       int(input("")))
print(f"Voce digitou {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}a posição")
else:
    print("O valor 3 não apareceu")    
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
