#operadores lógicos 

# AND - TODAS AS EXPRESSÕES VERDADEIRAS 
# OR - PELO MENOS UMA EXPRESSÃO SEJA VERDADEIRA
# NOT - INVERTER EXPRESSÃO 

sou = input("Digite: ")
idade = int(input("idade: "))

if(sou == "homem" and idade >= 18):
    print("Você deve tirar a reservista!")
