# receber 3 notas de um aluno
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
media = (nota1 + nota2 + nota3)/3 # calculo da media do aluno
# verificar se ele esta aprovado ou reprovado utilizando a media 7.0
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")