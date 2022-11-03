#Banco de dados
import mysql.connector

#notificações e interface
from win10toast import ToastNotifier
from tkinter import *
from tkinter import messagebox

#segurança
from decouple import config

#Função de inserção de dados e segunda tela
def InserirDados():
    
    #Registrando Login
    myconnection = mysql.connector.connect(host=config("localhost"), user='root', password=config("password"), database=config("database"))
     
    Idade = int(idade.get())
    name = str(Nome.get())
    
    MsgBox = messagebox.askquestion ('Salvar dados','Deseja salvar esses dados?',icon = 'question')

    if MsgBox == 'yes':
       JanelaLogin.destroy()
       
    cursor = myconnection.cursor()
    sql = "INSERT INTO logins(nome, idade) VALUE (%s, %s)"
    value = [
    (name, Idade)
    ]
    cursor.executemany(sql, value)
    myconnection.commit()
    print(cursor.rowcount, "Registros inseridos")

    if myconnection.is_connected(): 
        cursor.close()
        myconnection.close()
        print("Conexao ao MySql foi encerrada") 
    


    # Inicializa #
    toaster = ToastNotifier()

    # Passa parâmetros e mostra a notificação #
    toaster.show_toast(
    "Notificação de Login", 
    f"Seja bem vindo {name}", 
    threaded=False, 
    icon_path=None, 
    duration=10 # 3 segundos
 )             
       
    #Exibindo conta e cotações
    janelaConta = Tk()
    janelaConta.geometry("455x250")
    janelaConta.title("Cotação atual das moedas")
    
    Saudacao = Label(janelaConta, text=f"Seja bem vindo: {name}" )
    Saudacao.grid(column=0, row=0)
    
    Text1 = Label(janelaConta, text="")
    Text1.grid(column=0, row=1)
    
    janelaConta.mainloop()

    
#Janela de Login
JanelaLogin = Tk()
JanelaLogin.geometry("240x150")
JanelaLogin.title("Login")

Nome1 = Label(JanelaLogin, text="insira seu nome aqui aqui: ")
Nome1.grid(column=0, row=0)

Nome = Entry(JanelaLogin, width=40)
Nome.grid(column=0, row=1)

idade1 = Label(JanelaLogin, text="\ninsira sua idade aqui:")
idade1.grid(column=0, row=2)

idade = Entry(JanelaLogin, width=40)
idade.grid(column=0, row=3)

botao = Button(JanelaLogin, text="Inserir dados", command=InserirDados)
botao.grid(column=0, row=4)

JanelaLogin.mainloop()        
