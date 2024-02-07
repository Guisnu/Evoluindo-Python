def calcular_fatorial(n):
    fat = 1
    for i in range (1,n+1):
        fat*=i
    return(fat)

#chamado da função
n = int(input("Digite o valo de n: "))
print(f"O fatorial de {n} é {calcular_fatorial(n)}") 