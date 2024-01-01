from tkinter import *

janela_cadastro = Tk()
janela_cadastro.title('cadastro')
frame_cabecalho_cadastro = Frame(janela_cadastro)
frame_conteudo_cadastro = Frame(janela_cadastro)
janela_cadastro.geometry('500x300')

# Cabeçalho
texto_orientacao_1 = Label(frame_cabecalho_cadastro, text= 'Faça seu cadastro')
texto_orientacao_1.grid(row=0, column=2, padx=10, pady=17, columnspan=4)

# Conteudo
texto_orientacao_usuario = Label(frame_conteudo_cadastro, text='Digite seu nome de usuário:')
texto_orientacao_usuario.grid(row=1, column=1, padx=5, pady=5, columnspan= 2)
usuario = Entry(frame_conteudo_cadastro)
usuario.grid(row=1, column=3, padx=10, pady=10, columnspan=4)

texto_orientacao_email = Label(frame_conteudo_cadastro, text='Digite o seu Email:')
texto_orientacao_email.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
email = Entry(frame_conteudo_cadastro)
email.grid(row=2, column=3, padx=10, pady=10, columnspan=4)

texto_orientacao_senha = Label(frame_conteudo_cadastro, text='Digite a sua senha:')
texto_orientacao_senha.grid(row=3, column= 1, padx=10, pady=10, columnspan=2)
senha = Entry(frame_conteudo_cadastro)
senha.grid(row=3, column=3, padx=10, pady=10, columnspan=4)

texto_orientacao_senha_2 = Label(frame_conteudo_cadastro, text='Confirme a seua senha:')
texto_orientacao_senha_2.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
confirme_senha = Entry(frame_conteudo_cadastro)
confirme_senha.grid(row=4, column=3, padx=10, pady=10, columnspan=4)

enviar = Button(frame_conteudo_cadastro, text='Enviar')
enviar.grid(row=5, column=2, padx=10, pady=15, columnspan=4)

# Configurações
janela_cadastro.configure(background='black')
frame_cabecalho_cadastro.configure(background='black')
frame_conteudo_cadastro.configure(background='black')
texto_orientacao_1.configure(background='black', foreground='white', font=('Arial Black', 16, 'italic'))
texto_orientacao_usuario.configure(background='black', foreground='white', font=('Times', 12, 'italic'))
texto_orientacao_email.configure(background='black', foreground='white', font=('Times', 12, 'italic'))
texto_orientacao_senha.configure(background='black', foreground='white', font=('Times', 12, 'italic'))
texto_orientacao_senha_2.configure(background='black', foreground='white', font=('Times', 12, 'italic'))


frame_cabecalho_cadastro.pack()
frame_conteudo_cadastro.pack()
Tk.mainloop(janela_cadastro) 