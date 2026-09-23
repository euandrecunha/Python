print ("""Olá pessoal, aqui é o André e este é meu primeiro código em Python!
-----""")

#Nome do aluno
aluno = input ("Insira o nome do aluno: ")

#Notas do aluno
n1 = float (input ("Nota da Prova 1: "))
n2 = float (input ("Nota da Prova 2: "))
n3 = float (input ("Nota da Prova 3: "))

#Cálculo da média
media = sum([n1, n2, n3]) / len([n1, n2, n3])
if media >= 7:
    status = "Aprovado"
else:
    status = "Reprovado"

print (f"""O aluno {aluno}, obteve média final: {media:.1f}.
Sua situação é: {status}.
-----""")




