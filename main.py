#Mysql
import mysql.connector

#Tkinter
from tkinter import *
from tkinter import messagebox

#Notificação
from win10toast import ToastNotifier

#Segurança
from decouple import config

#Busca
import wikipedia

    

#Função de inserção de dados
def InserirDados():
    
    #Registrando Login
    myconnection = mysql.connector.connect(host=config("localhost"), user='root', password=config("password"), database=config("database"))
     
    Idade = int(idade.get())
    name = str(Nome.get())
    

    MsgBox = messagebox.askquestion ('Salvar dados','Deseja salvar esses dados?',icon = 'question')

    if MsgBox == 'yes':
       JanelaLogin.destroy()
       
       toaster = ToastNotifier()
       
       toaster.show_toast(
           "Login Efetuado",
           f"Seja bem vindo {name}!",
           threaded=True,
           icon_path=None,
           duration=5
       )
        
    cursor = myconnection.cursor()
    sql = "INSERT INTO logins(nome, idade) VALUE (%s, %s)"
    val = [
    (name, Idade)
    ]
    cursor.executemany(sql, val)
    myconnection.commit()
    print(cursor.rowcount, "Registros inseridos")

    if myconnection.is_connected(): 
        cursor.close()
        myconnection.close()
        print("Conexao ao MySql foi encerrada")   

    #Exibindo conta
    janelaConta = Tk()
    janelaConta.geometry("455x250")
    janelaConta.title("Conta")
    
    Saudacao = Label(janelaConta, text=f"Seja bem vindo: {name}" )
    Saudacao.grid(column=0, row=0)
    
    Text1 = Label(janelaConta, text="")
    Text1.grid(column=0, row=1)
    
    Text2 = Label(janelaConta, text="O que deseja buscar? (Obs: A busca será feita na wikipedia")
    Text2.grid(column=0, row=2)
    
    TextEntry1 = Entry(janelaConta, width=40)
    TextEntry1.grid(column=0, row=3)
    
    busca = (TextEntry1.get())
    
    result = wikipedia.summary(busca)
    
    TextResultado = Label(janelaConta, text="")
    TextResultado.grid(column=0, row=5)
    
    
    TextResultado["text"] = result
    
    
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

botao = Button(JanelaLogin, text="Inserir dados", command=lambda:[InserirDados()])
botao.grid(column=0, row=4)

JanelaLogin.mainloop()        