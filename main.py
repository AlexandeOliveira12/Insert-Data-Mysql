import mysql.connector
from tkinter import *
from tkinter import messagebox
from decouple import config

    

#Função de inserção de dados
def InserirDados():
    myconnection = mysql.connector.connect(host=config("localhost"), user='root', password=config("password"), database=config("database"))
     
    i = int(idade.get())
    n = str(Nome.get()) 

    MsgBox = messagebox.askquestion ('Salvar dados','Deseja salvar esses dados?',icon = 'question')

    if MsgBox == 'yes':
       JanelaLogin.destroy()
        
    cursor = myconnection.cursor()
    sql = "INSERT INTO logins(nome, idade) VALUE (%s, %s)"
    val = [
    (n, i)
    ]
    cursor.executemany(sql, val)
    myconnection.commit()
    print(cursor.rowcount, "Registros inseridos")

    if myconnection.is_connected(): 
        cursor.close()
        myconnection.close()
        print("Conexao ao MySql foi encerrada")      
        
     
      
        
def Janela2():
    janelaConta = Tk()
    janelaConta.geometry("240x150")
    janelaConta.title("Conta")
    
    i = int(idade.get())
    n = str(Nome.get())
    
    Saudacao = Label(janelaConta, text="Seja bem vindo" + n + i)
    Saudacao.grid(column=0, row=0)
    
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

botao = Button(JanelaLogin, text="Inserir dados", command=lambda:[InserirDados(), Janela2()])
botao.grid(column=0, row=4)

JanelaLogin.mainloop()        