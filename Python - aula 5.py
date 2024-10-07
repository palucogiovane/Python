'''
#Calculo de área de um círculo
def areaCirculo (raio, pi):
    area = pi*raio**2
    return area

raio = float(input('Dgite um raio:'))
pi = 3.14
area = areaCirculo(raio,pi)

print('A área do circulo é:',area,)
'''


#Operações básicas
def soma (a,b):
    soma1 = a + b
    return soma1

def subtracao (a,b):
    subtracao1 = a - b
    return subtracao1

def multiplicacao (a,b):
    multiplicacao1 = a * b
    return multiplicacao1

def divisao (a,b):
    divisao1 = a / b
    return divisao1
''''
a = float(input('Digite um valor:'))
b = float(input('Digite um valor:'))

soma1 = soma (a,b)
subtracao1 = subtracao (a,b)
multiplicacao1 = multiplicacao(a,b)
divisao1 = divisao(a,b)

print('A soma de' ,a, '+' ,b, 'é:',soma1)
print('A subtração entre' ,a, '-' ,b, 'é:',subtracao1)
print('A multiplicação entre' ,a, '*' ,b, 'é:',multiplicacao1)
print('A divisão entre' ,a, '/' ,b, 'é:',divisao1)
'''

'''
#Potência
def potencia (base,expoente):
    resultado = base**expoente
    return resultado

base = int(input('Digite um número para BASE:'))
expoente = int(input('Digite úm número para EXPOENTE:'))

calculo = potencia (base,expoente)
print('Se a BASE é' ,base, 'e o EXPOENTE é',expoente,',o resultado da potência será:',calculo)
'''

'''
#Par ou ímpar
def ehPar (numero):
    resultado = numero/2
    return resultado

numero = int(input('Digite um número:'))

if numero % 2 == 0:
    print('Verdadeiro')

else:
    print('Falso')
'''

'''
#Conversão de temperatura
def farenheitParaCelsius (F):
    calculo = 5/9 * (F-32)
    return calculo

F = float(input('Digite uma temperatura:'))
resultado = farenheitParaCelsius (F)
print('O resultado é:',resultado)
'''

'''
#Sequência Fibonacci
def fibonacci (n):
    a = 0
    b = 1
    for i in range(n):
        auxiliar = a
        a = b
        b = auxiliar + b
    return b
print(fibonacci())
'''
'''
#Fatorial
def fatorial (n):
    fat = 1
    for i in range (n):
        fat = fat * (i + 1)
    return fat
numero = int(input("Digite um número:"))
print(fatorial(numero))
'''

#Calculadora
def calculadora (a,b, operacao):
    if  operacao == '+':
        resultado = soma(a,b)

    elif operacao == '-':
        resultado = subtracao(a,b)

    elif operacao == '*':
        resultado = multiplicacao(a,b)

    else:
        resultado = divisao(a,b)
    return resultado

    while True:
        print('Calculadora')
        print('-----------')
        numero1 = float(input('Digite um número:'))
        numero2 = float(input('Digite um número:'))
        operacao = input('Digite uma operação entre (+ , - , * , /):')
