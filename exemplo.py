from tkinter import *
from PIL import Image, ImageTk  # Pillow para trabalhar com imagens

cor1 = "#6495ED"  # azul

# Função para exibir GIF animado
def atualizar_gif(ind):
    frame = frames[ind]
    l_logo.configure(image=frame)  # Atualiza o frame no Label
    ind += 1
    if ind == frame_count:  # Reinicia o GIF quando chegar ao último frame
        ind = 0
    janela.after(100, atualizar_gif, ind)  # Atualiza a cada 100ms
    l_logo.place(x=250, y=250)  # Atualiza a posição do Label

# Criar a janela principal
janela = Tk()
janela.title("ABA PSICOLOGIA")
janela.geometry("1000x1000")
janela.config(bg=cor1)

# Carregar o ícone da janela
janela.iconphoto(False, PhotoImage(file="frank ocean.gif"))

# Tornar a janela não redimensionável
janela.resizable(width=True, height=True)

# Carregar o GIF animado com Pillow
gif = Image.open("frank ocean.gif")

# Extrair frames do GIF
frames = []
frame_count = gif.n_frames  # Conta o número de frames no GIF
for i in range(frame_count):
    gif.seek(i)  # Navega pelos frames do GIF
    frame = ImageTk.PhotoImage(gif.copy())  # Copia o frame atual
    frames.append(frame)

# Criar um Label para exibir o GIF
l_logo = Label(janela)
l_logo.place(x=250, y=250)  # Adiciona o Label à janela

# Iniciar a animação do GIF
janela.after(0, atualizar_gif, 0)

botao = Button(janela, text="Exibir Gif", command=lambda: atualizar_gif(0))
botao.grid(column=0, row=0)

# Loop principal da janela
janela.mainloop()
