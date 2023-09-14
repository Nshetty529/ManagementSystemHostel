from tkinter import *
from PIL import Image,ImageTk  #module to set image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime
from datetime import date
from datetime import timedelta
from mysql.connector.locales.eng import client_error


class Roombooking:
    # Setting the geometry for the main window
    def __init__(self,root):
        # label_font = font.Font(weight="bold")
        self.root=root
        self.root.title(" ")
        self.root.geometry("1275x590+250+220")
        # self.root.wm_iconbitmap("logo3.ico")
        img = PhotoImage(file="logo3.png")  # Replace "image.png" with any image file.
        self.root.iconphoto(False, img)

        # =======================variables==================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomavailable=StringVar()
        self.var_noofdays=StringVar()
        self.var_tax=StringVar()
        self.var_total=StringVar()
        self.var_finaltotal=StringVar()
        self.var_name=StringVar()
        self.var_ref=StringVar()
     



        # ========heading========== 
        lbl_title=Label(self.root,text="BOOKING BED", font=("times new roman",18,"bold"),bg="black",fg="gold",border=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1275,height=50)

         # ====================labelframe===================
        labelFrameleft=LabelFrame(self.root,bd=2,relief= SOLID, padx=2,font=("times new roman",12,"bold"))
        labelFrameleft.place(x=8,y=50,width=425,height=482)

        # ====================labels and entry ===================
        # cutomer contact
        lbl_cust_contact=Label(labelFrameleft, text="Custumer Contact:",font=("arial",12,"bold"),padx=2,pady=6 )
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        # input feild created using ttk module
        entry_contact=ttk.Entry(labelFrameleft,textvariable=self.var_contact,width=13,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        # fetch data button
        btnFetchData=Button(labelFrameleft,command=self.fetch_contact,text="Fetch Data",font=("arial",9,"bold"),bg="black",fg="white",width=9,cursor="hand2")
        btnFetchData.place(x=280,y=4)

        # print(date.today())

        # check in date
        chech_in=Label(labelFrameleft, text="Check in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        chech_in.grid(row=1,column=0,sticky=W)
        textcheck_in_date=ttk.Entry(labelFrameleft,textvariable=self.var_checkin,width=22,font=("arial",13,"bold") )
        textcheck_in_date.insert(0,date.today())
        textcheck_in_date.grid(row=1,column=1)

        # check out date
        lbl_chech_out=Label(labelFrameleft, text="Check out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_chech_out.grid(row=2,column=0,sticky=W)
        textcheck_out_date=ttk.Entry(labelFrameleft,textvariable=self.var_checkout,width=22,font=("arial",13,"bold") )
        
        presentday = datetime.now()
        tomorrow = presentday + timedelta(1)
        textcheck_out_date.insert(0,tomorrow.strftime('%Y-%m-%d'))


        textcheck_out_date.grid(row=2,column=1)

       

        

         # Available Room
        lblRoomAvailable=Label(labelFrameleft, text="Available Bed:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        # textRoomAvailable=ttk.Entry(labelFrameleft,textvariable=self.var_roomavailable,width=22,font=("arial",13,"bold") )
        # textRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select room1 from avlroom")
        rows=my_cursor.fetchall()
        # print(rows)

        
        combo_RoomNo=ttk.Combobox(labelFrameleft, textvariable=self.var_roomavailable,font=("arial",12,"bold") ,width=20,state="readonly")
        combo_RoomNo["value"]=rows
        # combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        # # Meal
        # lblMeal=Label(labelFrameleft, text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        # lblMeal.grid(row=5,column=0,sticky=W)
        # textMeal=ttk.Entry(labelFrameleft,textvariable=self.var_meal,width=22,font=("arial",13,"bold") )
        # textMeal.grid(row=5,column=1)

        # No of days
        lblNoOfDays=Label(labelFrameleft, text="No of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        textNoOfDays=ttk.Entry(labelFrameleft,textvariable=self.var_noofdays,width=22,font=("arial",13,"bold") )
        textNoOfDays.grid(row=6,column=1)

        # Paid Pax
        lblNoOfDays=Label(labelFrameleft, text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        textNoOfDays=ttk.Entry(labelFrameleft,textvariable=self.var_tax,width=22,font=("arial",13,"bold") )
        textNoOfDays.grid(row=7,column=1)

        # SubTotakl
        lblsubtotal=Label(labelFrameleft, text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblsubtotal.grid(row=8,column=0,sticky=W)
        textsubtotal=ttk.Entry(labelFrameleft,textvariable=self.var_total,width=22,font=("arial",13,"bold") )
        textsubtotal.grid(row=8,column=1)

        # Total Cost
        lblTotalCost=Label(labelFrameleft, text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)
        textTotalCost=ttk.Entry(labelFrameleft,textvariable=self.var_finaltotal,width=22,font=("arial",13,"bold") )
        textTotalCost.grid(row=9,column=1)
        # =============================Bill buttons======================
        btnBill=Button(labelFrameleft,command=self.total,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=20,cursor="hand2")
        btnBill.place(x=90,y=340)
        # =============================buttons======================

        btn_Frame=Frame(labelFrameleft,bd=2,relief=FLAT)
        btn_Frame.place(x=3,y=438,width=412,height=40)
        
        btnAdd=Button(btn_Frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_Frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_Frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_Frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnReset.grid(row=0,column=3,padx=1)

        # ====================right side image===============
        img3=Image.open(r"C:\Users\HP\Desktop\Project\Hotel Mangement System\images\bed.jpg")
        img3=img3.resize((520,300),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=FLAT)
        lblimg.place(x=760,y=55,width=520,height=200)

        # ===================tabele frame search system=====================

        Table_Frame=LabelFrame(self.root,bd=2,relief=FLAT, padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=435,y=280,width=850,height=260)

        labelSearchBy=Label(Table_Frame ,text="Search By:",font=("times new roman",12,"bold") , bg="red",fg="white" ,width=15)
        labelSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame, textvariable=self.search_var,font=("arial",12,"bold") ,width=24,state="readonly")
        combo_search["value"]=("Mobile Number","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        # serach and show buutton

        btnSearch=Button(Table_Frame,command=self.search,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,command=self.fetch_data,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnShowAll.grid(row=0,column=4,padx=1)
        # ========================show data table==================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=830,height=200)

        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)

        # Treeveiw in ttk use to create a table inside our frame
        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomavailable","noofdays","tax","total","finaltotal"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("Treeview.Heading",background="black",foreground="white",font=('Arial Bold', 10))

        # pack
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomavailable",text="Bed Number")
        self.room_table.heading("noofdays",text="No of Days")
        self.room_table.heading("tax",text="Tax")
        self.room_table.heading("total",text="Total")
        self.room_table.heading("finaltotal",text="Final Total ")
        

        self.room_table["show"]="headings"

        self.room_table.column("contact", width=100,anchor=CENTER)
        self.room_table.column("checkin", width=100,anchor=CENTER)
        self.room_table.column("checkout", width=100,anchor=CENTER)
        self.room_table.column("roomavailable", width=100,anchor=CENTER)
        self.room_table.column("noofdays", width=100,anchor=CENTER)
        self.room_table.column("tax",width=100,anchor=CENTER)
        self.room_table.column("total",width=100,anchor=CENTER)
        self.room_table.column("finaltotal",width=100,anchor=CENTER)
        
        self.room_table.pack(fill=BOTH,expand=1 )
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()


    #    ===================Adding sata in database room===================================
    def add_data(self):
        if(self.var_contact.get()==""or self.var_checkin.get()==""or self.var_checkout.get()==""or self.var_roomavailable.get()==""or self.var_noofdays.get()==""or self.var_tax.get()==""or self.var_total.get()==""or self.var_finaltotal.get()==""):
            messagebox.showerror("Error","All feilds required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                     self.var_contact.get(),
                                                                                     self.var_checkin.get(),
                                                                                     self.var_checkout.get(),
                                                                                     
                                                                                     self.var_roomavailable.get(),
                                                                                     
                                                                                     self.var_noofdays.get(),
                                                                                     self.var_tax.get(),
                                                                                     self.var_total.get(),
                                                                                     self.var_finaltotal.get()

                                                                                                                                                                                    
                                                                                                                                                                                        
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
                my_cursor=conn.cursor()
                query=("DELETE FROM avlroom WHERE room1=%s")
                value=(self.var_roomavailable.get(),)
                my_cursor.execute(query,value)
                # print("***************************************hogaya")
                

               
                conn.commit()
                self.fetch_data()
                conn.close()

                



                # conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
                # my_cursor=conn.cursor()
                # query=("select Name from customer where Mobile=%s")
                # value=(self.var_contact.get(),)
                # my_cursor.execute(query,value,)
                # row=my_cursor.fetchone()
                # conn.commit()
                # my_cursor1=conn.cursor()
                # my_cursor1.executemany("insert into alldetail values(%s,%s,%s,%s,%s)",( 
                #                                                                     row,
                #                                                                     self.var_contact.get(),
                #                                                                     self.var_checkin.get(),
                #                                                                     self.var_checkout.get(),
                #                                                                     self.var_roomavailable.get()
                # ))
                                                                                                                      


                # messagebox.showinfo("Sucess","Room Booked",parent=self.root)
                presentday = datetime.now()
                tomorrow = presentday + timedelta(1)
                self.var_checkin.set(presentday.strftime('%Y-%m-%d')),
                self.var_checkout.set(tomorrow.strftime('%Y-%m-%d')),

                
                
                self.var_contact.set(" "),
                
                self.var_roomavailable.set(" "),
                self.var_noofdays.set(" ")
                self.var_tax.set(""),
                self.var_total.set(""),
                self.var_finaltotal.set("")
                
                self.after_fetch()
                
            except Exception as es:
                pass
                # messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    # =============fetch data============\
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        self.txt_search.set("")
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

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomavailable.set(row[3])
        self.var_noofdays.set(row[4])
        self.var_tax.set(row[5]),
        self.var_total.set(row[6]),
        self.var_finaltotal.set(row[7])
      
        

    # =============update====================

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in=%s,Check_out=%s,Roomavailable=%s,Noofdays=%s,tax=%s,total=%s,finaltotal=%s,where Contact1=%s" ,(
            
                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                          
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            
                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                            self.var_tax.get(),
                                                                                                                                            self.var_total.get(),
                                                                                                                                            self.var_finaltotal.get(),
                                                                                                                                            self.var_contact.get()
                                                                                                                                                                                    

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Sucess","Room Details Has Been Updated Successfully",parent=self.root)
            self.var_contact.set(" "),
            presentday = datetime.now()
            tomorrow = presentday + timedelta(1)
            self.var_checkin.set(presentday.strftime('%Y-%m-%d')),
            self.var_checkout.set(tomorrow.strftime('%Y-%m-%d')),

      
            
            self.var_roomavailable.set(" "),
         
            self.var_noofdays.set(" ")
            self.var_tax.set(""),
            self.var_total.set(""),
            self.var_finaltotal.set("")
            self.after_fetch()
            

     #=======================delete function=============
    def delete(self):
        
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room's Data",parent=self.root)
        if mdelete==True:
            self.fetch_contact()
            # adding bed number in avl bed
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into avlroom values(%s)",(self.var_roomavailable.get(),))
           
            conn.commit()
            self.fetch_data()
            conn.close()

            # print(self.var_name[0])
            # print(self.var_ref[0])
            # print(self.var_contact.get())
            # print(self.var_finaltotal.get())

            # deleting data 
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact1 =%s"
            value=(self.var_contact.get(),)
            # print(self.var_contact.get())
            my_cursor.execute(query,value)
           
            conn.commit()
            self.fetch_data()
            conn.close()

            # adding data in booking history
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",self.var_finaltotal.get())
            query="INSERT INTO  `alldetail` (`ref`,`Name`,`contact`,`datein` ,`dateout` ,`room`,`amount`) \
                VALUES(%s,%s,%s,%s,%s,%s,%s)"
            my_data=(self.var_ref[0],self.var_name[0],self.var_contact.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_roomavailable.get(),self.var_finaltotal.get(),)
            my_cursor.execute(query,my_data)
            # print("===========================================================hogaya")
                
            conn.commit()
            self.fetch_data()
            conn.close()

            

            presentday = datetime.now()
            tomorrow = presentday + timedelta(1)
            self.var_checkin.set(presentday.strftime('%Y-%m-%d')),
            self.var_checkout.set(tomorrow.strftime('%Y-%m-%d')),

            self.var_contact.set(" "),

            
            self.var_roomavailable.set(" "),
            
            self.var_noofdays.set(" ")
            self.var_tax.set(""),
            self.var_total.set(""),
            self.var_finaltotal.set("")
           
            self.after_fetch()
        
        else:
            if not mdelete:
                return
        
     

    # =====reset======================\=
    def reset(self): 
        self.var_contact.set(" "),
        
        presentday = datetime.now()
        tomorrow = presentday + timedelta(1)
        self.var_checkin.set(presentday.strftime('%Y-%m-%d')),
        self.var_checkout.set(tomorrow.strftime('%Y-%m-%d')),

     
        self.var_roomavailable.set(" "),
       
        self.var_noofdays.set(" ")
        self.var_tax.set(""),
        self.var_total.set(""),
        self.var_finaltotal.set("")
        self.txt_search.set("")
        self.after_fetch()
        

    # =============================Data Fetching from customr============================
    def after_fetch(self):
            
            
                # creating frame to show room data
            showDataframe=Frame(self.root,bd=4,relief=FLAT,padx=2)
            showDataframe.place(x=450,y=70,width=300,height=180)

            lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)
            

                # fetching gender
          
                
                

            lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=30)
           

                # Email
           
            lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
            lblEmail.place(x=0,y=60)
          
                

                # Nationaltity
         

            lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
            lblNationality.place(x=0,y=120)
         
                # Address
           

            lblddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
            lblddress.place(x=0,y=90)
          

    def fetch_contact(self):
        # print("me mobile ju============================",self.var_contact.get())
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            query=("select Ref from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            self.var_ref=row


            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            self.var_name=row
            
            

            
                # creating frame to show room data
            showDataframe=Frame(self.root,bd=4,relief=FLAT,padx=2)
            showDataframe.place(x=450,y=70,width=300,height=180)

            lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=0)

                # fetching gender
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            query=("select Gender from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
                
                

            lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=30)
            lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl2.place(x=90,y=30)

                # Email
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            query=("select Email from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
            lblEmail.place(x=0,y=60)
            lblEmail=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lblEmail.place(x=90,y=60)
                

                # Nationaltity
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            query=("select Nationality from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
            lblNationality.place(x=0,y=120)
            lblNationality=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lblNationality.place(x=90,y=120 ) 
                # Address
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            query=("select Address from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
            lblddress.place(x=0,y=90)
            lblddress=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lblddress.place(x=90,y=90 )

    # ====================seraching data in room=================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
        my_cursor=conn.cursor()
        val=self.txt_search.get()
        query="Select * from room where Contact1=%s"
        my_cursor.execute(query,(val,))

        
        rows=my_cursor.fetchall()
        if len(rows)!=0: 
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    # =====================total amount calculation=======================
    def total(self):
        
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%Y-%m-%d")
        outDate=datetime.strptime(outDate,"%Y-%m-%d")
        self.var_noofdays.set(abs(outDate-inDate).days)
        q5=float(250)*float((outDate-inDate).days)
        
      
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_tax.set(Tax)
        self.var_total.set(ST)
        self.var_finaltotal.set(TT)

        

       



if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()