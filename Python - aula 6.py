
#Calculadora
'''
def soma (numero1,numero2):
    soma1 = numero1 + numero2
    return soma1

def subtracao (numero1,numero2):
    subtracao1 = numero1 - numero2
    return subtracao1

def multiplicacao (numero1,numero2):
    multiplicacao1 = numero1 * numero2
    return multiplicacao1

def divisao (numero1,numero2):
    divisao1 = numero1 / numero2
    return divisao1

def calculadora (numero1,numero2, operacao):
    if  operacao == '+':
        resultado = soma(numero1,numero2)

    elif operacao == '-':
        resultado = subtracao(numero1,numero2)

    elif operacao == '*':
        resultado = multiplicacao(numero1,numero2)

    elif operacao == '/':
        resultado = divisao(numero1,numero2)

    else:
        print('Operação inválida')
    return resultado

while True:
        print('Calculadora')
        print('---------------------')
        numero1 = float(input('Digite um número:'))
        numero2 = float(input('Digite um número:'))
        operacao = input('Digite uma operação entre (+ , - , * , /):')
        calculo =  calculadora (numero1, numero2, operacao)
        print('O resultado é:',calculo)
        print('-*-*-*-*-*-*-*-*-*-*-')
'''

'''
minhaLista = [1,2,3,4,5,6,7,8,9,10]
minhaLista.append(11)
minhaLista.append(12)
minhaLista.append(13)
minhaLista.append(14)
minhaLista.append(15)
minhaLista.append(16)
minhaLista.append(17)
print(minhaLista)'''

'''
minhaTuplaMista = (1, 'Giovane' , 'cimento')
segundoElemento = minhaTuplaMista[1]
print(segundoElemento)
'''

'''
minhaListaMista = [37, 35.01559273106729, 'x6Fhj', False, 17, 47.292571, 'JRwbluF6Ux', True, 98, 1.86432]
minhaListaMista.remove(True)
print(minhaListaMista)
'''
'''
#IMC - Desafio de Lógica
from colorama import Fore, Style, init

peso = float(input('Digite seu peso (kg):'))
altura = float(input('Digite sua altura (metros):'))

IMC = peso / altura**2
print('Seu IMC é:',IMC,)

if(IMC < 18.5):
    print(f"{Fore.BLUE}Baixo Peso")

elif(IMC >= 18.5) and (IMC <= 24.9):
    print(f"{Fore.GREEN}Normal")

elif(IMC >= 25) and (IMC <= 29.9):
    print(f"{Fore.CYAN}Sobrepeso")

elif(IMC >= 30) and (IMC <= 34.9):
    print(f"{Fore.YELLOW}Obesidade")

else:
    print(f"{Fore.RED}Obesidade")
'''



