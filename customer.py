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




root=Tk()
root.geometry("1500x800")
root.state("zoomed")
root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
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
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
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




selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")

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
    ca=StringVar() 
    b2=ttk.Combobox(Labelframe1,textvariable = ca )    
      
    # Adding combobox drop down list 
    b2['values'] = ('Default') 
      
    b2.place(x=390,y=220) 
    b2.current(0)
    a1.place(x=10,y=7)
    a2.place(x=330,y=7)
        
    b1.place(x=120,y=7,width=200)
    b2.place(x=390,y=7,width=220)

    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = checkvar1, onvalue = 0, offvalue = 1)
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
    
    b11val = IntVar(Labelframe6, value='0')

    b11=Entry(Labelframe6).place(x=250,y=7,width=70)
    b12=Entry(Labelframe6,textvariable=b11val).place(x=80,y=30,width=70)

        
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

    c=StringVar() 
    

    b11=ttk.Combobox(Labelframe8,textvariable=c)
    b11.place(x=110,y=5,width=210)
    
   
    # Adding combobox drop down list 
    b11['values'] = ('India','America') 
      
    b11.place(x=110,y=5) 

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
    ca=StringVar() 
    b2=ttk.Combobox(Labelframe1,textvariable = ca )

  
    # Adding combobox drop down list 
    b2['values'] = ('Default') 
      
    b2.place(x=390,y=220) 
    b2.current(0)


    a1.place(x=10,y=7)
    a2.place(x=330,y=7)
        
    b1.place(x=120,y=7,width=200)
    b2.place(x=390,y=7,width=220)

    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = checkvar1, onvalue = 0, offvalue = 1)
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
    
    b11val = IntVar(Labelframe6, value='0')

    b11=Entry(Labelframe6).place(x=250,y=7,width=70)
    b12=Entry(Labelframe6,textvariable=b11val).place(x=80,y=30,width=70)


        
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

    c=StringVar() 
    

    b11=ttk.Combobox(Labelframe8,textvariable=c)
    b11.place(x=110,y=5,width=210)
    

      
    # Adding combobox drop down list 
    b11['values'] = ('India','America') 
      
    b11.place(x=110,y=5) 
  

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

#print Invoice


def printinvoice():

  def property1():
    propert=Toplevel()

  
 
    
    #edit_customer.geometry("775x580+300+100")

    propert.title("OneNote for Windows 10 Document Properties")
    p2 = PhotoImage(file = "images/fbicon.png")
    propert.iconphoto(False, p1)
    propert.geometry("580x470+380+210")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Options")
      p2 = PhotoImage(file = "images/fbicon.png")
      propert1.iconphoto(False, p1)
      propert1.geometry("580x470+410+220")
      property1_Frame1=LabelFrame(propert1,height=405, width=560)
      property1_Frame1.place(x=10, y=10)  

      name=Label(property1_Frame1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(property1_Frame1, text="Paper/Output").place(x=30, y=35)
      size=Label(property1_Frame1, text="Paper size:").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(property1_Frame1, width = 28, textvariable = n )
      search['values'] = ('A4','Letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(property1_Frame1, text="Copy Count:").place(x=55, y=95)
      nocopy = Spinbox(property1_Frame1,from_=0,to=100000000, width=28).place(x=150, y=95)    

      btn=Button(propert1,text="OK", width=10,).place(x=390, y=425)
      btn=Button(propert1,text="Cancel", width=10,).place(x=490, y=425)     
      


    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=450, width=581)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    




    property_Frame1=LabelFrame(property_Frame,height=380, width=560)
    property_Frame1.place(x=10, y=10)   

    name=Label(property_Frame1, text="Orientation:").place(x=10, y=15)
    n = StringVar()
    search = ttk.Combobox(property_Frame1, width = 28, textvariable = n )
    search['values'] = ('Landscape','Portrait')
    search.place(x=10,y=40)
    search.current(0)

    text=Text(property_Frame1,width=40).place(x=217, y=20,height=300)

    btn=Button(property_Frame1, text="Advanced...", width=10,command=property2).place(x=430, y=335)
    btn=Button(property_Frame,text="OK", width=10,).place(x=390, y=400)
    btn=Button(property_Frame, text="Cancel", width=10,).place(x=490, y=400)     


  
     
     
  print1=Toplevel()

  print1.title("Print")
  p2 = PhotoImage(file = "images/fbicon.png")
  print1.iconphoto(False, p1)
      

      
  print1.geometry("580x390+350+200")
      
  printerframe=LabelFrame(print1, text="Printer", height=85, width=563)
  printerframe.place(x=10, y=5)   




  name=Label(printerframe, text="Name:").place(x=10, y=5)
  
  v=StringVar() 
  
  e1= ttk.Combobox(printerframe,textvariable=v)
  
  
    # Adding combobox drop down list 
  e1['values'] = ('OneNote for Windows10','Microsoft XPS Document Writer','Microsoft Print PDF','Fax') 
      
  e1.place(x=70,y=5,width=310) 
  e1.current(0)
  

   
    


  where=Label(printerframe, text="Where:").place(x=10, y=35)
  printocheckvar=IntVar()
  printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
  printochkbtn.place(x=390, y=35)
  btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=470, y=5)

  pageslblframe=LabelFrame(print1, text="Pages", height=140, width=277)
  pageslblframe.place(x=10, y=95)
  radvar=IntVar()
  radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
  radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
  radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
  pagecountentry = Entry(pageslblframe, width=30).place(x=80, y=47)
  pageinfolabl=Label(pageslblframe,text="Enter page numbers and/or page ranges\n      seperated by commas. For example:1,3,5-12")
  pageinfolabl.place(x=0, y=75)

  copylblframe=LabelFrame(print1, text="Copies", height=140, width=277)
  copylblframe.place(x=295, y=95)
  nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
  noentry = Spinbox(copylblframe,from_=0,to=100000000, width=18).place(x=140, y=5)      
  one=Frame(copylblframe, width=30, height=50, bg="black").place(x=20, y=40)     
  two=Frame(copylblframe, width=30, height=50, bg="grey").place(x=15, y=45)     
  three=Frame(copylblframe, width=30, height=50, bg="white").place(x=10, y=50)      
  four=Frame(copylblframe, width=30, height=50, bg="black").place(x=80, y=40)      
  fiv=Frame(copylblframe, width=30, height=50, bg="grey").place(x=75, y=45)      
  six=Frame(copylblframe, width=30, height=50, bg="white").place(x=70, y=50)      
  collatecheckvar=IntVar()
  collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
  collatechkbtn.place(x=120, y=40)

  othrlblframe=LabelFrame(print1, text="Other", height=100, width=277)
  othrlblframe.place(x=10, y=240)
  printlb=Label(othrlblframe, text="Print").place(x=5, y=0)

  va=StringVar()  
  dropprint= ttk.Combobox(othrlblframe,textvariable=va)
    
    # Adding combobox drop down list 
  dropprint['values'] = ('AllPages','Odd Pages','Even Pages')     
  dropprint.place(x=80,y=0,width=185) 
  dropprint.current(0)


  orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
  dropord = ttk.Combobox(othrlblframe, width=28).place(x=80, y=25)

  
  val=StringVar() 
  dropord= ttk.Combobox(othrlblframe,textvariable=val)
  
  
    # Adding combobox drop down list 
  dropord['values'] = ('Direct(1-9)','Reverse(1-9)') 
      
  dropord.place(x=80,y=25,width=185) 
  dropord.current(0)

  duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)


  val1=StringVar() 
  
  droplex= ttk.Combobox(othrlblframe,textvariable=val1)
  
  
    # Adding combobox drop down list 
  droplex['values'] = ('Default','Vertical','Horizontal','Simplex') 
      
  droplex.place(x=80,y=50,width=185) 
  droplex.current(0)
  

  prmodelblframe=LabelFrame(print1, text="Print mode",height=100, width=277)
  prmodelblframe.place(x=295, y=240)

  
  val11=StringVar() 
  
  dropscal= ttk.Combobox(prmodelblframe,textvariable=val11)
  
  
    # Adding combobox drop down list 
  dropscal['values'] = ('Default','Split big Pages','Join Small Pages','Scale') 
      
  dropscal.place(x=5,y=5,width=260,height=40) 
  dropscal.current(0)
  
  poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=50)

  val12=StringVar() 
  
  droppos= ttk.Combobox(prmodelblframe,textvariable=val12)
  
  
    # Adding combobox drop down list 
  droppos['values'] = ('Default') 
      
  droppos.place(x=136,y=50,width=129) 
  droppos.current(0)
  

  okbtn=Button(print1, text="Ok", width=10).place(x=390, y=350)
  canbtn=Button(print1, text="Cancel", width=10).place(x=490, y=350)






#EMAIL INVOICE LIST



      
def emailinvoice():
  mailDetail=Toplevel()
  mailDetail.title("E-Mail Invoice List")
  p2 = PhotoImage(file = "images/fbicon.png")
  mailDetail.iconphoto(False, p1)
  mailDetail.geometry("1030x550+150+120")
 
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)

  messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)



  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)

  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)















#sms notification order
  
def customersms():
  send_SMS=Toplevel()
  
  send_SMS.title("Send SMS notification")
  p2 = PhotoImage(file = "images/fbicon.png")
  send_SMS.iconphoto(False, p1)
  send_SMS.geometry("580x500+380+150")

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  sms_Notebook = ttk.Notebook(send_SMS)
  SMS_Notification = Frame(sms_Notebook, height=485, width=585)
  SMS_Service_Account = Frame(sms_Notebook, height=485, width=585)
  sms_Notebook.add(SMS_Notification, text="SMS Notification")
  sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
  sms_Notebook.place(x=0, y=0)

  numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
  numlbel.place(x=10, y=10)
  numentry=Entry(SMS_Notification,width=92).place(x=10, y=35,height=25)
  stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=65)
  stex=Entry(SMS_Notification, width=60).place(x=10, y=90,height=120)
  no=Label(SMS_Notification, text="0/160 characters")
  no.place(x=285, y=210)
  
  dclbel=Label(SMS_Notification, text="Double click to insert into text")
  dclbel.place(x=395, y=65)
  dcl=Entry(SMS_Notification, width=27)
  dcl.place(x=395, y=90,height=200)
  
  smstype=LabelFrame(SMS_Notification, text="SMS message type", width=365, height=60)
  smstype.place(x=10, y=230)
  snuvar=IntVar()
  normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
  normal_rbtn.place(x=15, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
  unicode_rbtn.place(x=195, y=5)
  tiplbf=LabelFrame(SMS_Notification, text="Tips", width=552, height=120)
  tiplbf.place(x=10, y=292)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS number with the country code. Do not use the + sign at the beginning(example\nUS number: 8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
  tiplabl.place(x=5, y=5)


  btn1=Button(SMS_Notification,width=150,compound = LEFT,image=tick ,text="  Send SMS notification").place(x=10, y=425,height=31)
  btn2=Button(SMS_Notification,width=215,compound = LEFT,image=warnin,text="  Confirm SMS cost before sending").place(x=190, y=425,height=31)
  btn3=Button(SMS_Notification,width=80,compound = LEFT,image=cancel,text="  Cancel").place(x=472, y=425,height=31)


  


  smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=555, height=65)
  smstype.place(x=10, y=5)
  snumvar=IntVar()
  normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="EXPERTTEXTING(www.experttexting.com-Recommended", variable=snumvar, value=2)
  unicode_rbtn.place(x=210, y=5)

  sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=555, height=100)
  sms1type.place(x=10, y=80)
  name=Label(sms1type, text="Username").place(x=10, y=5)
  na=Entry(sms1type,width=29).place(x=100, y=5,height=23)
  password=Label(sms1type, text="Password").place(x=10, y=45)
  pas=Entry(sms1type, width=29).place(x=100, y=45,height=23)



  combo=Label(sms1type,text="Route").place(x=320, y=5)
  n = StringVar()
  combo1 = ttk.Combobox(sms1type,textvariable = n )

  combo1['values'] = ('1-Economy (test first)','2-Standard (default)','3-Premium') 
  combo1.place(x=375,y=5,height=23,width=165)  
  
  combo1.current(0)
  

  btn1=Button(sms1type,width=110,compound = LEFT,image=saves,text="  Save settings").place(x=420, y=35,height=31)



  
  tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=555, height=250)
  tiplbf.place(x=10, y=190)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
  tiplabl.place(x=2, y=5)
  tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
  tiplabl1.place(x=2, y=60)
  tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
  tiplabl2.place(x=2, y=100)
  tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
  tiplabl3.place(x=2, y=140)
  checkvar1=IntVar()
  chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=130, y=200)  










#IMPORT CUSTOMERS

def import_customer():

    top=Toplevel()
   
    top.title("Import Customers list from Excel(XLS)File")
    p2 = PhotoImage(file = "images/fbicon.png")
    top.iconphoto(False, p1)
    top.geometry("785x540+280+100")
    importframe=Frame(top)
    importframe.place(x=0,y=0,height=700,width=785)
    impolbl=Label(importframe,text="Import source Excel(XLS) File:").place(x=10,y=10)
    impoentry=Entry(importframe,bg="white")
    impoentry.place(x=10,y=40,width=400,height=25)
    previewlbl=Label(importframe,text="Source XLS File preview").place(x=10,y=75)

    
   
    ###### LISTBOX #####################
    langs = ()

    langs_var = StringVar(value=langs)

    listbox = Listbox(
        importframe,
        listvariable=langs_var,
        width=71,
        height=8,
        selectmode='extended')

    listbox.place(x=10,y=102,height=390)
    
    # link a scrollbar to a list
    scrollbar = Scrollbar(
        importframe,
        orient='vertical',
        command=listbox.yview
    )
    
    listbox['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=422,y=104,height=370)

    scrollbar = Scrollbar(
        importframe,
        orient='horizontal',
        
        command=listbox.xview
    )
    
    listbox['xscrollcommand'] = scrollbar.set
    scrollbar.place(x=12,y=474,width=427)



       


    lb1=Label(importframe,text="Select import source XLs file first after build column associations").place(x=10,y=500)

    def callback(url):
        webbrowser.open_new(url)

    
    link1 = Label(importframe, text="More info", fg="blue", cursor="hand2")
    link1.place(x=360,y=500)
    link1.bind("<Button-1>", lambda e: callback("https://f-billing.com/faq.php"))

  
        
        
     
      
    importbutton=Button(top,command=export_customer,image=folder,compound=LEFT)
    importbutton.place(x=410,y=40,height=25,width=30)

    lb1=Label(importframe,text="     Please associate datafields with data columns").place(x=500,y=10)

    id1=Label(importframe,text="CUSTOMER ID = ",fg="blue")
    id1.place(x=460,y=40)
    no = StringVar() 
    idd = ttk.Combobox(importframe, width = 27, textvariable = no ) 
      
    # Adding combobox drop down list 
    idd['values'] = ('    -NotAssociated-')
      
    idd.place(x=580,y=40,height=23) 
    idd.current(0)

    name1=Label(importframe,text="CUSTOMER NAME = ",fg="blue")
    name1.place(x=460,y=65)
    namevar = StringVar() 
    name = ttk.Combobox(importframe, width = 27, textvariable = namevar ) 
      
    # Adding combobox drop down list 
    name['values'] = ('    -NotAssociated-' 
                              )
      
    name.place(x=580,y=65,height=23) 
    name.current(0)


    category1=Label(importframe,text="CATEGORY = ",fg="blue")
    category1.place(x=460,y=90)
    categoryvar = StringVar() 
    category = ttk.Combobox(importframe, width = 27, textvariable = categoryvar ) 
      
    # Adding combobox drop down list 
    category['values'] = ('    -NotAssociated-' 
                              )
      
    category.place(x=580,y=90,height=23) 
    category.current(0)

    add=Label(importframe,text="ADDRESS = ",fg="blue")
    add.place(x=460,y=115)
    addvar = StringVar() 
    addc = ttk.Combobox(importframe, width = 27, textvariable = addvar ) 
      
    # Adding combobox drop down list 
    addc['values'] = ('    -NotAssociated-' 
                              )
      
    addc.place(x=580,y=115,height=23) 
    addc.current(0)

    tel1=Label(importframe,text="TEL.= ")
    tel1.place(x=460,y=140)
    telvar = StringVar() 
    telc = ttk.Combobox(importframe, width = 27, textvariable = telvar ) 
      
    # Adding combobox drop down list 
    telc['values'] = ('    -NotAssociated-' 
                              )
      
    telc.place(x=580,y=140,height=23) 
    telc.current(0)

    fax1=Label(importframe,text="FAX = ")
    fax1.place(x=460,y=165)
    faxvar = StringVar() 
    faxc = ttk.Combobox(importframe, width = 27, textvariable = faxvar ) 
      
    # Adding combobox drop down list 
    faxc['values'] = ('    -NotAssociated-' 
                              )
      
    faxc.place(x=580,y=165,height=23) 
    faxc.current(0)

    email1=Label(importframe,text="EMAIL = ")
    email1.place(x=460,y=190)
    emailvar = StringVar() 
    emailc = ttk.Combobox(importframe, width = 27, textvariable = emailvar ) 
      
    # Adding combobox drop down list 
    emailc['values'] = ('    -NotAssociated-'
                              )
      
    emailc.place(x=580,y=190,height=23) 
    emailc.current(0)


    cp1=Label(importframe,text="CONTACT PERSION = ")
    cp1.place(x=460,y=215)
    cpvar = StringVar() 
    cp = ttk.Combobox(importframe, width = 27, textvariable = cpvar ) 
      
    # Adding combobox drop down list 
    cp['values'] = ('    -NotAssociated-' 
                              )
      
    cp.place(x=580,y=215,height=23) 
    cp.current(0)

    sn2=Label(importframe,text="SHIP TO NAME = ")
    sn2.place(x=460,y=240)
    snvar = StringVar() 
    sn = ttk.Combobox(importframe, width = 27, textvariable = snvar ) 
      
    # Adding combobox drop down list 
    sn['values'] = ('    -NotAssociated-' 
                              )
      
    sn.place(x=580,y=240,height=23) 
    sn.current(0)

    saa2=Label(importframe,text="SHIP TO ADDESS = ")
    saa2.place(x=460,y=265)
    saa2var = StringVar() 
    saa = ttk.Combobox(importframe, width = 27, textvariable = saa2var ) 
      
    # Adding combobox drop down list 
    saa['values'] = ('    -NotAssociated-')
      
    saa.place(x=580,y=265,height=23) 
    saa.current(0)


    stt2=Label(importframe,text="SHIP TO TEL. = ")
    stt2.place(x=460,y=290)
    stt2var = StringVar() 
    stt = ttk.Combobox(importframe, width = 27, textvariable = stt2var ) 
      
    # Adding combobox drop down list 
    stt['values'] = ('    -NotAssociated-' 
                              )
      
    stt.place(x=580,y=290,height=23) 
    stt.current(0)


    stf2=Label(importframe,text="SHIP TO FAX = ")
    stf2.place(x=460,y=315)
    stf2var = StringVar() 
    stf = ttk.Combobox(importframe, width = 27, textvariable = stf2var ) 
      
    # Adding combobox drop down list 
    stf['values'] = ('    -NotAssociated-' 
                              )
      
    stf.place(x=580,y=315,height=23) 
    stf.current(0)


    dd2=Label(importframe,text="DISCOUNT = ")
    dd2.place(x=460,y=340)
    dd2var = StringVar() 
    dd = ttk.Combobox(importframe, width = 27, textvariable = dd2var) 
      
    # Adding combobox drop down list 
    dd['values'] = ('    -NotAssociated-'
                              )
      
    dd.place(x=580,y=340,height=23) 
    dd.current(0)

    st112=Label(importframe,text="SPECIAL TAX 1 = ")
    st112.place(x=460,y=365)
    st112var = StringVar() 
    st11 = ttk.Combobox(importframe, width = 27, textvariable = st112var ) 
      
    # Adding combobox drop down list 
    st11['values'] = ('    -NotAssociated-' 
                              )
      
    st11.place(x=580,y=365,height=23) 
    st11.current(0)

    st222=Label(importframe,text="SPECIAL TAX 2 = ")
    st222.place(x=460,y=390)
    st222var = StringVar() 
    st22 = ttk.Combobox(importframe, width = 27, textvariable = st222var ) 
      
    # Adding combobox drop down list 
    st22['values'] = ('    -NotAssociated-'
                              )
      
    st22.place(x=580,y=390,height=23) 
    st22.current(0)

    vrn2=Label(importframe,text="VAT REG.NUMBER = ")
    vrn2.place(x=460,y=415)
    vrn2var = StringVar() 
    vrn = ttk.Combobox(importframe, width = 27, textvariable = vrn2var ) 
      
    # Adding combobox drop down list 
    vrn['values'] = ('    -NotAssociated-' 
                              )
      
    vrn.place(x=580,y=415,height=23) 
    vrn.current(0)

    avt2=Label(importframe,text="ACTIVE = ")
    avt2.place(x=460,y=440)
    avt2var = StringVar() 
    avt = ttk.Combobox(importframe, width = 27, textvariable = avt2var ) 
      
    # Adding combobox drop down list 
    avt['values'] = ('    -NotAssociated-'
                              )
      
    avt.place(x=580,y=440,height=23) 
    avt.current(0)

    tee2=Label(importframe,text="TAX EXEMPTED= ")
    tee2.place(x=460,y=465)
    teevar = StringVar() 
    tee= ttk.Combobox(importframe, width = 27, textvariable = teevar ) 
      
    # Adding combobox drop down list 
    tee['values'] = ('    -NotAssociated-' 
                              )
      
    tee.place(x=580,y=465,height=23) 
    tee.current(0)

    btn=Button(importframe,text="Clear associations", width=15,).place(x=560, y=500)
    btn=Button(importframe, text="Next", width=10,).place(x=685, y=500)     



  
    
    top.mainloop()

#export_customer

def export_customer():
    name = askopenfilename(filetypes=[('Excel', ('*.xls', '*.xslm', '*.xlsx')),('CSV', '*.csv',)])

    if name:
        if name.endswith('.csv'):
            df = pd.read_csv(name)
        else:
            df = pd.read_excel(name)

            filename = name

           
            










#Search in Customers

def search_customers():
    top = Toplevel()  
    
    top.title("Find Text")
    
 
    
  
    p2 = PhotoImage(file = "images/fbicon.png")
    top.iconphoto(False, p1)
 
    
   
    
    top.geometry("520x180+390+250")
    findwhat1=Label(top,text="Find What:")
    findwhat1.place(x=5,y=15)
    n = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = n ) 
      
    # Adding combobox drop down list 
    
    findwhat.place(x=85,y=15,height=23) 
    

    findButton = Button(top, text ="Find next",width=10)
    findButton.place(x=420,y=15)

    findin1=Label(top,text="Find in:")
    findin1.place(x=5,y=40)
    n = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable = n ) 
      
    # Adding combobox drop down list 
    findIN['values'] = ('Customer name',  
                              'Customer ID', 
                              'Category', 
                              'Customer name', 
                              'Contact Person', 
                              'Customer Tel.', 
                              'SMS number',
                              'Type',
                              '<<All>>') 
      
    findIN.place(x=85,y=40,height=23) 
    findIN.current(0)

    closeButton = Button(top, text ="Close",width=10)
    closeButton.place(x=420,y=45)

    match1=Label(top,text="Match:")
    match1.place(x=5,y=65)
    n = StringVar() 
    match = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    match['values'] = ('From any part of the field','Whole field',  
                              'From beging of field')
      
    match.place(x=85,y=65,height=23) 
    match.current(0)

    search1=Label(top,text="Search:")
    search1.place(x=5,y=90)
    n = StringVar() 
    search = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    search['values'] = ('Up','Down','All')
      
    search.place(x=85,y=90,height=23) 
    #search.current(0)


    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(top,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=60,y=120)

    checkvarStatus5=IntVar()
   
    Button5 = Checkbutton(top,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button5.place(x=270,y=120)





    top.mainloop()

#refresh
def refresh_customers(self):
  
    self.destroy()
    self.__init__()
 



######################## FRONT PAGE OF CUSTOMER SECTION #######################################################################

    
mainFrame=Frame(tab7, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(5, 2))
pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

addcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_add.png"))
addcustomerLabel = Button(midFrame,compound="top", text="Add new\nCustomer",relief=RAISED,  command=add_customer,          image=addcustomerIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)

addcustomerLabel.pack(side="left", pady=3, ipadx=4)

editcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_edit.png"))
editcustomerLabel = Button(midFrame,compound="top", text="Edit/View\nCustomer",relief=RAISED,command=edit_customer, image=editcustomerIcon,  font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)

editcustomerLabel.pack(side="left")

deletecustomerIcon = ImageTk.PhotoImage(Image.open("images/user_delete.png"))
deletecustomerLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, command=delete_customer,image=deletecustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)

deletecustomerLabel.pack(side="left")



pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)



previewinvoiceIcon = ImageTk.PhotoImage(Image.open("images/priewok.png"))
previewinvoiceLabel = Button(midFrame,compound="top", text="Preview\nInvoice List",relief=RAISED,               image=previewinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
previewinvoiceLabel.pack(side="left")

printinvoiceIcon = ImageTk.PhotoImage(Image.open("images/printer.png"))
printinvoiceLabel = Button(midFrame,compound="top", text="Print\n Invoice List",relief=RAISED,  command=printinvoice, image=printinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
printinvoiceLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

emailinviceIcon = ImageTk.PhotoImage(Image.open("images/gmail.png"))
emailinviceLabel = Button(midFrame,compound="top",command=emailinvoice, text="E-mail\nInvoice List",relief=RAISED,               image=emailinviceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
emailinviceLabel.pack(side="left")

smsIcon = ImageTk.PhotoImage(Image.open("images/text-message.png"))
smsLabel = Button(midFrame,compound="top", text="Send SMS\nNotification",command=customersms, relief=RAISED, image=smsIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
smsLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

importcustomerIcon = ImageTk.PhotoImage(Image.open("images/import.png"))
importcustomerLabel = Button(midFrame,compound="top", text="Import\nCustomers",command=import_customer,relief=RAISED, image=importcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
importcustomerLabel.pack(side="left")

exportcustomerIcon = ImageTk.PhotoImage(Image.open("images/export-file.png"))
exportcustomerLabel = Button(midFrame,compound="top", text="Export\nCustomers",command=export_customer,relief=RAISED, image=exportcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
exportcustomerLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)


customersearchIcon = ImageTk.PhotoImage(Image.open("images/search-icon.png"))
customersearchLabel = Button(midFrame,compound="top",command=search_customers, text="Search in\nCustomers",relief=RAISED,               image=customersearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
customersearchLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)


refreshcustomerIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
refreshcustomerLabel = Button(midFrame,compound="top", command=refresh_customers,text="Refresh\ncustomer list",relief=RAISED,               image=refreshcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
refreshcustomerLabel.pack(side="left")








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
