from time import sleep

print(40* "=")
print("Boas vindas ao meu primeiro projeto!")
print(40* "=")

nome = input("Digite seu nome: ")
print("Iniciando calculadora...")
sleep(3)

print(f"Calculadora inicicada! E aí {nome} bora começar? ")

continua = "s"

while(continua == "s"):
    num1 = float(input("Digite o primeito numero: "))
    op = str(input("Digite a operação ( + , - , * , / ): "))
    num2 = float(input("Digite o segundo numero: "))

    if(op == "+"):
        resultado = num1 + num2
    elif(op == "-"):
        resultado = num1 - num2
    elif(op == "*"):
        resultado = num1 * num2
    elif(op == "/"):
        resultado = num1 / num2
    else:
        resultado = 0
    print(f"Resultado: {resultado}")

    continua = input("Deseja continuar s/n: ")

print("Fim")
