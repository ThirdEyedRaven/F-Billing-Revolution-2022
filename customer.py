from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog





root = Tk()
root.state("zoomed")
root.title("F-Billing Revolution 2022 (FREE version) | Company database: fbillingdb | User:Administrator")

p1 = PhotoImage(file = "images/fbicon.png")
root.iconphoto(False, p1)

s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)

invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")

tick = PhotoImage(file="images/check.png")
cancel = PhotoImage(file="images/close.png")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)

  
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')

tabControl.pack(expand = 1, fill ="both")



def file():
    filename = filedialog.askopenfilename(title='open')
    return filename
def file_upload():
    f = file()
    img = Image.open(f)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(tab2, image=img)
    panel.image = img
    panel.pack()



#add new customer

def add_customer():
    add_customer = Toplevel()  
    
    add_customer.title("Add new Customer ")
    p2 = PhotoImage(file = "images/fbicon.png")
    add_customer.iconphoto(False, p1)
 
    
    add_customer.geometry("775x580+300+100")
   
    Labelframe1=LabelFrame(add_customer,text="Customer")
    Labelframe1.place(x=10,y=10,width=755,height=525)

    a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
    a2=Label(Labelframe1,text="Category:")
    a3=Label(Labelframe1,text="Status :")
    a3.place(x=620,y=7)
    b1=Entry(Labelframe1)
    b2=ttk.Combobox(Labelframe1,values=['Default'])
    a1.place(x=10,y=7)
    a2.place(x=330,y=7)
        
    b1.place(x=120,y=7,width=200)
    b2.place(x=390,y=7,width=220)

    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = checkvar1, onvalue = 1, offvalue = 0)
    chkbtn1.place(x=670,y=6)

    #.............Invoice to Frame............
    Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
    Labelframe2.place(x=10,y=35,width=340,height=125)

    a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
    a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)

    b1=Entry(Labelframe2).place(x=110,y=10,width=210)
    b2=Entry(Labelframe2).place(x=110,y=35,width=210,height=63)

    #>>

    btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=85,height=20)

    #.............Ship to Frame...............
    Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
    Labelframe3.place(x=400,y=35,width=340,height=125)

    a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
    a21=Label(Labelframe3,text="Address:").place(x=10,y=35)

    b11=Entry(Labelframe3).place(x=110,y=10,width=210)
    b21=Entry(Labelframe3).place(x=110,y=35,width=210,height=63)

    #............Contact Frame..................
    Labelframe4=LabelFrame(Labelframe1,text="Contact")
    Labelframe4.place(x=10,y=170,width=340,height=137)

    a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
    a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
    a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)

    b11=Entry(Labelframe4).place(x=110,y=10,width=210)
    b21=Entry(Labelframe4).place(x=110,y=35,width=210)
    b31=Entry(Labelframe4).place(x=110,y=60,width=90)
    b41=Entry(Labelframe4).place(x=230,y=60,width=90)
    b51=Entry(Labelframe4).place(x=215,y=85,width=105)

    #>>

    btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=220,height=20)


    #...........Ship to Contact Frame..............
    Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
    Labelframe5.place(x=400,y=170,width=340,height=108)

    a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
    a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)

    b11=Entry(Labelframe5).place(x=110,y=10,width=210)
    b21=Entry(Labelframe5).place(x=110,y=35,width=210)
    b31=Entry(Labelframe5).place(x=110,y=60,width=90)
    b41=Entry(Labelframe5).place(x=230,y=60,width=90)

    #..........Payment Frame.........................
    Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
    Labelframe6.place(x=10,y=317,width=340,height=80)

    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = checkvar1, onvalue = 1, offvalue = 0, font=("arial", 8))
    chkbtn1.place(x=10,y=6)

    a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
    a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)

    b11=Entry(Labelframe6).place(x=250,y=7,width=70)
    b12=Entry(Labelframe6).place(x=80,y=30,width=70)

        
    #............Customer Type Frame.................
    Labelframe7=LabelFrame(Labelframe1,text="Customer type")
    Labelframe7.place(x=10,y=405,width=340,height=90)

    i=IntVar()
    r1=Radiobutton(Labelframe7, text = "Client", variable = i, value = 1).place(x=5,y=15)
    r2=Radiobutton(Labelframe7, text = "Vender", variable = i, value = 2).place(x=90,y=15)
    r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = i, value = 3).place(x=180,y=15)

    #.........Additional Info.......................
    Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
    Labelframe8.place(x=400,y=288,width=340,height=80)

    a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
    a12=Label(Labelframe8,text="City:").place(x=10,y=30)

    b11=ttk.Combobox(Labelframe8,value=[""]).place(x=110,y=5,width=210)
    b12=Entry(Labelframe8).place(x=110,y=30,width=210)

    #.............Note Frame.........................
    Labelframe9=LabelFrame(Labelframe1,text="Notes")
    Labelframe9.place(x=400,y=380,width=340,height=115)
    '''scrollbar = Scrollbar(Labelframe9)
        scrollbar.place(x=300,y=10)
        b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
        yscrollcommand.config(command=b12.yview)'''
    b12=Entry(Labelframe9).place(x=20,y=10,width=295,height=70)
    scrollbar = Scrollbar(Labelframe9)
    scrollbar.place(x=295,y=10)

    #.............OK and Cancel Button....................

    btn1=Button(add_customer,width=50,compound = LEFT,image=tick ,text="  OK").place(x=20, y=545)
    btn2=Button(add_customer,width=80,compound = LEFT,image=cancel,text="  Cancel").place(x=665, y=545)




    add_customer.mainloop()


    # Edit/View customer

def edit_customer():
    edit_customer = Toplevel()  
    
    edit_customer.title("Edit Customer Details ")
    p2 = PhotoImage(file = "images/fbicon.png")
    edit_customer.iconphoto(False, p1)
 
    
    edit_customer.geometry("775x580+300+100")
   
    Labelframe1=LabelFrame(edit_customer,text="Customer")
    Labelframe1.place(x=10,y=10,width=755,height=525)

    a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
    a2=Label(Labelframe1,text="Category:")
    a3=Label(Labelframe1,text="Status :")
    a3.place(x=620,y=7)
    b1=Entry(Labelframe1)
    b2=ttk.Combobox(Labelframe1,values=['Default'])
    a1.place(x=10,y=7)
    a2.place(x=330,y=7)
        
    b1.place(x=120,y=7,width=200)
    b2.place(x=390,y=7,width=220)

    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = checkvar1, onvalue = 1, offvalue = 0)
    chkbtn1.place(x=670,y=6)

    #.............Invoice to Frame............
    Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
    Labelframe2.place(x=10,y=35,width=340,height=125)

    a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
    a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)

    b1=Entry(Labelframe2).place(x=110,y=10,width=210)
    b2=Entry(Labelframe2).place(x=110,y=35,width=210,height=63)

    #>>

    btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=85,height=20)

    #.............Ship to Frame...............
    Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
    Labelframe3.place(x=400,y=35,width=340,height=125)

    a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
    a21=Label(Labelframe3,text="Address:").place(x=10,y=35)

    b11=Entry(Labelframe3).place(x=110,y=10,width=210)
    b21=Entry(Labelframe3).place(x=110,y=35,width=210,height=63)

    #............Contact Frame..................
    Labelframe4=LabelFrame(Labelframe1,text="Contact")
    Labelframe4.place(x=10,y=170,width=340,height=137)

    a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
    a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
    a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)

    b11=Entry(Labelframe4).place(x=110,y=10,width=210)
    b21=Entry(Labelframe4).place(x=110,y=35,width=210)
    b31=Entry(Labelframe4).place(x=110,y=60,width=90)
    b41=Entry(Labelframe4).place(x=230,y=60,width=90)
    b51=Entry(Labelframe4).place(x=215,y=85,width=105)

    #>>

    btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=220,height=20)


    #...........Ship to Contact Frame..............
    Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
    Labelframe5.place(x=400,y=170,width=340,height=108)

    a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
    a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)

    b11=Entry(Labelframe5).place(x=110,y=10,width=210)
    b21=Entry(Labelframe5).place(x=110,y=35,width=210)
    b31=Entry(Labelframe5).place(x=110,y=60,width=90)
    b41=Entry(Labelframe5).place(x=230,y=60,width=90)

    #..........Payment Frame.........................
    Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
    Labelframe6.place(x=10,y=317,width=340,height=80)

    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = checkvar1, onvalue = 1, offvalue = 0, font=("arial", 8))
    chkbtn1.place(x=10,y=6)

    a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
    a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)

    b11=Entry(Labelframe6).place(x=250,y=7,width=70)
    b12=Entry(Labelframe6).place(x=80,y=30,width=70)

        
    #............Customer Type Frame.................
    Labelframe7=LabelFrame(Labelframe1,text="Customer type")
    Labelframe7.place(x=10,y=405,width=340,height=90)

    i=IntVar()
    r1=Radiobutton(Labelframe7, text = "Client", variable = i, value = 1).place(x=5,y=15)
    r2=Radiobutton(Labelframe7, text = "Vender", variable = i, value = 2).place(x=90,y=15)
    r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = i, value = 3).place(x=180,y=15)

    #.........Additional Info.......................
    Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
    Labelframe8.place(x=400,y=288,width=340,height=80)

    a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
    a12=Label(Labelframe8,text="City:").place(x=10,y=30)

    b11=ttk.Combobox(Labelframe8,value=[""]).place(x=110,y=5,width=210)
    b12=Entry(Labelframe8).place(x=110,y=30,width=210)

    #.............Note Frame.........................
    Labelframe9=LabelFrame(Labelframe1,text="Notes")
    Labelframe9.place(x=400,y=380,width=340,height=115)
    '''scrollbar = Scrollbar(Labelframe9)
        scrollbar.place(x=300,y=10)
        b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
        yscrollcommand.config(command=b12.yview)'''
    b12=Entry(Labelframe9).place(x=20,y=10,width=295,height=70)
    scrollbar = Scrollbar(Labelframe9)
    scrollbar.place(x=295,y=10)

    #.............OK and Cancel Button....................

    btn1=Button(edit_customer,width=50,compound = LEFT,image=tick ,text="  OK").place(x=20, y=545)
    btn2=Button(edit_customer,width=80,compound = LEFT,image=cancel,text="  Cancel").place(x=665, y=545)




    edit_customer.mainloop()

#delete Customer


def delete_customer():
   
    messagebox.askyesno("Delete Customers", "Are you sure want to delete 1 Customer(s) ?")

######################## FRONT PAGE OF CUSTOMER SECTION #######################################################################

    
mainFrame=Frame(tab7, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(5, 2))
pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

productIcon = ImageTk.PhotoImage(Image.open("images/user_add.png"))
productLabel = Button(midFrame,compound="top", text="Add new\nCustomer",relief=RAISED,  command=add_customer,          image=productIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)

productLabel.pack(side="left", pady=3, ipadx=4)

proeditIcon = ImageTk.PhotoImage(Image.open("images/user_edit.png"))
proeditLabel = Button(midFrame,compound="top", text="Edit/View\nCustomer",relief=RAISED,command=edit_customer, image=proeditIcon,  font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)

proeditLabel.pack(side="left")

prodeleteIcon = ImageTk.PhotoImage(Image.open("images/user_delete.png"))
prodeleteLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, command=delete_customer,image=prodeleteIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)

prodeleteLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)








prolabel = Label(tab7, text="Customers", font=("arial", 16), bg="#dbdad7")
prolabel.place(x=8,y=72)



product_frame=Frame(tab7,background="white",highlightbackground="gray",highlightthickness=1)
product_frame.place(x=1099,y=100,width=255,height=580)

pr_label = Label(tab7, text="Category", font=("arial", 16), bg="#dbdad7")
pr_label.place(x=1099,y=70)




 

pro_label = Label(tab7, text="Right click on datagrid row for more options.",  bg="#dbdad7")
pro_label.place(x=820,y=77)



 



#table
s=ttk.Style()
s.configure('Treeview.Heading',background='white')

tree=ttk.Treeview(tab7,selectmode='browse')
tree.place(x=8,y=100,height=570)
vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
vertical_bar.place(x=1083,y=101,height=570)

tree["columns"]=("1","2","3","4","5","6","7","8")
tree["show"]='headings'
tree.column("1",width=2,anchor='c')
tree.column("2",width=160,anchor='c')
tree.column("3",width=190,anchor='c')
tree.column("4",width=176,anchor='c')
tree.column("5",width=176,anchor='c')
tree.column("6",width=120,anchor='c')
tree.column("7",width=130,anchor='c')
tree.column("8",width=120,anchor='c')

tree.heading("1",text="")
tree.heading("2",text="Customer ID")
tree.heading("3",text="Category")
tree.heading("4",text="Customer Name")
tree.heading("5",text="Contact Persion")
tree.heading("6",text="Customer Tel.")
tree.heading("7",text="SMS Number")
tree.heading("8",text="Type")


######side_Table##############



tree1=ttk.Treeview(tab7,selectmode='browse')
tree1.place(height=580,width=254,
                      x=1099,y=101
                      )



tree1["columns"]=("1")
tree1["show"]='headings'

tree1.column("1",width=254,anchor='c')



tree1.heading("1",text="View filter by category")


listbox = Listbox(tab7,height =8,  
                      width = 29,  
                      bg = "white",
                    
                      activestyle = 'dotbox',  
                      fg = "black",
                      
                     highlightbackground="white")  
listbox.insert(0, "  View all records")
listbox.insert(1, "  View only Client/Vendor Type")
listbox.insert(2, "  View only Client Type")
listbox.insert(3, "  View only Vendor Type")
listbox.insert(4, "  Default")
listbox.place(x=1099,y=120,height=545,width=254)















root.mainloop()
