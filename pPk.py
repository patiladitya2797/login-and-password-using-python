from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1199x600")

        Frame_login = Frame(self.root)
        Frame_login.place(x=330, y=150, width=500, height=400)

        title=Label(Frame_login,text="Login Here",font=("Imapact",35,"bold"),fg="#6162FF").place(x=90,y=30)
        lbl_user=Label(Frame_login,text="USERNAME",font=("Imapact",25,"bold"),fg="grey").place(x=90,y=140)
        self.username=Entry(Frame_login,font=("Imapact",25))
        self.username.place(x=90,y=170,width=320,height=35)

        lbl_password = Label(Frame_login, text="Password", font=("Imapact", 25, "bold"), fg="grey").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Imapact", 25))
        self.password.place(x=90, y=240, width=320, height=35)

        forget=Button(Frame_login, text="Forgot Password", font=("Imapact", 10, "bold"), fg="grey").place(x=90, y=280)
        submit=Button(Frame_login,command=self.check_function, text="login", font=("Imapact", 20, "bold"), fg="grey").place(x=90, y=340,width=220,height=60)
        registration=Button(Frame_login, text="registration", font=("Imapact", 15, "bold"), fg="grey").place(x=90, y=300,width=180,height=50)

    def check_function(self):
            if self.username.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","all field are required",parent=self.root)
            elif self.username.get()!="aditya@gmail.com" or self.password.get()!="Aditya2797@":
                messagebox.showerror("Error","Invalid username or password",parent=self.root)
            else:
                messagebox.showinfo("welcome",f"welcome{self.username.get()}")







root=Tk()
object=Login(root)
root.mainloop()