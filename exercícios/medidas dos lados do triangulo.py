lado_1 = float(input("tamanho lado 1: "))
lado_2 = float(input("tamanho lado 2: "))
lado_3 = float(input("tamanho lado 3: "))

if(lado_1 == lado_2 and lado_1 == lado_3):
    print("Todos os lados são iguais logo o triangulo é Equilatero.")

elif(lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3):
    print("Dois dos lados são iguais logo o triangulo é Isoceles.")

else:
    print("Todos os lados são diferentes logo o triangulo é Escaleno.")