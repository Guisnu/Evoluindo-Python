#operadores lógicos 

# AND - TODAS AS EXPRESSÕES VERDADEIRAS 
# OR - PELO MENOS UMA EXPRESSÃO SEJA VERDADEIRA
# NOT - INVERTER EXPRESSÃO

estado = input("Digite seu estado: ")

if(estado == "bahia" or estado == "pernambuco"):
    print("A trasportadora atende ao seu estado!")
else:
    print("A transportadora infelizmente não atende ao seu estado")