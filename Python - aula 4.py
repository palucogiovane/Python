'''
a = float(input('Digite um número:'))
b = float(input('Digite um número:'))

resultado = a + b
print('O resultado é:',resultado,)
'''

'''
a = float(input('Digite um número:'))
b = float(input('Digite um número:'))
c = float(input('Digite um número:'))
d = float(input('Digite um número:'))

resultado = (a * b) - (c / d)
print('O resultado é:',resultado,)

x = float(input('Digite o número 10:'))
y = float(input('Digite o número 3:'))
z = float(input('Digite o número 8:'))
w = float(input('Digite o número 2:'))

resultado = (x * y) - (z / w)
print('O resultado é:',resultado,)
'''

'''
valor1 = int(input('Digite um valor:'))
valor2 = int(input('Digite um valor:'))

if(valor1 > 3) or (valor2 < 4):
    print('Verdadeiro')

else:
    print('Falso')
'''

'''
#IMC
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

elif(IMC >= 35) and (IMC <= 39.9):
    print(f"{Fore.RED}Obesidade mórbida - GRAU I")

else:
    print(f"{Fore.RED}Obesidade mórbida - GRAU II")
'''

'''
a = float(input('Digite um número:'))

resultado = a ** (1/3)
print('O resultado da raiz cúbica de' ,a, 'é:',resultado,)
'''

'''
#Juros Compostos
capital = float(input('Digite o valor do capital:'))
taxaJuros = float(input('Digite o valor da taxa de juros:'))
anos = float(input('Digite a quantidade de tempo (anos):'))

montante = capital * (1+taxaJuros/100) ** anos
print('O valor da montante no final de',anos,'ano(s) é de' ,montante,)
'''

'''
#Voto Obrigatorio, Facultativo ou Não Eleitor
idade = int(input('Digite sua idade:'))

if(idade < 16):
    print('Sua idade é de',idade, ', portanto NÃO ELEGÍVEL para votar')

elif(idade == 16) or (idade == 17):
    print('Sua idade é de',idade,', portanto seu voto é FACULTATIVO')

elif(idade >= 18) and (idade <= 70):
    print('Sua idade é de',idade, ', portanto seu voto é OBRIGATÓRIO')

else:
    print('Sua idade é de',idade, ', portanto seu voto é FACULTATIVO')
'''

'''
hora = int(input('Digite a hora:'))
minuto = int(input('Digite os minutos:'))
segundo = int(input('Digite os segundos:'))

if(hora >= 0) and (hora < 24) and (minuto <= 59) and (segundo <= 59):
    print('A hora é igual a:',hora,':',minuto,':',segundo,'.Portanto É UM HORÁRIO VÁLIDO.')

else:
    print('A hora é igual a:',hora,':',minuto,':',segundo,'.Portanto NÃO É UM HORÁRIO VÁLIDO.')
'''


qtdProdutos = int(input('Digite a quantidade de produtos:'))
valorUnidade = float(input('Digite o valor de cada unidade:'))

if (qtdProdutos >= 100):
    desconto = 0.1

else:
    desconto = 0.05

descontoUnidade = valorUnidade * desconto
valorFinal = descontoUnidade * qtdProdutos
valorCompraSemDesconto = qtdProdutos * valorUnidade
ValorFinal2 = valorCompraSemDesconto - valorFinal


print('A quantidade de produtos solicitadas é:',qtdProdutos,)
print('O valor de cada produto é:',valorUnidade,)
print('O desconto por unidade é:',descontoUnidade,)
print('O valor total de desconto é:',valorFinal,)
print('O desconto aplicado é de:',valorCompraSemDesconto,)
print('O valor final da compra com desconto é:',ValorFinal2,)
