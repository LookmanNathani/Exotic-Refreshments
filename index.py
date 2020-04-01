from tkinter import *
from tkinter import messagebox
import time
import pymysql

# Window and frame elements
me = Tk()
me.geometry('1280x720')
me.configure(bg='#114D96')

# Declaring Variables
a = b = c = d = e = 0

# Methods for buttons
def onClick1(event=None):
    global a
    a += 1

    e1 = Entry(me, width=8)
    e1.insert(0, a)
    e1.place(x=120, y=450)
    disp_total()


def onClick2(event=None):
    global b
    b+=1

    e2 = Entry(me, width=8)
    e2.insert(0,b)
    e2.place(x=490, y=450)
    disp_total()


def onClick3(event=None):
    global c
    c += 1
    e3 = Entry(me, width=8)
    e3.insert(0,c)
    e3.place(x=920, y=450)
    disp_total()


def onClick4(event=None):
    global d
    d+=1
    e4 = Entry(me, width=8)
    e4.insert(0,d)
    e4.place(x=110, y=740)
    disp_total()


def onClick5(event=None):
    global e
    e+=1
    e5 = Entry(me, width=8)
    e5.insert(0,e)
    e5.place(x=500, y=740)
    disp_total()

#----------------------------------Remove Function-------------------------------------
def remove_a():
    global a
    if(a>0):
        a-=1
        e1 = Entry(me, width=8)
        e1.insert(0, a)
        e1.place(x=120, y=450)
        disp_total()

def remove_b():
    global b
    if (b>0):
        b-=1
        e2 = Entry(me, width=8)
        e2.insert(0, b)
        e2.place(x=490, y=450)
        disp_total()

def remove_c():
    global c
    if (c > 0):
        c -= 1
        e3 = Entry(me, width=8)
        e3.insert(0, c)
        e3.place(x=920, y=450)
        disp_total()

def remove_d():
    global d
    if (d > 0):
        d -= 1
        e4 = Entry(me, width=8)
        e4.insert(0, d)
        e4.place(x=110, y=740)
        disp_total()

def remove_e():
    global e
    if (e > 0):
        e -= 1
        e5 = Entry(me, width=8)
        e5.insert(0, e)
        e5.place(x=500, y=740)
        disp_total()

# ------------------------------- BILLING FUNCTIONS -----------------------------------

def calculate():
    number = no_entry.get()
    name = name_entry.get()
    if((len(number) == 8 or len(number) == 10) and number.isdigit()):
        conn = pymysql.connect(host='localhost', user='root', password='', db='refreshment')
        a = conn.cursor()
        sql = "INSERT INTO customer (name,number) VALUES(%s, %s)";
        a.execute(sql,(name,number))
        conn.commit()

        global win2
        win2 = Tk()
        win2.config(bg='#DEB887')
        bill()
        win2.geometry("1366x768")
        win2.mainloop()
    else:
        messagebox.showerror("Error", "Invalid Credentials")

def bill():
    global price
    price = [70, 40, 50, 120, 30]
    item_name = ['Cappuccino','Coca-Cola','Tea','Frappaccino','Mango Juice']
    global l1

    title = Label(win2, text="Exotic Refreshments", fg='#000080', font=('Comic Sans MS', 15)).pack(side=TOP)

    user_l = Label(win2,text="Customer Name: "+name_entry.get(),font=("arial", 20)).place(x= 350 , y = 40)
    user_l2 = Label(win2,text='Mobile Number: '+no_entry.get(),font=("arial", 20)).place(x = 700, y = 40)

    l1 = Label(win2 , text = "Item Name" , font = ("arial" , 24) , fg = '#000080' , bg = '#DEB887')
    l2 = Label(win2, text="Unit", font=("arial", 24) , fg = '#000080' , bg = '#DEB887')
    l3 = Label(win2, text="Price", font=("arial", 24) , fg = '#000080' , bg = '#DEB887')
    l4 = Label(win2, text="Amount", font=("arial", 24) , fg = '#000080' , bg = '#DEB887')

    if(a>0):
        total = a * price[0]
        l5 = Label(win2 , bg = '#DEB887', text = ""+item_name[0]+"               "+""+str(a)+"          x            "+str(price[0])+"             =              "+""+str(total), font = ('arial',18))
        l5.place(x= 375 , y = 150)

    if (b > 0):
        total1 = b * price[1]
        l6 = Label(win2, bg = '#DEB887', text="" + item_name[1] + "                 " + "" + str(b) + "           x          " + str(price[1]) + "               =             " + "" + str(total1), font=('arial', 18))
        l6.place(x=375, y=180)

    if (c > 0):
        total2 = c * price[2]
        l7 = Label(win2, bg = '#DEB887', text="" + item_name[2] + "                           " + "" + str(c) + "            x         " + str(price[2]) + "               =              " + "" + str(total2), font=('arial', 18))
        l7.place(x=375, y=210)

    if (d > 0):
        total3 = d * price[3]
        l8 = Label(win2, bg = '#DEB887', text="" + item_name[3] + "               " + "" + str(d) + "         x          " + str(price[3]) + "               =             " + "" + str(total3), font=('arial', 18))
        l8.place(x=375, y=240)

    if (e > 0):
        total4 = e * price[4]
        l9 = Label(win2, bg = '#DEB887', text="" + item_name[4] + "               " + "" + str(e) + "         x          " + str(price[4]) + "               =             " + "" + str(total4), font=('arial', 18))
        l9.place(x=375, y=270)

    if(a>0 or b>0 or c>0 or d>0 or e>0):
        total_price = (a * price[0]) + (b * price[1]) + (c * price[2]) + (d * price[3]) + (e * price[4])
        l9 = Label(win2 , bg = '#DEB887', text = "YOUR TOTAL AMOUNT IS "+str(total_price)+" Rs" , font = ('arial' , 26))
        l10 = Label(win2 , bg = '#DEB887', text = "THANKS FOR BUYING FROM US !" , font = ('arial' , 28))
        l9.place(x=390, y=310)
        l10.place(x=360, y=400)
    else:
        l11 = Label(win2 , bg = '#DEB887', text = "PLEASE ADD ITEMS TO YOUR CART !" , fg = 'red', font = ("arial" , 28))
        l11.place(x= 380 , y= 350)

    l1.place(x= 340 , y = 80)
    l2.place(x= 580 , y = 80)
    l3.place(x = 760 , y = 80)
    l4.place(x= 960 , y = 80)

# Heading
hlabel = Label(me, text="Exotic Refreshments", fg='white', bg='#114D96', pady=12, font=('Comic Sans MS', 35)).pack(
    side='top')

# Current time info
t = time.ctime()
t_label = Label(me, text=t, font=("Times New Roman", 18), fg='yellow', bg='#114D96')
t_label.pack()

# User Details
name_lbl = Label(me, text='Customer Name', font=("Times New Roman", 18), bg='#114D96', fg='white').place(x=70, y=160)
name_entry = Entry(me, width=30)
name_entry.place(x=250, y=170)

no_lbl = Label(me, text='Phone No', font=("Times New Roman", 18), bg='#114D96', fg='white').place(x=500, y=160)
no_entry = Entry(me, width=30)
no_entry.place(x=610, y=170)



# Image Buttons
photo1 = PhotoImage(file="cappuccino.png")
b1 = Button(me, image=photo1, height=200, width=210,command=onClick1)
b1.place(x=80, y=240)
e1 = Entry(me, width=8)
e1.place(x=120, y=450)
r1 = Button(me, width=8, text='Remove', bg='yellow', fg='red', command=remove_a).place(x=180, y=450)

photo2 = PhotoImage(file="cocacola.png")
b2 = Button(me, image=photo2, height=200, width=299,command=onClick2)
b2.place(x=420, y=240)
e2 = Entry(me, width=8).place(x=490, y=450)
r2 = Button(me, width=8, text='Remove', bg='yellow', fg='red',command=remove_b).place(x=550, y=450)

photo3 = PhotoImage(file="tea.png")
b3 = Button(me, image=photo3, height=200, width=244,command=onClick3)
b3.place(x=850, y=240)
e3 = Entry(me, width=8).place(x=920, y=450)
r3 = Button(me, width=8, text='Remove', bg='yellow', fg='red',command=remove_c).place(x=980, y=450)

photo4 = PhotoImage(file="frappaccino.png")
b4 = Button(me, image=photo4, height=200, width=195,command=onClick4)
b4.place(x=80, y=530)
e4 = Entry(me, width=8).place(x=110, y=740)
r4 = Button(me, width=8, text='Remove', bg='yellow', fg='red',command=remove_d).place(x=170, y=740)

photo5 = PhotoImage(file="mango.png")
b5 = Button(me, image=photo5, height=200, width=200,command=onClick5)
b5.place(x=450, y=530)
e5 = Entry(me, width=8).place(x=500, y=740)
r5 = Button(me, width=8, text='Remove', bg='yellow', fg='red',command=remove_e).place(x=560, y=740)

# Billing and total amount buttons
def disp_total():
    total = a*70+b*40+c*50+d*120+e*30
    if(total < 0):
        total = 0
    Label(me, text='Your total amount is: ', fg='red', bg='#114D96',
          font=("Times New Roman", 22)).place(x=850, y=570)
    t_entry = Entry(me,width=5,font=("Courier New", 12, 'bold'))
    t_entry.delete(0,'end')
    t_entry.insert(0,total)
    t_entry.place(x=1100,y=580)

bill_btn = Button(me, text='Generate Bill',command=calculate,bg='red', fg="white", width=16, height=2, font=('Arial', 16)).place(x=860,
                                                                                                            y=630)

# ******************************CALCULATOR*********************************
textin = StringVar()
operator = ""


def clickbut(number):  # lambda:clickbut(1)
    global operator
    operator = operator + str(number)
    textin.set(operator)


def equlbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''


def equlbut():
    global operator
    sub = str(eval(operator))
    textin.set(sub)
    operator = ''


def equlbut():
    global operator
    mul = str(eval(operator))
    textin.set(mul)
    operator = ''


def equlbut():
    global operator
    div = str(eval(operator))
    textin.set(div)
    operator = ''


def clrbut():
    textin.set('')


metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=32, bd=5, bg='powder blue')
metext.place(x=1200, y=55 + 150)

but1 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(1), text="1",
              font=("Courier New", 16, 'bold'))
but1.place(x=10 + 1190, y=100 + 150)

but2 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(2), text="2",
              font=("Courier New", 16, 'bold'))
but2.place(x=10 + 1190, y=170 + 150)

but3 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(3), text="3",
              font=("Courier New", 16, 'bold'))
but3.place(x=10 + 1190, y=240 + 150)

but4 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(4), text="4",
              font=("Courier New", 16, 'bold'))
but4.place(x=75 + 1190, y=100 + 150)

but5 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(5), text="5",
              font=("Courier New", 16, 'bold'))
but5.place(x=75 + 1190, y=170 + 150)

but6 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(6), text="6",
              font=("Courier New", 16, 'bold'))
but6.place(x=75 + 1190, y=240 + 150)

but7 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(7), text="7",
              font=("Courier New", 16, 'bold'))
but7.place(x=140 + 1190, y=100 + 150)

but8 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(8), text="8",
              font=("Courier New", 16, 'bold'))
but8.place(x=140 + 1190, y=170 + 150)

but9 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(9), text="9",
              font=("Courier New", 16, 'bold'))
but9.place(x=140 + 1190, y=240 + 150)

but0 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(0), text="0",
              font=("Courier New", 16, 'bold'))
but0.place(x=10 + 1190, y=310 + 150)

butdot = Button(me, padx=47, pady=14, bd=4, bg='white', command=lambda: clickbut("."), text=".",
                font=("Courier New", 16, 'bold'))
butdot.place(x=75 + 1190, y=310 + 150)

butpl = Button(me, padx=14, pady=14, bd=4, bg='white', text="+", command=lambda: clickbut("+"),
               font=("Courier New", 16, 'bold'))
butpl.place(x=205 + 1190, y=100 + 150)

butsub = Button(me, padx=14, pady=14, bd=4, bg='white', text="-", command=lambda: clickbut("-"),
                font=("Courier New", 16, 'bold'))
butsub.place(x=205 + 1190, y=170 + 150)

butml = Button(me, padx=14, pady=14, bd=4, bg='white', text="*", command=lambda: clickbut("*"),
               font=("Courier New", 16, 'bold'))
butml.place(x=205 + 1190, y=240 + 150)

butdiv = Button(me, padx=14, pady=14, bd=4, bg='white', text="/", command=lambda: clickbut("/"),
                font=("Courier New", 16, 'bold'))
butdiv.place(x=205 + 1190, y=310 + 150)

butclear = Button(me, padx=14, pady=119, bd=4, bg='white', text="CE", command=clrbut, font=("Courier New", 16, 'bold'))
butclear.place(x=270 + 1190, y=100 + 150)

butequal = Button(me, padx=151, pady=14, bd=4, bg='white', command=equlbut, text="=", font=("Courier New", 16, 'bold'))
butequal.place(x=10 + 1190, y=380 + 150)


me.mainloop()
