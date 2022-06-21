from tkinter import *
from tkinter import ttk

app=Tk()
app.geometry('810x300')

tree=ttk.Treeview(app)
tree['columns']=('Nombre','Email','Celular')

tree.column('#0')
tree.column('Nombre')
tree.column('Email')
tree.column('Celular')

tree.heading('#0',text='id')
tree.heading('Nombre',text='Nombre')
tree.heading('Email',text='Email')
tree.heading('Celular',text='Celular')

tree.grid(row=0,column=0)

#insertar datos
tree.insert('',END,'1',values=('cesar mayta','cesar@gmail.com','123456789'),text='01')


app.mainloop()