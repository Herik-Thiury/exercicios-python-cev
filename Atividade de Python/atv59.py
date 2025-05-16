n1 = float(input("Digite um valor: "))
n2 = float(input("Digite um valor: "))
opção = 0

while opção != 5:
      print("""            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos números
            [5] Sair do programa""")
      
      opção = int(input("Qual sua opção? "))

      if opção == 1:
            soma = n1 + n2
            print(f"A soma de {n1:.2f} + {n2:.2f} é {soma:.2f}")
      elif opção == 2:
            produto = n1 * n2
            print(f"A multiplicação de {n1:.2f} + {n2:.2f} é {produto:.2f}")
      elif opção == 3:
            if n1 > n2:
                  print(f"O {n1} é maior")   
            else:
                  print(f"O {n2} é maior")
      elif opção == 4:
            n1 = float(input("Digite um valor: "))
            n2 = float(input("Digite um valor: "))
      elif opção == 5:
            print("Saindo do programa...")
            break
      else:
            print("Opção inválida. Tente novamente")