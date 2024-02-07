def calcular_media_notas(nota1,nota2,nota3):
    media = nota1*0.4 + nota2*0.4 + nota3*0.2
    return(media)

#chamado da função
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

print(f"A media ponderada das 3 notas é {calcular_media_notas(nota1,nota2,nota3)}")