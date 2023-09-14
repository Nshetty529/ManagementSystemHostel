
from tkinter import *
from PIL import Image,ImageTk  #module to set image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from mysql.connector.locales.eng import client_error
from datetime import datetime


class roomreport:
    # Setting the geometry for the main window
    def __init__(self,root):
        # label_font = font.Font(weight="bold")
        self.root=root
        self.root.title(" ")
        self.root.geometry("1275x590+250+220")
        # self.root.wm_iconbitmap("logo3.ico")
        img = PhotoImage(file="logo3.png")  # Replace "image.png" with any image file.
        self.root.iconphoto(False, img)

        self.var_name=StringVar()
        self.var_ref=StringVar()
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        
        self.var_roomno=StringVar()
        self.var_amount=StringVar()

        # ========heading========== 
        lbl_title=Label( self.root,text="BOOKING HISTORY",font=("times new roman",18,"bold"),bg="black",fg="gold",border=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1275,height=50)

        labelFrameleft=LabelFrame(self.root,bd=2,relief=FLAT, padx=2,font=("times new roman",12,"bold"))
        labelFrameleft.place(x=40,y=70,width=1200,height=500)

        btnDelete=Button(labelFrameleft,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=23,cursor="hand2")
        btnDelete.place(x=950,y=200)
        # serach option
        labelSearchBy=Label(labelFrameleft,text="Search By:",font=("times new roman",12,"bold") , bg="red",fg="white" ,width=15)
        labelSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(labelFrameleft, textvariable=self.search_var,font=("arial",12,"bold") ,width=24,state="readonly")
        combo_search["value"]=("Mobile Number",)
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(labelFrameleft,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        # serach and show buutton

        btnSearch=Button(labelFrameleft,command=self.search,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(labelFrameleft,command=self.fetch_data,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnShowAll.grid(row=0,column=4,padx=1)
        # ===================table
        Table_Frame=LabelFrame(self.root,bd=2,relief=FLAT, padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=40,y=110,width=900,height=500)
        details_table=Frame(Table_Frame,bd=2,relief=SOLID)
        details_table.place(x=0,y=0,width=850,height=450)

        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)

        # Treeveiw in ttk use to create a table inside our frame
        self.room_table=ttk.Treeview(details_table,columns=("ref","name","contact","checkin","checkout","roomno","amount"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("Treeview.Heading",background="black",foreground="white",font=('Arial Bold', 10))

        # pack
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("ref",text="Refrence")
        self.room_table.heading("name",text="Name")
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomno",text="Bed Number")
        self.room_table.heading("amount",text="Amount")

        self.room_table["show"]="headings"
        self.room_table.column("ref", width=100,anchor=CENTER)
        self.room_table.column("name", width=100,anchor=CENTER)
        self.room_table.column("contact", width=100,anchor=CENTER)
        self.room_table.column("checkin", width=100,anchor=CENTER)
        self.room_table.column("checkout", width=100,anchor=CENTER)
        self.room_table.column("roomno", width=100,anchor=CENTER)
        self.room_table.column("amount", width=100,anchor=CENTER)
        self.room_table.pack(fill=BOTH,expand=1 )
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
     # =================veiw data in table================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]


        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_checkin.set(row[3])
        self.var_checkout.set(row[4])
        
        self.var_roomno.set(row[5])
        self.var_amount.set(row[6])
    # =============fetch data============\
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from alldetail")
        rows=my_cursor.fetchall()
        self.txt_search.set("")
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    # =================serach function ====================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
        my_cursor=conn.cursor()
        val=self.txt_search.get()
        query="Select * from alldetail where contact=%s"
        my_cursor.execute(query,(val,))

       

        rows=my_cursor.fetchall()

        # print(rows)
        
        if len(rows)!=0: 
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    # ===========dlete=============

    def delete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room's Data",parent=self.root)
        if mdelete==True:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            # onother method to run sql command
            query="delete from alldetail where ref=%s and datein=%s and dateout=%s and contact=%s and amount=%s and room=%s"
            value=(self.var_ref.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_contact.get(),self.var_amount.get(),self.var_roomno.get())
            # print(self.var_ref.get())
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data()
if __name__=="__main__":
    root=Tk()
    obj=roomreport(root)
    root.mainloop()