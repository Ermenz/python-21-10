from tkinter import *
from PIL import Image, ImageTk  # Importar Pillow para trabalhar com imagens

cor1 = "#6495ED"  # azul

# Criar a janela principal
janela = Tk()
janela.title("ABA PSICOLOGIA")
janela.geometry("1000x1000")
janela.config(bg=cor1)

# Carregar o ícone da janela (certifique-se de que o arquivo .gif está no caminho correto)
janela.iconphoto(False, PhotoImage(file="frank ocean.gif"))

# Tornar a janela não redimensionável
janela.resizable(width=False, height=False)

# Carregar a imagem GIF com Pillow
img = Image.open("frank ocean.gif")
img = ImageTk.PhotoImage(img)

# Criar um Label para exibir a imagem
l_logo = Label(janela, image=img)
l_logo.place(x=10, y=10)

# Manter uma referência da imagem para evitar coleta de lixo
l_logo.image = img

# Loop principal da janela
janela.mainloop()
