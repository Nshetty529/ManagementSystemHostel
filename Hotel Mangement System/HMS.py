
from tkinter import *
from PIL import Image,ImageTk  #module to set image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from tkinter import font
from hotel import HotelManagementSystem
from mysql.connector.locales.eng import client_error


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        # self.root.wm_iconbitmap("logo3.png")
        img = PhotoImage(file="logo3.png")  # Replace "image.png" with any image file.
        self.root.iconphoto(False, img)
        # self.root.config(bg="white")

        self.txtpass1=StringVar()
        self.txtuser1=StringVar()
        self.txtpass=StringVar()
        self.txtuser=StringVar()
        # ====background image======
        img=Image.open(r"C:\Users\HP\Desktop\Project\Hotel Mangement System\images\3.jpg")
        img=img.resize((1550,780),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_bg=Label(self.root,image=self.photoimg)
        lbl_bg.place(x=0,y=0,width=1550,height=780)

        # =====creating center frame ========
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\HP\Desktop\Project\Hotel Mangement System\images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg.place(x=730,y=175,width=100,height=100)

        #========== labels username and password===========
        username=lbl=Label(frame,text="Username:",font=("times new roman",15,"bold"),background="black",foreground="white")
        username.place(x=120,y=155)

        txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",15,"bold"))
        txtuser.place(x=40,y=190,width=270)

        password=lbl=Label(frame,text="Password:",font=("times new roman",15,"bold"),background="black",foreground="white")
        password.place(x=120,y=225)

        txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("times new roman",15,"bold"))
        txtpass.place(x=40,y=260,width=270)

        # =======login button=============
        loginbutton=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="red",activebackground="white")
        loginbutton.place(x=110,y=300,width=120,height=35)

       

        # ==============password====================
        passbutton=Button(frame,text="Forgot Password",command=self.fpass,borderwidth=0,font=("times new roman",10,"bold"),relief=RIDGE,bg="black",fg="white",activebackground="black")
        passbutton.place(x=90,y=380,width=160)

        # ============login button functuon================
    def login(self):
            if self.txtuser.get()=="" or self.txtpass.get()=="":
                messagebox.showerror("Error","All feilds required")
            elif self.txtuser.get()=="Admin" and self.txtpass.get()=="TheHarmonyHostel":
                open_main=messagebox.askyesno("yesno","Are you Admin")
                if open_main>0:
                    self.txtuser.set("")
                    self.txtpass.set("")
                    self.txtpass1.set("")
                    # self.new_window.destroy()
                    messagebox.showinfo("Sucessfull","Logged in as admin")
                    
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                    

                else:
                    if not open_main:
                        
                        return
            else:
                 messagebox.showerror("Error","Invalid username or password")
    def fpass(self):

        newwindow=Toplevel(root)
        newwindow.title("Forgot Password")
        newwindow.geometry("500x500+520+200")

        frame1=Frame(newwindow,bg="black")
        frame1.place(x=0,y=0,width=500,height=500)

        username1=lbl=Label(frame1,text="Question:",font=("times new roman",15,"bold"),background="black",foreground="white")
        username1.place(x=220,y=155)

        Ptxtuser1=Label(frame1,font=("times new roman",15,"bold"),text="What is the Password of cabin",state=DISABLED)
        Ptxtuser1.place(x=80,y=190,width=350)

        password1=lbl=Label(frame1,text="Answer",font=("times new roman",15,"bold"),background="black",foreground="white")
        password1.place(x=220,y=225)

        Ptxtpass1=ttk.Entry(frame1,textvariable=self.txtpass1,font=("times new roman",15,"bold"))
        Ptxtpass1.place(x=55,y=260,width=400)

         # =======check button=============
        loginbutton=Button(frame1,text="Check",font=("times new roman",15,"bold"),command=self.check,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="red",activebackground="white")
        loginbutton.place(x=200,y=350,width=120,height=35)

    def check(self):
        
         if  self.txtpass1.get()=="":
                messagebox.showerror("Error","All feilds required",parent=self.root)
         
         elif self.txtpass1.get()=="admin12345": 
              
              self.txtuser1.set("The Password is:"),
              self.txtpass1.set("Username:Admin  Password:TheHarmonyHostel")
            #   messagebox.showinfo("Correct","Entered Password is Correct",parent)
         else:
              messagebox.showerror("Error","Wrong Password",parent=self.root)

            




if __name__=="__main__":
    
    root=Tk()
    app=login_window(root)
    root.mainloop()