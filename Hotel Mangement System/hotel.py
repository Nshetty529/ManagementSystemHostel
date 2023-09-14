from tkinter import *
from PIL import Image,ImageTk  #module to set image
from customer import Cust_Win
from room import Roombooking
from tkinter import messagebox
import customtkinter
from mysql.connector.locales.eng import client_error

from reports import roomreport

from details import Detailsroom


x=1
class HotelManagementSystem:
    
    # Setting the geometry for the main window
    def __init__(self,root):
        self.root=root
        self.root.title("HOSTEL MANAGEMENT SYSTEM")
        # self.root.attributes("-fullscreen",True)
#         width= self.root.winfo_screenwidth()
#         height= self.root.winfo_screenheight()
# #setting tkinter window size
#         self.root.geometry("%dx%d" % (width, height))
        self.root.geometry("1550x800+0+0")
        # self.root.wm_iconbitmap("logo3.ico")
        img = PhotoImage(file="logo3.png")  # Replace "image.png" with any image file.
        self.root.iconphoto(False, img)
        


        # =======================First image===================
        # r to convert forward slash to backwards
        img1=Image.open(r"C:\Users\HP\Desktop\Project\Hotel Mangement System\images\3.jpg")
        # anitiliasconverts high level image to low level now in new version LANCZOS 
        img1=img1.resize((1528,170),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=SOLID)
        lblimg.place(x=0,y=0,width=1528,height=170)


        # =======================logo===================
        # img2=Image.open(r"C:\Users\HP\Desktop\Project\Hotel Mangement System\images\2.jpg")
        # img2=img2.resize((230,140),Image.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=FLAT)
        # lblimg.place(x=0,y=0,width=230,height=140)


        # =======================title===================
        lbl_title=Label(self.root,text="HARMONY HOSTEL", font=("times new roman",40,"bold"),bg="black",fg="white")
        lbl_title.place(x=300,y=50,width=1000,height=70)


        # ==================main frame================
        main_frame=Frame(self.root,bd=4,relief=FLAT)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # ===========================menu========================
        
    
        # ==================button frame================
        btn_frame=Frame(main_frame,bd=4,relief=FLAT)
        btn_frame.place(x=0,y=100,width=228,height=300)
        
        # lbl_menu=Button(btn_frame,text="MENU", font=("times new roman",25,"bold"),fg="white",bg="black",bd=4,relief=RIDGE)
        # lbl_menu.place(x=0,y=140,width=230)

        menu_btn=Button(btn_frame,text="MENU",width=20,font=("times new roman",14,"bold"),fg="white",bg="black",bd=1)
        menu_btn.grid(row=0,column=0, )
        # grid method to place them all buttons in one column
        # cursor hand so than when hoverd on button it shows different cursor
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=20,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand2")
        cust_btn.grid(row=1,column=0, pady=2, padx=5)

        room_btn=Button(btn_frame,text="BOOKING",command=self.roombooking,width=20,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand2")
        room_btn.grid(row=2,column=0 ,pady=2)

        detail_btn=Button(btn_frame,command=self.report,text="HISTORY",width=20,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand2")
        detail_btn.grid(row=3,column=0, pady=2)

        report_btn=Button(btn_frame,text="ADD BED",command=self.details,width=20,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand2")
        report_btn.grid(row=4,column=0 ,pady=2)

        logout_btn=Button(btn_frame,command=self.logout,text="LOGOUT",width=20,font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,cursor="hand2")
        logout_btn.grid(row=5,column=0 ,pady=2)


        # ==============right side image========================
        img3=Image.open(r"C:\Users\HP\Desktop\Project\Hotel Mangement System\images\1.3.jpg")
        img3=img3.resize((1270,600),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=SOLID)
        lblimg1.place(x=250,y=0,width=1270,height=600)

        # =======================down images=======================
        # img4=Image.open(r"C:\Users\HP\Desktop\Project\Hotel Mangement System\images\myh.jpg")
        # img4=img4.resize((230,210),Image.LANCZOS)
        # self.photoimg4=ImageTk.PhotoImage(img4)

        # lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        # lblimg.place(x=0,y=225,width=230,height=210)
        

        # img5=Image.open(r"C:\Users\HP\Desktop\Project\Hotel Mangement System\images\khana.jpg")
        # img5=img5.resize((230,190),Image.LANCZOS)
        # self.photoimg5=ImageTk.PhotoImage(img5)

        # lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        # lblimg.place(x=0,y=420,width=230,height=190)

    # ===============function for new window to open when clicked on button =========================

    
    def cust_details(self):    
        try:
            if(self.new_window.winfo_exists()):
                self.new_window.destroy()
                self.new_window=Toplevel(self.root)
                self.app=Cust_Win(self.new_window)       
        except:
            self.new_window=Toplevel(self.root) 
            self.app=Cust_Win(self.new_window)   
        

    def roombooking(self):
        try:
            if(self.new_window.winfo_exists()):
                self.new_window.destroy()
                self.new_window=Toplevel(self.root)
                self.app=Roombooking(self.new_window)       
        except:
            self.new_window=Toplevel(self.root) 
            self.app=Roombooking(self.new_window)
    
        
    def details(self):
       try:
            if(self.new_window.winfo_exists()):
                self.new_window.destroy()
                self.new_window=Toplevel(self.root)
                self.app=Detailsroom(self.new_window)       
       except:
            self.new_window=Toplevel(self.root) 
            self.app=Detailsroom(self.new_window)
    
    def report(self):
       try:
            if(self.new_window.winfo_exists()):
                self.new_window.destroy()
                self.new_window=Toplevel(self.root)
                self.app=roomreport(self.new_window)       
       except:
            self.new_window=Toplevel(self.root) 
            self.app=roomreport(self.new_window)

    def logout(self):
        try:
            self.new_window.destroy()
            open_main=messagebox.askyesno("yesno","Do you want to logout")
            if open_main>0:
                self.root.destroy()            

            else:
                if not open_main:
                    return
        except:
            open_main=messagebox.askyesno("yesno","Do you want to logout")
            if open_main>0:
                    self.root.destroy()            

            else:
                 if not open_main:
                        return

        
        


if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
