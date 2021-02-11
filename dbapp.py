import tkinter, json, mysql.connector
from tkinter.constants import END
from tkinter.scrolledtext import ScrolledText
from mysql.connector import errorcode
from db.connection import connection

window = tkinter.Tk()

e1Val = tkinter.StringVar()

def runSearch():
    cursor = connection.cursor()
    queryTerm = """'{input}'""".format(input=e1Val.get())
    print(queryTerm)
    query = """SELECT * FROM Dictionary WHERE Expression={queryTerm}""".format(queryTerm=queryTerm)
    e1.delete(0,END)
    s1.delete('1.0',END)
    try: 
        data = cursor.execute(query)
        for row in cursor:
            s1.insert('1.0', row[1])
    except mysql.connector.Error as err:
        print(err)

l1 = tkinter.Label(window, text='Word: ')
l1.grid(row=0,column=0)

e1 = tkinter.Entry(window, textvariable=e1Val, width=30)
e1.grid(row=0,column=1)

b1 = tkinter.Button(window, text="Search",command=runSearch, width=20)
b1.grid(row=0,column=2)

s1 = ScrolledText(window, width=50, height=5)
s1.grid(row=1,column=0)

window.mainloop()



