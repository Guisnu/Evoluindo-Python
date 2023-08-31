#Lista
minha_lista = [1,2,3,"quatro","cinco"]
um = minha_lista[0]  # Acessando o primeiro elemento (índice 0)
dois = minha_lista[3]  # Acessando o terceiro elemento (índice 2)

print(um)
print(dois)

#Tupla
minha_tupla = (1, 2, 3, "quatro", "cinco")
primeiro_elemento = minha_tupla[0]  # Acessando o primeiro elemento (índice 0)
terceiro_elemento = minha_tupla[4]  # Acessando o terceiro elemento (índice 2)

print(primeiro_elemento)
print(terceiro_elemento)

#conjunto

#Os elementos em um conjunto não possuem uma ordem
#específica e não podem ser acessados por índices,
#já que não possuem índices.
#Para verificar a existência de um elemento em um conjunto,
#você pode usar a palavra-chave in.

meu_conjunto = {1, 2, 3, 4, 5}
if 3 in meu_conjunto:
    print("O elemento 3 está presente no conjunto.")


#dicionário
meu_dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
nome = meu_dicionario["nome"]  # Acessando o valor associado à chave "nome"
idade = meu_dicionario["idade"]  # Acessando o valor associado à chave "idade"

print(nome)
print(idade)
