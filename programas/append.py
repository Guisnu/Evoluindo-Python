#append usado para adicionar um dado ao final da lista

listanomes = []

while True:
    nome = input("Digite um nome")
    listanomes.append(nome)#adiciona a variavel nome a listanomes

    continuar = input("Digite sim para continuar ou não para parar")
    if(continuar=="não" or continuar=="NÃO"):
        break

print(listanomes)
