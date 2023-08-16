'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

estado = input("Diga a sigla de um estado brasileiro: ")

if estado == 'RJ' or estado == 'SP' or estado == 'MG' or estado == 'ES':
    print("Faz parte da região sudeste")
else:
    print("Não faz parte da região sudeste")
