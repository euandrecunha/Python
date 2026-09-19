print ("Olá pessoal, aqui é o André e este é meu primeiro código em Python!")
print ("-----")

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

print (f"As notas do aluno {aluno} foram: {n1}, {n2} e {n3}.")
print (f"Com isso, sua média final foi: {media} ({status}).")
print ("-----")
print ("Obrigado por acompanhar até aqui.")
