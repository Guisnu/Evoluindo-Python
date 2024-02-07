def main():
    resp = "S"

    while(resp != "N"):
        print(" 1-Soma \n 2-Subtrair \n 3-multiplicar \n 4-Dividir")
        opc = int(input("Digite a opção desejada 1-4: "))

        match opc:
            case 1:
                num1,num2 = Ler_numeros()
                print(f"A soma é {Somar_numeros(num1,num2)}")
            case 2:
                num1,num2 = Ler_numeros()
                print(f"A subtração é {Subtrair_numeros(num1,num2)}")
            case 3:
                num1,num2 = Ler_numeros()
                print(f"A multiplicação é {Multiplicar_numeros(num1,num2)}")
            case 4:
                num1,num2 = Ler_numeros()
                print(f"A Divisão é {Dividir_numeros(num1,num2)}")
            case _:
                print("opção inválida")

    resp = input("Deseja realizar outra operação? (S/N): ")

#funções do programador
def Ler_numeros():
    num1 = int(input("digite o primeiro número: "))
    num2 = int(input("digite o segundo número: "))
    return(num1,num2)

def Somar_numeros(num1,num2):
    soma = num1 + num2
    return(soma)

def Subtrair_numeros(num1,num2):
    sub = num1 - num2
    return(sub)

def Multiplicar_numeros(num1,num2):
    mult = num1 * num2
    return(mult)

def Dividir_numeros(num1,num2):
    div = num1 / num2
    return(div)

if __name__ == "__main__":
    main()