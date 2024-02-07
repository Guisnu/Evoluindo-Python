n = int(input("Digite um numero para calcular a media: "))

def calcular_media(n):
    soma = 0
    for i in range (1,n+1):
        soma+=i
    media = soma / n
    return(media)

#chamada da função considerando "n" igual 20
print(f"A soma dos paresd de 1 até {n} é {calcular_media(n)}")