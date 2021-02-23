import mysql.connector
from mysql.connector import errorcode
import tkinter, json
from tkinter.constants import END
from tkinter.scrolledtext import ScrolledText
from db.controller import Database

window = tkinter.Tk()
db = Database()

nameSearchVal = tkinter.StringVar()
newNameVal = tkinter.StringVar()
newGenreVal = tkinter.StringVar()
newPlatformVal = tkinter.StringVar()

def runSearch():
    queryTerm = nameSearchVal.get()
    if queryTerm.strip():
        try: 
            data = db.find(queryTerm)
            nameSearch.delete(0,END)
            infoBox.delete('1.0',END)
            for i in data:
                infoBox.insert('1.0', i[1] + '\n')
        except mysql.connector.Error as err:
            print(err)

def addEntry():
    name = newNameVal.get()
    genre = newGenreVal.get()
    platform = newPlatformVal.get()
    if name.strip() and genre.strip() and platform.strip():
        try:
            data = db.create(name,genre,platform)
            print("""Added {name} to the db! New row id is {id}""".format(id=data, name=name))
            newName.delete(0,END)
            newGenre.delete(0,END)
            newPlatform.delete(0,END)
        except mysql.connector.Error as err:
            print(err)

def updateEntry():
    # oldExp = nameSearch.get()
    # newExp = "dude"
    # newDef = infoBox.get('1.0',END).rstrip()
    # if newExp.strip() and newDef.strip():
    #   try:
    #       data = update(oldExp,(newExp,newDef))
    #       print(data)
    #       if(data):
    #           print("""Updated {exp} to the db! New definition is {defn}""".format(exp=oldExp, defn=newDef))
    #       nameSearch.delete(0,END)
    #       infoBox.delete('1.0',END)
    #   except mysql.connector.Error as err:
    #       print(err)
    print('Still working on update!')

def deleteEntry():
    print('deleting something from db')

def close():
    db.end()
    window.destroy()

searchLabel = tkinter.Label(window, text='Search for game: ')
searchLabel.grid(row=0,column=0)

nameSearch = tkinter.Entry(window, textvariable=nameSearchVal, width=30)
nameSearch.grid(row=0,column=1)

searchBtn = tkinter.Button(window, text="Search",command=runSearch, width=20)
searchBtn.grid(row=0,column=2)

addBtn = tkinter.Button(window, text="Add",command=addEntry, width=20)
addBtn.grid(row=1,column=2)

updateBtn = tkinter.Button(window, text="Update",command=updateEntry, width=20)
updateBtn.grid(row=2,column=2)

deleteBtn = tkinter.Button(window, text="Delete",command=deleteEntry, width=20)
deleteBtn.grid(row=3,column=2)

closeBtn = tkinter.Button(window, text="Close",command=close, width=20)
closeBtn.grid(row=4,column=2)

infoBox = ScrolledText(window, width=50, height=5)
infoBox.grid(row=1,column=1, rowspan=3)

addLabel = tkinter.Label(window, text="Add a new game:", padx=10, justify="center")
addLabel.grid(row=5, column=1)

newNameLabel = tkinter.Label(window, text='Name: ')
newNameLabel.grid(row=6,column=0)

newName = tkinter.Entry(window, textvariable=newNameVal, width=30)
newName.grid(row=6,column=1)

newGenreLabel = tkinter.Label(window, text='Genre: ')
newGenreLabel.grid(row=7,column=0)

newGenre = tkinter.Entry(window, textvariable=newGenreVal, width=30)
newGenre.grid(row=7,column=1)

newPlatformLabel = tkinter.Label(window, text='Platform: ')
newPlatformLabel.grid(row=8,column=0)

newPlatform = tkinter.Entry(window, textvariable=newPlatformVal, width=30)
newPlatform.grid(row=8,column=1)

window.mainloop()



