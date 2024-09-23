#Estrutura de repetição
#for
'''
for numero in range(0,11,2):
    print(numero)
'''

'''
lista = ["vermelho","azul","verde","amarelo"]
for cor in lista:
    print('Cores:',cor,)
'''
'''
soma = 0
for valor in range(1,101):
    soma = soma + valor
    # soma = 0 + 1 = 1
    # soma = 1 + 2
    # soma = 1 + 2 + 3
    print(soma)
'''
'''
numero = int(input('Digite um número:'))
for tabuada in range (1,11):
    resultado = numero * tabuada
    print(numero, "x" ,tabuada, "=",resultado,)
'''

'''
aluno = input('Digite o nome do aluno:')
nota = int(input('Digite a quantidade de notas:'))

somaNotas = 0
for i in range(nota):
    valor = float(input('Digite a nota:'))
    somaNotas = somaNotas + nota

media =  somaNotas / nota
print('O aluno', aluno, 'ficou com', media, 'de média')
'''

#while

'''
import time
numero = int(input('Digite um número entre 5 e 10:'))

while numero >= 0:
    print(numero)
    numero = numero - 1
    time.sleep(1)
print('Terminou a contagem')
'''

'''
maior = 0
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1
    numero = float(input('Digite um número:'))
    if numero > maior:
        maior = numero
print("O maior número é:" ,maior,)
'''

'''
fatorial = 1
contador = 1

numero = int(input('Digite um número:'))
while contador <= numero:
    fatorial = fatorial * contador
    contador = contador + 1
print('O resultado é:',fatorial,)
'''

'''
import random
numero = random.randint(1,100)
numero_esc = -1
tentativas = 1
while numero != numero_esc:
    numero_esc = int(input('Digite um número:'))
    if(numero_esc == numero):
        print('Acertou!''E precisou de',tentativas, 'tentativas')

    elif numero < numero_esc:
        print('Errou, o número era menor')

    else:
        print('Errou, o número era maior')
    tentativas = tentativas + 1
'''

from colorama import Fore, Style, init
print(f"{Fore.RED}Este texto é vermelho!")
print('teste')

print(f"{Fore.GREEN}Este texto é verde!")
print('teste')

print(f"{Fore.BLUE}Este texto é azul!")
print('teste')

print(f"{Fore.YELLOW}Este texto é amarelo!")
print('teste')