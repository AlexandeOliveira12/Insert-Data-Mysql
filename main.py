import mysql.connector
from tkinter import *
from tkinter import messagebox
from decouple import config

def InserirDados():
    myconnection = mysql.connector.connect(host=config("localhost"), user='root', password=config("password"), database=config("database"))

    i = int(idade.get())
    n = str(Nome.get())    

    MsgBox = messagebox.askquestion ('Salvar dados','Deseja salvar esses dados?',icon = 'question')

    if MsgBox == 'yes':
       janela.destroy()
        
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
        
janela = Tk()
janela.geometry("240x150")
janela.title("Login")

Nome1 = Label(janela, text="insira seu nome aqui aqui: ")
Nome1.grid(column=0, row=0)

Nome = Entry(janela, width=40)
Nome.grid(column=0, row=1)

idade1 = Label(janela, text="\ninsira sua idade aqui:")
idade1.grid(column=0, row=2)

idade = Entry(janela, width=40)
idade.grid(column=0, row=3)

botao = Button(janela, text="Inserir dados", command=lambda:[InserirDados()])
botao.grid(column=0, row=4)

janela.mainloop()        