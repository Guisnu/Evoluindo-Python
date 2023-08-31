# laço de while pt3

continua = "s"
soma = 0

while(continua == "s"):
    num = int(input("Digite um numero: "))
    soma += num

    continua =  str(input("Deseja continuar?(s/n): "))

print(f"Fim do program, soma total: {soma}")