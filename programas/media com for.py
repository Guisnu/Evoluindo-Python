qtdvalores = int(input("Digite a quantidade de valores que serão calculados"))
contador = 0
valores = 0

for contador in range(contador,qtdvalores,1):
    valores += float(input("Digite o valor do numero"))

media = valores / contador

print(media)

#media de valores em for a