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

p1 = PhotoImage(file = 'fbicon.png')
root.iconphoto(False, p1)

s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)

photo = PhotoImage(file = "plus.png")


photo1 = PhotoImage(file = "edit.png")

photo2 = PhotoImage(file = "delete.png")

photo3 = PhotoImage(file = "research.png")


photo4 = PhotoImage(file = "import.png")

photo5 = PhotoImage(file = "export-file.png")

photo6 = PhotoImage(file = "refresh.png")





invoices= PhotoImage(file="invoice.png")

orders = PhotoImage(file="order.png")

estimates = PhotoImage(file="estimate.png")

recurring = PhotoImage(file="recurring.png")

purchase = PhotoImage(file="purchase.png")

expenses = PhotoImage(file="expense.png")

customer = PhotoImage(file="customer.png")

product = PhotoImage(file="customer.png")

reports = PhotoImage(file="report.png")

setting = PhotoImage(file="setting.png")

tick = PhotoImage(file="check.png")

cancel = PhotoImage(file="close.png")

filebrowse = PhotoImage(file="folder.png")

clear = PhotoImage(file="clear.png")

share = PhotoImage(file="clear.png")



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
    p2 = PhotoImage(file = 'fbicon.png')
    add_customer.iconphoto(False, p1)
 
    
    add_customer.geometry("755x580+300+100")
   
    Labelframe1=LabelFrame(add_customer,text="Customer",font=('arial',8))
    Labelframe1.place(x=10,y=10,width=735,height=525)

    a1=Label(Labelframe1,text="Customer ID:",font=('arial',8),fg="Blue")
    a2=Label(Labelframe1,text="Category:",font=('arial',8))
    a3=Label(Labelframe1,text="Status :",font=('arial',8)).place(x=580,y=7)
    b1=Entry(Labelframe1)
    b2=ttk.Combobox(Labelframe1,values=['Default'])
    a1.place(x=5,y=7)
    a2.place(x=290,y=7)
        
    b1.place(x=100,y=7,width=180)
    b2.place(x=340,y=7,width=230)

    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = checkvar1, onvalue = 1, offvalue = 0, font=("arial", 8))
    chkbtn1.place(x=630,y=6)

    #.............Invoice to Frame............
    Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)",font=('arial',8))
    Labelframe2.place(x=10,y=35,width=330,height=125)

    a1=Label(Labelframe2,text="Business Name:",font=('arial',8),fg="Blue").place(x=10,y=10)
    a2=Label(Labelframe2,text="Address:",font=('arial',8),fg="Blue").place(x=10,y=35)

    b1=Entry(Labelframe2).place(x=100,y=10,width=210)
    b2=Entry(Labelframe2).place(x=100,y=35,width=210,height=63)

    #.............Ship to Frame...............
    Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)",font=('arial',8))
    Labelframe3.place(x=390,y=35,width=330,height=125)

    a11=Label(Labelframe3,text="Ship to Name:",font=('arial',8)).place(x=10,y=10)
    a21=Label(Labelframe3,text="Address:",font=('arial',8)).place(x=10,y=35)

    b11=Entry(Labelframe3).place(x=100,y=10,width=210)
    b21=Entry(Labelframe3).place(x=100,y=35,width=210,height=63)

    #............Contact Frame..................
    Labelframe4=LabelFrame(Labelframe1,text="Contact",font=('arial',8))
    Labelframe4.place(x=10,y=170,width=330,height=137)

    a11=Label(Labelframe4,text="Contact Person:",font=('arial',8)).place(x=10,y=10)
    a21=Label(Labelframe4,text="Email Address:",font=('arial',8),fg="Blue").place(x=10,y=35)
    a31=Label(Labelframe4,text="Tel. No:",font=('arial',8)).place(x=10,y=60)
    a41=Label(Labelframe4,text="Fax:",font=('arial',8)).place(x=193,y=60)
    a51=Label(Labelframe4,text="Mobile Number For SMS Notification:",font=('arial',8)).place(x=10,y=85)

    b11=Entry(Labelframe4).place(x=100,y=10,width=210)
    b21=Entry(Labelframe4).place(x=100,y=35,width=210)
    b31=Entry(Labelframe4).place(x=100,y=60,width=90)
    b41=Entry(Labelframe4).place(x=220,y=60,width=90)
    b51=Entry(Labelframe4).place(x=190,y=85,width=120)

    #...........Ship to Contact Frame..............
    Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact",font=('arial',8))
    Labelframe5.place(x=390,y=170,width=330,height=108)

    a11=Label(Labelframe5,text="Contact Person:",font=('arial',8)).place(x=10,y=10)
    a21=Label(Labelframe5,text="Email Address:",font=('arial',8)).place(x=10,y=35)
    a31=Label(Labelframe5,text="Tel. No:",font=('arial',8)).place(x=10,y=60)
    a41=Label(Labelframe5,text="Fax:",font=('arial',8)).place(x=193,y=60)

    b11=Entry(Labelframe5).place(x=100,y=10,width=210)
    b21=Entry(Labelframe5).place(x=100,y=35,width=210)
    b31=Entry(Labelframe5).place(x=100,y=60,width=90)
    b41=Entry(Labelframe5).place(x=220,y=60,width=90)

    #..........Payment Frame.........................
    Labelframe6=LabelFrame(Labelframe1,text="Payment Option",font=('arial',8))
    Labelframe6.place(x=10,y=317,width=330,height=80)

    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = checkvar1, onvalue = 1, offvalue = 0, font=("arial", 8))
    chkbtn1.place(x=10,y=6)

    a11=Label(Labelframe6,text="Specific Tax1%:",font=('arial',8)).place(x=150,y=7)
    a12=Label(Labelframe6,text="Discount%:",font=('arial',8)).place(x=10,y=30)

    b11=Entry(Labelframe6).place(x=240,y=7,width=70)
    b12=Entry(Labelframe6).place(x=70,y=30,width=70)

        
    #............Customer Type Frame.................
    Labelframe7=LabelFrame(Labelframe1,text="Customer type",font=('arial',8))
    Labelframe7.place(x=10,y=405,width=330,height=90)

    i=IntVar()
    r1=Radiobutton(Labelframe7, text = "Client", variable = i, value = 1, font=("arial", 8)).place(x=5,y=15)
    r2=Radiobutton(Labelframe7, text = "Vender", variable = i, value = 2, font=("arial", 8)).place(x=90,y=15)
    r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = i, value = 3, font=("arial", 8)).place(x=180,y=15)

    #.........Additional Info.......................
    Labelframe8=LabelFrame(Labelframe1,text="Additional Info",font=('arial',8))
    Labelframe8.place(x=390,y=288,width=330,height=80)

    a11=Label(Labelframe8,text="Country:",font=('arial',8)).place(x=10,y=5)
    a12=Label(Labelframe8,text="City:",font=('arial',8)).place(x=10,y=30)

    b11=ttk.Combobox(Labelframe8,value=[""]).place(x=100,y=5,width=210)
    b12=Entry(Labelframe8).place(x=100,y=30,width=210)

    #.............Note Frame.........................
    Labelframe9=LabelFrame(Labelframe1,text="Notes",font=('arial',8))
    Labelframe9.place(x=390,y=380,width=330,height=115)
    '''scrollbar = Scrollbar(Labelframe9)
        scrollbar.place(x=300,y=10)
        b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
        yscrollcommand.config(command=b12.yview)'''
    b12=Entry(Labelframe9).place(x=10,y=10,width=285,height=70)
    scrollbar = Scrollbar(Labelframe9)
    scrollbar.place(x=295,y=10)

    #.............OK and Cancel Button....................
    btnOK=Button(add_customer,text="OK",relief=GROOVE).place(x=20,y=545,width=50)
    btnCancel=Button(add_customer,text="Cancel",relief=GROOVE).place(x=652,y=545,width=80)



    add_customer.mainloop()



######################## FRONT PAGE OF CUSTOMER SECTION #######################################################################

    
mainFrame=Frame(tab7, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(5, 2))
pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

productIcon = ImageTk.PhotoImage(Image.open("plus.png"))
productLabel = Button(midFrame,compound="top", text="Add new\nCustomer",relief=RAISED,  command=add_customer,          image=productIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)

productLabel.pack(side="left", pady=3, ipadx=4)

proeditIcon = ImageTk.PhotoImage(Image.open("edit.png"))
proeditLabel = Button(midFrame,compound="top", text="Edit/View\nProduct",relief=RAISED, image=proeditIcon,  font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)

proeditLabel.pack(side="left")

prodeleteIcon = ImageTk.PhotoImage(Image.open("delete.png"))
prodeleteLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=prodeleteIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)

prodeleteLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)


root.mainloop()
