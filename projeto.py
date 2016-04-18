from tkinter import *

class Window(Frame):
    
    def __init__ (self, master = None):
        Frame.__init__(self, master)
        
        self.master = master 
        self.init_window()
        
        
    def init_window(self):
        
        self.master.title("JANELA")
        self.pack(fill = BOTH, expand = 1)
        
        Button1 = Button(self, text = "                              \n\n\n\n\n", command=self.show_txt)
        Button1.place (x=0, y=0)       
        
        Button2 = Button(self, text = "                              \n\n\n\n\n", command = self.client_print)
        Button2.place (x=100, y=0)
        
        Button3 = Button(self, text = "                              \n\n\n\n\n", command = self.client_print)
        Button3.place (x=200, y=0)
        
        Button4 = Button(self, text = "                              \n\n\n\n\n", command = self.client_print)
        Button4.place (x=0, y=100)
        
        Button5 = Button(self, text = "                              \n\n\n\n\n", command = self.client_print)
        Button5.place (x=100, y=100)
        
        Button6 = Button(self, text = "                              \n\n\n\n\n", command = self.client_print)
        Button6.place (x=200, y=100)
        
        Button7 = Button(self, text = "                              \n\n\n\n\n", command = self.client_print)
        Button7.place (x=0, y=200)
        
        Button8 = Button(self, text = "                              \n\n\n\n\n", command = self.client_print)
        Button8.place (x=100, y=200)
        
        Button9 = Button(self, text = "                              \n\n\n\n\n", command = self.client_print)
        Button9.place (x=200, y=200)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        file.add_command(label = "Exit", command = self. client_exit)
        menu.add_cascade(label="File", menu = file)
                
        edit = Menu(menu)
        edit.add_command(label = "Mostrar Texto", command=self.show_txt)
        menu.add_cascade(label="Edit", menu = edit)
        
        
    def show_txt(self):
        count = 0
        if count%2 == "0":
            text = Label(self, text = "O")
            return O
        else:
            text = Label(self, text = "X")
            return X
        text.pack()
    
    def client_exit(self):
        exit()
    
    def client_print(self):
        print ("Eai, DJOW")
    
count = 0

root = Tk ()

root.geometry("300x350")

app = Window(root)

root.mainloop()

        