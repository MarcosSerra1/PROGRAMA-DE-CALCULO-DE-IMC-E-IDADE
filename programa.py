"""
Programa para calculo de IMC e idade.
"""

print('Caro ussuario colocar "." no lugar ","')
print()
nome = str(input('Qual é o seu nome? '))
ano_nasc = int(input('Em que ano você nasceu? '))
altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso?(kg)' ))
ano_atu = int(input('Em que ano estamos? '))
imc = peso / (altura ** 2)
idade = ano_atu - ano_nasc
print()
print('=====================================')
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
if imc < 18.5:
    print('Você está com o peso abaixo do seu percentual')
elif imc <= 24.9:
    print('Você está com seu peso normal')
elif imc <= 29.9:
    print('Você está com sobrepeso')
elif imc <= 39.9:
    print('Você está com obsidade')
elif imc > 39.9:
    print('Você está com obsidade morbida')
print('=====================================')
