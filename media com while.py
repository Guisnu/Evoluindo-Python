qtdnumeros = int(input("digite a quantidade de valores que serão calculados"))
contador = 0
valores = 0

while contador < qtdnumeros:
    valores += float(input("digite o valor de cada numero"))
    contador = contador +1

media = valores / contador

print(media)
