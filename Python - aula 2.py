'''
valor = float(input('Digite um valor:'))
juros = 0.1
resultado = valor + juros*valor

print('O total de juros é:',resultado,)'''
import random

#Operador relacional
'''
numero = int(input('Digite um valor:'))
resultado = numero > 0

print(resultado)'''

'''
numero = int(input('Digite um valor:'))
rd = numero % 5
nm5 = rd != 0

print(nm5)'''

#Operador de decisão
'''idade = int(input('Digite sua idade:'))

if(idade > 18):
    print('É maior de idade')

elif(idade < 18):
    print('É menor de idade')

else:
    print('Tem exatamente 18 anos')'''


'''
nota = float(input('Digite uma nota:'))

if(nota >= 9.0):
    print('Excelente')

elif(nota >= 7 and nota < 9):
    print('Boa')

elif(nota >= 5 and nota <9):
    print('Média')

else:
    print('Insuficiente')
'''

'''
idade = int(input('Digite a idade:'))

if(idade < 2):
    print('Bebê')

elif(idade < 13):
    print('Criança')

elif(idade < 18):
    print('Adolescente')

elif(idade < 60):
    print('Adulto')

else:
    print('Idoso')'''

'''
a = float(input('Digite um valor para A:'))
b = float(input('Digite um valor para B:'))
c = float(input('Digite um valor para C:'))

if a+b>c and a+c>b and b+c>a:
    print('É possível formar um triângulo.')

    if a == b and b == c:
        print('É um triangulo equilátero')

    elif a == b or b == c or a == c:
        print('É um triangulo isóceles')

else:
    print('Não é possível formar um triângulo')
'''

'''
adivinha = int(input('Digite um número de -100 a 100:'))
import random
numero = random.randint(-100,100)


if(adivinha == numero):
    print('Acertou!!!')

else:
    print('Errou, o número certo é:',numero,)
'''

'''
import random
opcao = random.choice(["Gustavo","Lucas","Luis","Giovane","Cauã","Ana","Mary","Iza"])

print(opcao)'''

import random
maquina = random.choice(["Pedra", "Papel", "Tesoura"])

humano = input("Digite Pedra, Papel ou Tesoura.")


if(maquina == humano):
       print('Empate')

elif(humano == "Pedra" and maquina == "Tesoura")\
       or(humano == "Papel" and maquina == "Pedra")\
       or(humano == "Tesoura" and maquina == "Papel"):
       print('Ganhou!')

else:
       print('Perdeu')

print('A máquina escolheu:',maquina,)