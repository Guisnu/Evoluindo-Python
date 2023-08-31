continua = str(input("Deseja iniciar o programa s/n: "))

while(continua == "s"):
    numero = int(input("Digite um numero para dobrar: "))
    calculo = numero * 2
    print(calculo)
    
    continua = str(input("Deseja continuar s/n: "))
    
print("Fim")