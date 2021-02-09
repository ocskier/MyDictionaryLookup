import tkinter, json, mysql.connector
from tkinter.constants import END
from mysql.connector import errorcode
from db.connection import connection

cursor = connection.cursor()
queryTerm = "'freon'"
query = """SELECT * FROM Dictionary WHERE Expression={queryTerm}""".format(queryTerm=queryTerm)
try: 
    data = cursor.execute(query)
    for row in cursor:
        print(json.dumps(row, indent=2))
except mysql.connector.Error as err:
    print(err)

window = tkinter.Tk()

e1Val = tkinter.StringVar()

e1 = tkinter.Entry(window, textvariable=e1Val)
e1.grid(row=0,column=0)

t1 = tkinter.Text(window, height=1, width=20)
t1.grid(row=0,column=1)

b1 = tkinter.Button(window, text="Search")
b1.grid(row=0,column=2)

window.mainloop()



