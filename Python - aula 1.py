'''
mensagem = "oi, Giovane"
numero = 6
pi = 3.14
print(mensagem)
print(numero)
print(pi)
'''

'''#Declarando e atribuindo valores a variáveis
idade = 21
nome = "Giovane"
altura = 1.75

#Exibindo os valores das variáveis
print("Nome:", nome)
print("Idade:", idade)
print("Altura (cm):", altura)'''

'''
#Declarando e atribuindo valores a variáveis
idade = 21
nome = "Giovane"

#Exibindo os valores das variáveis
print("Olá, meu nome é",nome, "e tenho", idade, "anos.")'''

'''
#Declarando e atribuindo valores a variáveis
idade = input("Digite a sua idade:")
nome = input("Digite o seu nome:")

#Exibindo os valores das variáveis
print("Olá, meu nome é",nome, "e tenho", idade, "anos.")'''

'''
#Declarando e atribuindo valores a variáveis
dia = input("Digite o dia de nascimento:")
mes = input ("Digite o mês de nascimento:")
ano = input("Digite o ano de nascimento:")
nome = input ("Digite seu nome:")

#Exibindo os valores das variáveis
print("Olá,",nome,"sua data de nascimento é:",dia,"/",mes,"/",ano,".")'''

'''
#Declarando e atribuindo valores a variáveis
x = float(input("Digite um número:"))
y = float(input("Digite um número:"))
z = float(input("Digite um número:"))
soma = x + y + z
media = (x + y + z) / 3
mult = x * y * z
div = x / y / z

#Exibindo os valores das variáveis
print("Resultado da soma é:", soma,)
print("Resultado da média é:", media)
print("Resultado da multiplicação é:", mult)
print("Resultado da divisão é:", div)'''


print("Bem-vindo ao sistema de gerenciamento de finanças pessoais!")
print("Você irá cadastrar receitas e edespesas, calcular o saldo e gerar um relatório detalhado.")

#Declarando e atribuindo valores a variáveis
receita1 = float(input("Digite um valor para Receita 1:"))
receita2 = float(input("Digite um valor para Receita 2:"))
receita3 = float(input("Digite um valor para Receita 3:"))
despesa1 = float(input("Digite um valor para Despesa 1:"))
despesa2 = float(input("Digite um valor para Despesa 2:"))
despesa3 = float(input("Digite um valor para Despesa 3:"))

soma_receita = receita1 + receita2 + receita3
soma_despesa = despesa1 + despesa2 + despesa3
saldo_final = soma_receita - soma_despesa

per_r1 = receita1 / soma_receita
per_r2 = receita2 / soma_receita
per_r3 = receita3 / soma_receita

per_d1 = despesa1 / soma_despesa
per_d2 = despesa2 / soma_despesa
per_d3 = despesa3 / soma_despesa

#Exibindo os valores das variáveis
print("O resultado das receitas são:",soma_receita,)
print("O resultado das despesas são:",soma_despesa,)
print("O resultado do saldo final é:",saldo_final,)

print("O resultado do percentual da Receita 1 é:",per_r1,)
print("O resultado do percentual da Receita 2 é:",per_r2,)
print("O resultado do percentual da Receita 3 é:",per_r3,)

print("O resultado do percentual da Despesa 1 é:",per_d1,)
print("O resultado do percentual da Despesa 2 é:",per_d2,)
print("O resultado do percentual da Despesa 3 é:",per_d3,)

print("Total das receitas:",soma_receita,)
print("Total das despesas:",soma_despesa,)
print("Saldo final:",saldo_final,)
print("Percentual da Receita 1:",per_r1,)
print("Percentual da Receita 2:",per_r2,)
print("Percentual da Receita 3:",per_r3,)
print("Percentual da Despesa 1:",per_d1,)
print("Percentual da Despesa 2:",per_d2,)
print("Percentual da Despesa 3:",per_d3,)

'''
