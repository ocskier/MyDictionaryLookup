import tkinter, json
from tkinter.constants import END
from tkinter.scrolledtext import ScrolledText
from db.controller import find,create,end

window = tkinter.Tk()

e1Val = tkinter.StringVar()

def runSearch():
    queryTerm = e1Val.get()
    if queryTerm.strip():
        data = find(queryTerm)
        print(data)
        e1.delete(0,END)
        s1.delete('1.0',END)
        for i in data:
            print(i[2])
            s1.insert('1.0', i[2])

def addEntry():
    newExp = e1.get()
    newDef = s1.get('1.0',END)
    if newExp.strip() and newDef.strip():
        data = create(newExp,newDef)
        print("""Added {exp} to the db! New row id is {id}""".format(id=data, exp=newExp))
        e1.delete(0,END)
        s1.delete('1.0',END)

def updateEntry():
    print('updating something in db')

def deleteEntry():
    print('deleting something from db')

def close():
    end()
    window.destroy()

l1 = tkinter.Label(window, text='Word: ')
l1.grid(row=0,column=0)

e1 = tkinter.Entry(window, textvariable=e1Val, width=30)
e1.grid(row=0,column=1)

b1 = tkinter.Button(window, text="Search",command=runSearch, width=20)
b1.grid(row=0,column=2)

b2 = tkinter.Button(window, text="Add",command=addEntry, width=20)
b2.grid(row=1,column=2)

b3 = tkinter.Button(window, text="Update",command=updateEntry, width=20)
b3.grid(row=2,column=2)

b4 = tkinter.Button(window, text="Delete",command=deleteEntry, width=20)
b4.grid(row=3,column=2)

b5 = tkinter.Button(window, text="Close",command=close, width=20)
b5.grid(row=4,column=2)

s1 = ScrolledText(window, width=50, height=5)
s1.grid(row=1,column=0, rowspan=3)

window.mainloop()



