from tkinter import*
from tkinter import ttk 
from tkinter import messagebox

root=Tk()
root.title("Creating GUI elements")
root.geometry("900x600")
gui_elements=["dropdown","label","button"]
dropdown_gui=ttk.Combobox(root,state="readonly",values=gui_elements)
dropdown_gui.pack()
class createelements:
    def __init__(self):
        print("this is a class create elements")
    def createdropdown(self):
        list1=[1,2,3,4]
        dropdown1=ttk.Combobox(root,state="readonly",values=list1)
        dropdown1.pack()
    def createlabel(self):
        label1=Label(root,text="a new label is being created using this class",fg="red")
        label1.pack()
    def createbutton(self):
        button1=Button(root,text="button",command=self.showmessage)
        button1.pack()
    def showmessage(self):
        messagebox.showinfo("message","this button is created using class")
    
        
    def choose(self):
        global dropdown_gui
        element=dropdown_gui.get()
        if element=="dropdown":
            self.createdropdown()
        elif element=="label":
            self.createlabel()
        elif element=="button":
            self.createbutton()
obj_of_element=createelements()    
button2=Button(root,text="create element",command=obj_of_element.choose)     
button2.pack()       
        
root.mainloop()