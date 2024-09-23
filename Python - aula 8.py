
'''
import tkinter as paluco
from tkinter import font

tela = paluco.Tk()
tela.title("Giovane Paluco - Phyton")
tela.geometry('1920x1080')


botao = paluco.Button(tela, text='Parabéns Gustavo <3')
botao.pack(pady=5)

caixaTexto = paluco.Entry(tela,)
caixaTexto.pack(pady=5)

caixaMultilinha = paluco.Text(tela, height=30, width=70)
caixaMultilinha.pack(pady=5)

caixaSelecao = paluco.Checkbutton(tela,)
caixaSelecao.pack(pady=5)

caixaOpcao = paluco.Radiobutton(tela,)
caixaOpcao.pack(pady=5)

tela.mainloop()
'''


import tkinter as paluco
from PIL import Image
import requests
from io import BytesIO

def pegaImagemNet(linkImagem):
    respostaSite = requests.get(linkImagem)
    imagemSite = BytesIO(respostaSite.content)
    imagem = Image.open(imagemSite)
    imagem = imagem.convert('RGB')
    return imagem

def converterImagem(imagem):
    with BytesIO() as output:
        imagem.save(output, format='PPM')
        ppmImagem = output.getvalue()
    return ppmImagem

def abrirImagem1(imgUrl):
    novaImg = pegaImagemNet(imgUrl)
    novaImgPPM = converterImagem(novaImg)
    novaImg = paluco.PhotoImage(data=novaImgPPM)
    canvas.itemconfig(imgCanvas, image=novaImg)

    canvas.image = novaImg

def bosch():
    imgUrl1 = "https://blog.coremma.com.br/wp-content/uploads/2023/02/bosch-ferramentas-produtos-empresa-linha-bosch12v-bosch18v-01-1-1140x624.png"
    abrirImagem1(imgUrl1)

def palmeiras():
    imgUrl2 ="https://www.palmeiras.com.br/wp-content/uploads/2018/12/palmeiras.png"
    abrirImagem1(imgUrl2)

def pikachu():
    imgUrl3 ="https://cdn.ome.lt/qkNrBaOPl8HvDqdathCGHwkJeuE=/987x0/smart/uploads/conteudo/fotos/pikachu.jfif"
    abrirImagem1(imgUrl3)

def naruto():
    imgUrl4 ="https://wallpapers.com/images/high/kurama-mode-naruto-and-sasuke-susano-gzayxfgjty4c5n5q.webp"
    abrirImagem1(imgUrl4)

def blu():
    imgUrl4 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRa9QlFAUg3dJ2m3vGR_rtrESohiOjgQ7gCg&s"
    abrirImagem1(imgUrl4)

def blu2():
    imgUrl4 = "https: // encrypted - tbn0.gstatic.com / images?q = tbn:ANd9GcSR6G1l2K3n_qFIa0EYHU - k8l64s40mqIVIeg & s"
    abrirImagem1(imgUrl4)

def blu3():
    imgUrl4 = "https://pm1.aminoapps.com/6378/ab4499c7314f4647b2fc5eb68a48c6e138785740_hq.jpg"
    abrirImagem1(imgUrl4)

def pauli():
    imgUrl4 = "https://i.ytimg.com/vi/-7hgCYE63mA/maxresdefault.jpg"
    abrirImagem1(imgUrl4)


imgUrl = "https://s2-oglobo.glbimg.com/JQSyHzUamTXCU4IQYcjPExg05o0=/0x0:571x536/888x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_da025474c0c44edd99332dddb09cabe8/internal_photos/bs/2022/B/R/sXvEbjQDap6m1Or0eSTA/sabrina.png"
imagem1 = pegaImagemNet(imgUrl)


tela = paluco.Tk()
tela.title('Giovane Paluco - Phyton')
canvas = paluco.Canvas(tela, width=1366, height=766)
canvas.pack()

imagem = pegaImagemNet(imgUrl)
imagemPPM = converterImagem(imagem)
imagem = paluco.PhotoImage(data=imagemPPM)

imgCanvas = canvas.create_image(600, 300,image=imagem)

menuBar = paluco.Menu(tela)
tela.config(menu=menuBar)

fileMenu = paluco.Menu(menuBar, tearoff=2)
menuBar.add_cascade(label='Imagem', menu=fileMenu)
fileMenu.add_command(label='Imagem1', command=bosch)
fileMenu.add_command(label='Imagem2', command=palmeiras)
fileMenu.add_command(label='Imagem3', command=pikachu)
fileMenu.add_command(label='Imagem4', command=naruto)
fileMenu.add_command(label='Imagem5', command=blu)
fileMenu.add_command(label='Imagem6', command=blu2)
fileMenu.add_command(label='Imagem7', command=blu3)
fileMenu.add_command(label='Imagem8', command=pauli)

tela.mainloop()
'''
def hello():
    print('Olá')

tela = paluco.Tk()
tela.title('Giovane Paluco - Phyton')
canvas =paluco.Canvas(tela, width=200, height=200)
canvas.pack()
canvas.create_line(0,0,200,200)


listbox = paluco.Listbox(tela)
listbox.pack()
listbox.insert(paluco.END, "Item 1")
listbox.insert(paluco.END, "Item 2")

menuBar = paluco.Menu(tela)
tela.config(menu=menuBar)

fileMenu = paluco.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Arquivo', menu=fileMenu)
fileMenu.add_command(label='Saudar', command= hello)
fileMenu.add_command(label='Link', command= hello)
fileMenu.add_command(label='Opções', command= hello)
fileMenu.add_command(label='Abrir', command= hello)


tela.mainloop()
'''
