import tkinter as tk
from tkinter import ttk
import sqlite3

database= sqlite3.connect("candidate.db")
cursor=database.cursor()
cursor.execute("DROP TABLE CANDIDATE")
cursor.execute('''CREATE TABLE CANDIDATE (
                NAME    TEXT    NOT NULL,
                GROUPNAME   TEXT    NOT NULL,
                VOTES   INT     NOT NULL
               );''')

gui =tk.Tk()
gui.title("Candidate Registeration")
gui.geometry('300x250+50+50')

register=tk.Frame(gui)
register.pack()

def registery():
    cursor.execute(f"INSERT INTO CANDIDATE(NAME,GROUP,VOTES) \ VALUES({name.get},{group.get},0)")
    name.set("")
    group.set("")

name=tk.StringVar()
namelabel=ttk.Label(register,text="Candidate Name")
namefield=ttk.Entry(register,textvariable=name)
namelabel.pack(ipady=15)
namefield.pack(fill='x',pady=10)
namefield.focus()

group=tk.StringVar()
grouplabel=ttk.Label(register,text="Group Name (- if none)")
groupfield=ttk.Entry(register,textvariable=group)
grouplabel.pack(ipady=15)
groupfield.pack(fill='x',pady=10)
groupfield.focus()

registerbutton=ttk.Button(register,text="Register", command=registery)
registerbutton.pack(pady=15)

gui.mainloop()