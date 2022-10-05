import mysql.connector
from tkinter import *
from tkinter import messagebox
from decouple import config

    

#Função de inserção de dados
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
    
    Text1 = Label(janelaConta, text="""Esta é uma versão de teste, erros serão corrigidos o mais rapido possivel, por favor, 
                                       se achar algum bug, nos reporte no instagram: 
                                       @xandin_robert""")
    Text1.grid(column=0, row=1)
    
    
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