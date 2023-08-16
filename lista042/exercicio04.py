'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana
'''

num = int(input("Escolha um número: "))

if num == 1:
    print("Domingo")
if num == 2:
    print("Segunda-Feira")
if num == 3:
    print("Terça-Feira")
if num == 4:
    print("Quarta-Feira")
if num == 5:
    print("Quinta-Feira")
if num == 6:
    print("Sexta-Feira")
if num == 7:
    print("Sabado")
else:
    print("número inválido")
