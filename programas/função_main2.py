def main():
    lista_numeros = []
    tam = int(input("Digite o tamanho da lista: "))
    ler_lista (lista_numeros, tam)
    print(f"A média dos elementos da lista é {calcular_media_lista(lista_numeros, tam)}")
    print(f"A nova lista (quadrados eos elementos da lista_numeros) e: {criar_lista_quadrado(lista_numeros, tam)}")

# Função para ler os elementos de uma lista
def ler_lista (lista_numeros, tam):
    for i in range(tam):
        lista_numeros.append(int(input("Digite um elemento da lista: ")))

# Funções para calcular e retornar a média dos elementos da lista
def calcular_media_lista (lista_numeros, tam):
    soma = 0
    for i in range(tam):
        soma+=lista_numeros[i]
    media = soma / tam
    return(media)

#função para criar e retornar uma nova lista com elementos da lista numeros elevados ao quadrado

def criar_lista_quadrado(lista_numeros, tam):
    lista_quadrado = []
    for i in range (tam):
        lista_quadrado.append(lista_numeros[i]**2)
    return(lista_quadrado)

if __name__ == "__main__":
    main()