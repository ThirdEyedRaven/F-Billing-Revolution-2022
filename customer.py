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

    propert.title("Microsoft Print To PDF Advanced Document Settings")
    p2 = PhotoImage(file = "images/fbicon.png")
    propert.iconphoto(False, p1)
    propert.geometry("580x470+380+210")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
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
emailinviceLabel = Button(midFrame,compound="top", text="E-mail\nInvoice List",relief=RAISED,               image=emailinviceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
emailinviceLabel.pack(side="left")

smsIcon = ImageTk.PhotoImage(Image.open("images/text-message.png"))
smsLabel = Button(midFrame,compound="top", text="Send SMS\nNotification",relief=RAISED, image=smsIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
smsLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

importcustomerIcon = ImageTk.PhotoImage(Image.open("images/import.png"))
importcustomerLabel = Button(midFrame,compound="top", text="Export\nCustomers",relief=RAISED, image=importcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
importcustomerLabel.pack(side="left")

exportcustomerIcon = ImageTk.PhotoImage(Image.open("images/export-file.png"))
exportcustomerLabel = Button(midFrame,compound="top", text="Export\nCustomers",relief=RAISED, image=exportcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
exportcustomerLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)


customersearchIcon = ImageTk.PhotoImage(Image.open("images/search-icon.png"))
customersearchLabel = Button(midFrame,compound="top",command=search_customers, text="Search in\nCustomers",relief=RAISED,               image=customersearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
customersearchLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)


refreshcustomerIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
refreshcustomerLabel = Button(midFrame,compound="top", text="Refresh\ncustomer list",relief=RAISED,               image=refreshcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
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
