'''
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo
'''

nome = input("Qual seu nome? ")

nota1 = float(input("Qual sua nota da prova 1? "))

nota2 = float(input("Qual sua nota da prova 2?" ))

media = nota1 + nota2

media1 = media/2

if media1>=7:
    print("Aprovado")
if media1<6.9 and media1>3.0:
    print("Prova final")
if media1<=3.0:
    print("Reprovado")
