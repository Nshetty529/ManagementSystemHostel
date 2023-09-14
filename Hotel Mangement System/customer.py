from tkinter import *
from PIL import Image,ImageTk  #module to set image
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from tkinter import font
from mysql.connector.locales.eng import client_error
import re




class Cust_Win:
    # Setting the geometry for the main window
    def __init__(self,root):
        
        label_font = font.Font(weight="bold")
        self.root=root
        self.root.title(" ")
        self.root.geometry("1275x590+250+220")
        img = PhotoImage(file="logo3.png")  # Replace "image.png" with any image file.
        self.root.iconphoto(False, img)
        # self.root.wm_iconbitmap("logo3.png")
    
        # lblimg1.place(x=270,y=0,width=1210,height=590)
        # lblimg1.place(x=270,y=0,width=1275,height=590)

        # ==================variabkes================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        

        # ==================title==============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",border=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1275,height=50)


         # =======================logo===================
        # img2=Image.open(r"C:\Users\HP\Desktop\Project\Hotel Mangement System\images\logohotel.png")
        # img2=img2.resize((100,40),Image.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        # lblimg.place(x=5,y=2,width=100,height=40)

        # ====================labelframe===================
        labelFrameleft=LabelFrame(self.root,bd=2,relief=SOLID, padx=2,font=("times new roman",12,"bold"))
        labelFrameleft.place(x=5,y=50,width=425,height=490)

        # =======================labels and entries==============
        # cutomerrefrence
        lbl_cust_ref=Label(labelFrameleft,text="Registration No", font=("arial",12,"bold"),padx=2,pady=6 )
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        # input feild created using ttk module
        entry_ref=ttk.Entry(labelFrameleft,textvariable=self.var_ref,width=22,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        # customer name
        cname=Label(labelFrameleft, text="Custumer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelFrameleft,textvariable=self.var_cust_name,width=22,font=("arial",13,"bold") )
        txtcname.grid(row=1,column=1)

        # mother name
        lblmname=Label(labelFrameleft, text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelFrameleft,textvariable=self.var_mother,width=22,font=("arial",13,"bold") )
        txtmname.grid(row=2,column=1)

        # gender 
        lbl_gender=Label(labelFrameleft, text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelFrameleft,textvariable=self.var_gender,font=("arial",12,"bold") ,width=20,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        

        # postcode
        lblPostCode=Label(labelFrameleft, text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelFrameleft,textvariable=self.var_post,width=22,font=("arial",13,"bold") )
        txtPostCode.grid(row=4,column=1)

        # mobile number
        lblMobile=Label(labelFrameleft, text="Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelFrameleft,textvariable=self.var_mobile,width=22,font=("arial",13,"bold") )
        txtMobile.grid(row=5,column=1)

        # Email
        lblEmail=Label(labelFrameleft, text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelFrameleft,textvariable=self.var_email,width=22,font=("arial",13,"bold") )
        txtEmail.grid(row=6,column=1)

        # nationality
        lblNationality=Label(labelFrameleft, text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_nationality=ttk.Combobox(labelFrameleft, textvariable=self.var_nationality,font=("arial",12,"bold") ,width=20,state="readonly")
        combo_nationality["value"]=("Indian","British","American")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)

        # id prof
        lblIdproof=Label(labelFrameleft, text="Id Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdproof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelFrameleft, textvariable=self.var_id_proof,font=("arial",12,"bold") ,width=20,state="readonly")
        combo_id["value"]=("Aadhar Card","Pan Card","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # id number
        lblIdNumber=Label(labelFrameleft, text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelFrameleft,textvariable=self.var_id_number,width=22,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)

        # Address
        lblAddress=Label(labelFrameleft, text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelFrameleft,textvariable=self.var_address,width=22,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)


        # ====================buttons================
        btn_Frame=Frame(labelFrameleft,bd=2,relief=FLAT)
        btn_Frame.place(x=2,y=420,width=412,height=40)
        
        btnAdd=Button(btn_Frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_Frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_Frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_Frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand2")
        btnReset.grid(row=0,column=3,padx=1)

        # ===================tabele frame search system=====================

        Table_Frame=LabelFrame(self.root,bd=2,relief=FLAT, padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=435,y=50,width=860,height=490)

        labelSearchBy=Label(Table_Frame ,text="Search By:",font=("times new roman",12,"bold") , bg="red",fg="white" ,width=15)
        labelSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame, textvariable=self.search_var,font=("arial",12,"bold") ,width=24,state="readonly")
        combo_search["value"]=("Mobile Number",)
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
        details_table.place(x=0,y=50,width=820,height=410)

        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)

        # Treeveiw in ttk use to create a table inside our frame
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("Treeview.Heading",background="black",foreground="white",font=('Arial Bold', 10))
        # pack
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Ref No.")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Contact")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("name", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("mother", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("gender", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("post", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("mobile", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("email", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("nationality", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("idproof", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("idnumber", width=100,anchor=CENTER)
        self.Cust_Details_Table.column("address", width=100,anchor=CENTER)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1 )
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    

    def add_data(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(self.var_mobile.get()==""or self.var_mother.get()=="" or self.var_post.get()=="" or self.var_mobile.get()=="" or self.var_email.get()=="" or self.var_id_number.get()=="" or self.var_address.get()==""   ):
            messagebox.showerror("Error","All feilds required",parent=self.root)
            return
        if((re.fullmatch('[6-9][0-9]{9}',self.var_mobile.get()))==None):
            messagebox.showerror("Error","Enter Valid Number",parent=self.root)
            return
        if((re.fullmatch(pattern, self.var_email.get()))==None):
            messagebox.showerror("Error","Enter Valid Email Address",parent=self.root)
            return
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_ref.get(),
                                                                                                        self.var_cust_name.get(),
                                                                                                        self.var_mother.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_post.get(),
                                                                                                        self.var_mobile.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_nationality.get(),
                                                                                                        
                                                                                                        self.var_id_proof.get(),
                                                                                                         self.var_id_number.get(),
                                                                                                         self.var_address.get()
                                                                                                                                                                                            
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Customer details added successfully",parent=self.root)
                self.var_cust_name.set(""),
                self.var_mother.set(""),
                # self.var_gender.set(""),
                self.var_post.set(""),
                self.var_mobile.set(""),
                self.var_email.set(""),
                # self.var_nationality.set(""),
                self.var_address.set(""),
                # self.var_id_proof.set(""),
                self.var_id_number.set("")
                x=random.randint(1000,9999)
                self.var_ref.set(str(x))
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        self.txt_search.set("")
        if(len(rows)==0):
            pass
        else:
            len(rows)!=0
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)

            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10]),

    def update(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        if(self.var_mobile.get()==""or self.var_mother.get()=="" or self.var_post.get()=="" or self.var_mobile.get()=="" or self.var_email.get()=="" or self.var_id_number.get()=="" or self.var_address.get()==""   ):
            messagebox.showerror("Error","All feilds required",parent=self.root)
            return
        if((re.fullmatch('[6-9][0-9]{9}',self.var_mobile.get()))==None):
            messagebox.showerror("Error","Enter Valid Number",parent=self.root)
            return
        if((re.fullmatch(pattern, self.var_email.get()))==None):
            messagebox.showerror("Error","Enter Valid Email Address",parent=self.root)
            return
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                                        
                                                                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                                                                    self.var_mother.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_post.get(),
                                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                                    self.var_email.get(),

                                                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                                                    
                                                                                                                                                                                    self.var_id_proof.get(),
                                                                                                                                                                                    self.var_id_number.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_ref.get()

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Sucess","Customer Details Has Been Updated Successfully",parent=self.root)
            self.var_cust_name.set(""),
            self.var_mother.set(""),
            # self.var_gender.set(""),
            self.var_post.set(""),
            self.var_mobile.set(""),
            self.var_email.set(""),
            # self.var_nationality.set(""),
            self.var_address.set(""),
            # self.var_id_proof.set(""),
            self.var_id_number.set("")
            x=random.randint(1000,9999)
            self.var_ref.set(str(x))



    def delete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer's Data",parent=self.root)
        if mdelete==True:
            conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            # onother method to run sql command
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
            # self.var_ref.set(""),
            self.var_cust_name.set(""),
            self.var_mother.set(""),
            # self.var_gender.set(""),
            self.var_post.set(""),
            self.var_mobile.set(""),
            self.var_email.set(""),
            # self.var_nationality.set(""),
            self.var_address.set(""),
            # self.var_id_proof.set(""),
            self.var_id_number.set("")
            x=random.randint(1000,9999)
            self.var_ref.set(str(x))
        
        else:
            if not mdelete:
                return
        
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self): 
        
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        self.var_address.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set("")
        self.txt_search.set("")

        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="management")
        my_cursor=conn.cursor()
        val=self.txt_search.get()
        query="Select * from customer where Mobile=%s"
        my_cursor.execute(query,(val,))
        
       

        rows=my_cursor.fetchall()

        # print(rows)
        if len(rows)==0: 
            messagebox.showinfo("Not Found","No data found")
        else:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()





        





        



if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()