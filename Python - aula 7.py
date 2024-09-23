'''
class biblioteca:
    def __init__ (self, livro, estante):
        self.livro = livro
        self.estante = estante
    def pegarLivroEmprestado(self):
        print('Foi pego o', self.livro)

    def pegarLivroNaEstante(self):
        print('Peguei o', self.livro, 'na estante' ,self.estante)

biblioteca1 = biblioteca('Código da Vinci', '2')
biblioteca1.pegarLivroNaEstante()

biblioteca2 = biblioteca('O Herói Perdido','7')
biblioteca2.pegarLivroEmprestado()


class pessoa:
    def __init__  (self, rg, cpf, compro_res, nome, idade):
        self.rg = rg
        self.cpf = cpf
        self.compro_res = compro_res
        self.nome = nome
        self.idade = idade
    def estudar(self):
        print(self.nome,'está estudando')

class aluno(pessoa):
    def __init__ (self, rg, cpf, compro_res, nome, idade, notas):
        super(). __init__ ( rg, cpf, compro_res, nome, idade)
        self.notas = notas
    def fazerProva(self):
        print('O aluno', self.nome, 'está fazendo prova')

    def verNota(self):
        print('O aluno',self.nome, 'tirou',self.notas,)

aluno1 = aluno('123','456','Rua Etc','Giovane','22 anos','9')
aluno1.fazerProva()

aluno2 = aluno('123','456','Rua Etc','Giovane','22 anos','9')
aluno2.verNota()


class professor(pessoa):
    def __init__ (self, rg, cpf, compro_res, nome, idade, correcao, aula):
        super(). __init__ ( rg, cpf, compro_res, nome, idade)
        self.correcao = correcao
        self.aula = aula

    def fazerCorrecao(self):
        print('O professor está fazendo as correções das' ,self.correcao, 'provas')
    def darAula(self):
        print('O professor está dando aula de',self.aula,)

prof1 = professor('123','456','Rua Etc','Giovane','32 anos','7','9')
prof1.fazerCorrecao

prof2 = professor('123','456','Rua Etc','Giovane','32 anos','7','9')
prof2.darAula

class contaBancaria:
    def __init__ (self,titular, saldo,):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print('Deposito realizado')
        else:
            print('Valor inválido')

    def sacar(self, valor):
        if valor < 0:
            print('Valor inválido')

        elif valor <= self.saldo:
            self.saldo = self.saldo - valor
            print('Saque realizado')
        else:
            print('Saldo Insuficiente')

    def mostrarSaldo(self):
        print('O saldo do usúario:',self.titular,'é de:',self.saldo,)

cb1= contaBancaria('Giovane',6050)
cb1.depositar(11)

cb2= contaBancaria('Giovane',6050)
cb2.sacar(11)

cb3= contaBancaria('Giovane',6050)
cb3.mostrarSaldo()
'''

'''
import tkinter as paluco
from tkinter import font

tela = paluco.Tk()
tela.title("Giovane Paluco - Phyton")
tela.geometry('700x300')


fonte = font.Font(family= "Algerian", size= 24)
fonte1 = font.Font(family= "Gigi", size= 24)
fonte2 = font.Font(family= "BankGothic Md BT", size= 24)
fonte3 = font.Font(family= "Bodoni MT Black", size= 24)

label = paluco.Label(tela, text='Meu primeiro programa front-end em Phyton', font=fonte)
label.pack(pady=30)

label = paluco.Label(tela, text='Meu primeiro programa front-end em Phyton', font=fonte1)
label.pack(pady=30)

label = paluco.Label(tela, text='Meu primeiro programa front-end em Phyton', font=fonte2)
label.pack(pady=30)

label = paluco.Label(tela, text='Meu primeiro programa front-end em Phyton', font=fonte3)
label.pack(pady=30)

botao = paluco.Button(tela, text="Entrar")
botao.pack(pady=30)

caixaTexto = paluco.Entry(tela,)
caixaTexto.pack(pady=30)
'''

import tkinter as paluco
from tkinter import font

tela = paluco.Tk()
tela.title("Giovane Paluco - Phyton")
tela.geometry('700x300')

fonte = font.Font(family= "Algerian", size= 24)

label = paluco.Label(tela, text='Nome:', font=fonte)
label.pack()

caixaTextoNome = paluco.Entry(tela,)
caixaTextoNome.pack(pady=30)

label = paluco.Label(tela, text='Sobrenome:', font=fonte)
label.pack()

caixaTextoSobrenome = paluco.Entry(tela,)
caixaTextoSobrenome.pack(pady=30)

def nomeSobrenomeClick():
    nome = caixaTextoNome.get()
    sobrenome = caixaTextoSobrenome.get()
    labelNomeSobrenome.config(text="Seu nome é:" " " + nome + " " + sobrenome)

botao = paluco.Button(tela, text="Entrar", command=nomeSobrenomeClick)
botao.pack(pady=10)

labelNomeSobrenome = paluco.Label(tela, text='')
labelNomeSobrenome.pack(pady=30)

tela.mainloop()