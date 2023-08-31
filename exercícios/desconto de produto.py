preco = float(input("Digite o valor da compra: "))

print("1. À vista\n2. À vista no cartão\n3. Parcelado")
opcao = int(input("Digite a forma de pagamento: "))

if(opcao == 1):
    calculo = preco * 0.90
    print(f"Preço final: {calculo}")
elif(opcao == 2):
    calculo = preco * 0.95
    print(f"Preço final: {calculo}")
elif(opcao == 3):
    print(f"preço final: {preco}")
else:
    print("Opção inválida!")



