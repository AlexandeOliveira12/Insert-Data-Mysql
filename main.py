import mysql.connector
from tkinter import *
from decouple import config

def inserir():
    myconnection = mysql.connector.connect(host=config("localhost"), user='root', password=config("password"), database=config("database"))

    i = int(idade.get())
    n = str(Nome.get())    

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
janela.title("query tools")

Nome1 = Label(janela, text="insira seu nome aqui aqui: ")
Nome1.grid(column=0, row=0)

Nome = Entry(janela, width=50)
Nome.grid(column=0, row=1)

idade1 = Label(janela, text="insira sua idade aqui:")
idade1.grid(column=0, row=2)

idade = Entry(janela, width=50)
idade.grid(column=0, row=3)

botao = Button(janela, text="Inserir dados", command=inserir)
botao.grid(column=0, row=4)

janela.mainloop()        