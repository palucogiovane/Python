'''
import tkinter as paluco
from PIL import Image
import requests
from io import BytesIO

tela = paluco.Tk()
tela.title('Giovane Paluco - Phyton')
canvas = paluco.Canvas(tela, width=800, height=800)
canvas.pack()

#   Eventos com o Teclado
def Onkey(loc):
        print("Tecla pressionada:", loc.char, "Shift",)

tela.bind("<KeyPress>",Onkey)


# Eventos com o Mouse
def onClick(loc):
    print('Clique detectado em:',loc.x, loc.y)

# tela.bind("<MouseWheel>", onClick)
# tela.bind("<Button-1>", onClick)
# tela.bind("<Button-2>", onClick)
# tela.bind("<Button-3l>", onClick)
# tela.bind("<<ButtonRelease-1>", onClick)
# tela.bind("<Enter>", onClick)
# tela.bind("<Leave>", onClick)
# tela.bind("<Motion>", onClick)


tela.mainloop()
'''


import tkinter as paluco

tela = paluco.Tk()
tela.title('Giovane Paluco - Phyton')
canvas = paluco.Canvas(tela, width=190, height=180)
canvas.pack()

label = paluco.Label(tela, text='Vazio', font=60)
label.pack()
def onClick (loc):
    print('Clique em:', loc.x, loc.y)
    novoTexto = "A coordenada é:" " " + str(loc.x) + " " + str(loc.y)
    label.config(text=novoTexto)

tela.bind("<Motion>", onClick)

tela.mainloop()
