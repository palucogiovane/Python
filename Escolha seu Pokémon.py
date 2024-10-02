import tkinter as paluco
import requests
from PIL import Image
from io import BytesIO
from tkinter import ttk
from colorama import Fore, Style, init

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

def pegarPokemon(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    qualPokemon = requests.get(url)
    qualPokemon = qualPokemon.json()
    imagem = qualPokemon['sprites']['front_default']
    return imagem

def pokemon():
    nomePokemon = texto.get()
    imgUrl = pegarPokemon(nomePokemon)
    abrirImagem1(imgUrl)

def buscarPokemon():
    Url = "https://pokeapi.co/api/v2/pokemon?limit=10000"
    listaPokemon = requests.get(Url)
    listaPokemon = listaPokemon.json()
    pokemons = listaPokemon['results']
    pokedex = []
    for pokemon in pokemons:
        pokedex.append(pokemon['name'])
    return pokedex

def pokemonCombobox(event):
    nomePokemon = pc.get()
    Url = pegarPokemon(nomePokemon)
    abrirImagem1(Url)


tela = paluco.Tk()
tela.title('Quem é esse Pokémon?')
tela.configure(background='red')

label = paluco.Label(text='Quem é esse Pokémon?')
label.configure(background='white')
label.pack(pady=10)

canvas = paluco.Canvas(tela, width=500, height=500)
canvas.pack(pady=10)
imgCanvas = canvas.create_image(250, 200)

texto = paluco.Entry(tela,)
texto.pack(pady=10)
texto.configure(background='white')

pokedex = buscarPokemon()
pc = ttk.Combobox(tela, values=pokedex)
pc.bind("<<ComboboxSelected>>", pokemonCombobox)
pc.pack()



botao = paluco.Button(tela,text="Carregar Pokémon", command=pokemon)


tela.mainloop()


