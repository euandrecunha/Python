print ("""Olá pessoal, aqui é o André e este é meu primeiro código em Python!
-----""")

#Nome do aluno
aluno = "Arthur"

#Notas do aluno
n1 = 8
n2 = 8.5
n3 = 6

#Cálculo da média
media = sum([n1, n2, n3]) / len([n1, n2, n3])
if media >= 7:
    status = "Aprovado"
else:
    status = "Reprovado"

print (f"""Nome do aluno: {aluno}.
Notas das provas: {n1}, {n2} e {n3}.
Média final: {media}.
Situação: {status}.
-----""")
