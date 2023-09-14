
from tkinter import *
from PIL import Image,ImageTk  #module to set image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime
from mysql.connector.locales.eng import client_error


class Detailsroom:
    # Setting the geometry for the main window
    def __init__(self,root):
        # label_font = font.Font(weight="bold")
        self.root=root
        self.root.title(" ")
        self.root.geometry("1275x590+250+220")
        # self.root.wm_iconbitmap("logo3.ico")
        img = PhotoImage(file="logo3.png")  # Replace "image.png" with any image file.
        self.root.iconphoto(False, img)

        # ========heading========== 
        lbl_title=Label(self.root,text="ADD NEW BED", font=("times new roman",18,"bold"),bg="black",fg="gold",border=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1275,height=50)

         # ====================labelframe===================
        labelFrameleft=LabelFrame(self.root,bd=2,relief=SOLID, padx=2,font=("times new roman",12,"bold"))
        labelFrameleft.place(x=80,y=120,width=540,height=350)

        # ====================labels and entry ===================
        self.var_floor=StringVar()
        self.var_roomno=StringVar()
        self.var_roomtype=StringVar()

       
        # floor
        lbl_floor=Label(labelFrameleft, text="Floor:",font=("arial",12,"bold"),padx=50,pady=50)
        lbl_floor.grid(row=2,column=0,sticky=W)
        # input feild created using ttk module
        entry_floor=ttk.Entry(labelFrameleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=2,column=1,sticky=W)

        # room no
        lbl_floor=Label(labelFrameleft, text="Bed Number:",font=("arial",12,"bold"),padx=50,pady=6)
        lbl_floor.grid(row=4,column=0,sticky=W)
        # input feild created using ttk module
        entry_floor=ttk.Entry(labelFrameleft,textvariable=self.var_roomno,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=4,column=1,sticky=W)

        # # Room Type
        # lbl_Roomtype=Label(labelFrameleft, text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6 )
        # lbl_Roomtype.grid(row=2,column=0,sticky=W)
        # # input feild created using ttk module
        # entry_Roomtype=ttk.Entry(labelFrameleft,textvariable=self.var_roomtype,width=20,font=("arial",13,"bold"))
        # entry_Roomtype.grid(row=2,column=1,sticky=W)\
        

        # =============================buttons======================

        btn_Frame=Frame(labelFrameleft,bd=2,relief=FLAT)
        btn_Frame.place(x=50,y=200,width=412,height=40)
        
        btnAdd=Button(btn_Frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_Frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_Frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_Frame,command=self.reset,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnReset.grid(row=0,column=3,padx=1)

        # ===================tabele frame search system=====================

        Table_Frame=LabelFrame(self.root,bd=2,relief=SOLID, padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=650,y=120,width=540,height=350)
        

        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)

        # Treeveiw in ttk use to create a table inside our frame
        self.room_table=ttk.Treeview(Table_Frame,columns=("Floor","Bed Number"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("Treeview.Heading",background="black",foreground="white",font=('Arial Bold', 10))

        # pack
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("Bed Number",text="Bed Number")
        # self.room_table.heading("Room Type",text="RoomType")
        

        self.room_table["show"]="headings"
    
        self.room_table.column("Floor", width=100,anchor=CENTER)
        self.room_table.column("Bed Number", width=100,anchor=CENTER)
        # self.room_table.column("Room Type", width=100)
        self.room_table.pack(fill=BOTH,expand=1 )
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
    #    ===================Adding sata in database room===================================
    def add_data(self):
            if(self.var_floor.get()==""or self.var_roomno.get()==""):
                messagebox.showerror("Error","All feilds required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into details values(%s,%s)",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_roomno.get(),
                                                                                        # self.var_roomtype.get()
                                                                                       
                                                                                                                                                                                        
                                                                                                                                                                                            
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into avlroom values(%s)",(
                                                                        self.var_roomno.get()  ,                                                              
                                                                                                                                                                                                                                                              
                                                                                                                                                                                            
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Room Details Added",parent=self.root)
                    self.var_floor.set(""),
                    self.var_roomno.set(""),
                    # self.var_roomtype.set("")

                   
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    
    # =============fetch data============\
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)

            conn.commit()
        conn.close()
    # =================veiw data in table================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
         
        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        # self.var_roomtype.set(row[2])
    
     # =============update====================

    def update(self): 
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set  Floor=%s where RoomNo=%s" ,(
                                                                                        self.var_floor.get(),
                                                                                        # self.var_roomtype.get(),
                                                                                        self.var_roomno.get()
                                                                                        
                                                                                                
            
                                                                                                                                                         

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Sucess","Room Details Has Been Updated Successfully",parent=self.root)
            
            self.var_floor.set(""),
            self.var_roomno.set(""),
            self.var_roomtype.set("")
            
            



     #=======================delete function=============
    def delete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room's Data",parent=self.root)
        # print(mdelete)
        if mdelete==True:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            # onother method to run sql command
            query="delete from details where RoomNo=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
            
        else:
            if not mdelete:
                return
        
        conn.commit()
        self.fetch_data()
        conn.close()
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
        my_cursor=conn.cursor()
        query=("DELETE FROM avlroom WHERE room1=%s")
        value=(self.var_roomno.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        self.fetch_data()
        conn.close()
        self.var_floor.set(""),
        self.var_roomno.set(""),
        # self.var_roomtype.set("")
    # =====reset======================\=
    def reset(self): 
        self.var_floor.set(""),
        self.var_roomno.set(""),
        # self.var_roomtype.set("")
       

   

    
        



       
    
  

if __name__=="__main__":
    root=Tk()
    obj=Detailsroom(root)
    root.mainloop()