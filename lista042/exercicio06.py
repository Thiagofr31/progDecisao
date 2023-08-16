'''
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”
'''



n = int(input("Informe seu ano de nascimento: "))

a = int(input("Informe o ano atual: "))

idade = a-n

if n > a:
    print("Dados inseridos estão incorretos")

else:
    print(f"Você tem {idade} anos")


