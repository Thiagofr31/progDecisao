'''
Crie um programa que pergunte dois números ao usuário.
Em seguida o programa deverá somar os dois números e apresentar o
resultado se o valor for maior que 10.
'''

# Inputs

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2

# Condições e Print

if  ( soma > 10 ) :
    print("A soma dos números inseridos é ", soma)

print("FIM DO PROGRAMA")

