from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("WELCOME TO STUDENTS MANAGEMENT SYSTEM")
root.geometry("600x400")
root.resizable(0, 0)
f55=None
r1 = StringVar()
r2 = StringVar()
r3 = StringVar()
g1 = StringVar()
g2 = StringVar()
s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()
a1 = StringVar()
b1 = StringVar()
d1 = StringVar()
d2 = StringVar()
d3 = StringVar()
d4 = StringVar()
e1 = StringVar()


def login():
    f2 = Frame(bg="#091e42")
    f2.place(x=0, y=0, width=600, height=400)
    u5 = Label(f2, text="Enter Name", bg="#091e42", fg="white")
    u5.place(x=200, y=50)
    e5 = Entry(f2, font=("", 11), textvariable=g1)
    e5.place(x=300, y=50, width=130)

    up = Label(f2, text="Enter Password", bg="#091e42", fg="white")
    up.place(x=200, y=100)
    ep = Entry(f2, font=("", 11), textvariable=g2,show="*")
    ep.place(x=300, y=100, width=130)

    kl = Button(f2, text="LOGIN", bg="#091e42", fg="white", command=logo)
    kl.place(x=260, y=160, width=100, height=40)

    vb = Button(f2, text="HOME", bg="#091e42", fg="white", command=home)
    vb.place(x=15, y=340)

    bv = Button(f2, text="REGISTER", bg="#091e42", fg="white", command=register)
    bv.place(x=480, y=340)


def register():
    f3 = Frame(bg="#091e42")
    f3.place(x=0, y=0, width=600, height=400)

    q = Label(f3, text="Enter Name", bg="#091e42", fg="white")
    q.place(x=200, y=50)
    r = Entry(f3, font=("", 11), textvariable=r1)
    r.place(x=300, y=50, width=130)

    m = Label(f3, text="Enter Password", bg="#091e42", fg="white")
    m.place(x=200, y=100)
    b = Entry(f3, font=("", 11), textvariable=r2, show="*")
    b.place(x=300, y=100, width=130)

    l = Label(f3, text="Enter C.N.", bg="#091e42", fg="white")
    l.place(x=200, y=150)
    t = Entry(f3, font=("", 11), textvariable=r3)
    t.place(x=300, y=150, width=130)
    j = Button(f3, text="REGISTER", bg="#091e42", fg="white", command=tq)
    j.place(x=260, y=200, width=100, height=40)
    x = Button(f3, text="HOME", bg="#091e42", fg="white", command=home)
    x.place(x=15, y=340)
    h = Button(f3, text="LOGIN", bg="#091e42", fg="white", command=login)
    h.place(x=480, y=340)


def tq():
    db = sqlite3.connect('vivek.db')
    cr = db.cursor()
    cr.execute("insert into bb values('" + r1.get() + "','" + r2.get() + "','" + r3.get() + "')")
    db.commit()
    db.close()
    messagebox.showinfo('Title', 'User Register')
    r1.set("")
    r2.set("")
    r3.set("")


def logo():
    db = sqlite3.connect('vivek.db')
    cr = db.cursor()
    r = cr.execute("select * from bb where NAME='" + g1.get() + "' AND PASSWORD='" + g2.get() + "'")
    for r1 in r:
        mymenu()
        break
    else:
        messagebox.showinfo('Title', 'INVALID ENTRY')
    db.commit()
    db.close()
    g1.set("")
    g2.set("")

def mymenu()   :
    n=ttk.Notebook()
    n.place(x=0,y=0,width=600,height=400)

    def demo(a):
      if n.index("current")==5:
       home()
    n.bind("<<NotebookTabChanged>>", demo)


    insertdata(n)
    showalldata(n)
    searchdata(n)
    updatedata(n)
    deletedata(n)
    logoutdata(n)
def showthedata(f5)   :
    for w in f5.winfo_children():
        w.destroy()

    s=Label(f5,text="Roll No",font=("Arial",11),bg="#091e42",fg="white")
    s.place(x=0,y=0,width=120)

    r = Label(f5, text="NAME", font=("Arial", 11), bg="#091e42", fg="white")
    r.place(x=120, y=0, width=120)

    o = Label(f5, text="PHYSICS", font=("Arial", 11), bg="#091e42", fg="white")
    o.place(x=240, y=0, width=120)

    m = Label(f5, text="CHEMISTRY", font=("Arial", 11), bg="#091e42", fg="white")
    m.place(x=360, y=0, width=120)

    d = Label(f5, text="MATHS", font=("Arial", 11), bg="#091e42", fg="white")
    d.place(x=480, y=0, width=120)
    db = sqlite3.connect('vivek.db')
    cr = db.cursor()
    r=cr.execute("select * from aa")
    x=0
    y=60
    for r1 in r:
        Label(f5, text=r1[0], font=("Arial", 11), bg="#091e42", fg="white").place(x=x,y=y,width=120)
        x+=120
        Label(f5, text=r1[1], font=("Arial", 11), bg="#091e42", fg="white").place(x=x, y=y, width=120)
        x+=120
        Label(f5, text=r1[2], font=("Arial", 11), bg="#091e42", fg="white").place(x=x, y=y, width=120)
        x += 120
        Label(f5, text=r1[3], font=("Arial", 11), bg="#091e42", fg="white").place(x=x, y=y, width=120)
        x += 120
        Label(f5, text=r1[4], font=("Arial", 11), bg="#091e42", fg="white").place(x=x, y=y, width=120)
        x += 120

        y+=40
        x=0

        y+=40



    db.commit()
    db.close()














def insertdata(n) :
    f4=Frame(bg="#091e42")
    n.add(f4,text="Insert")
    rt=Label(text="Enter Roll No",font=("Arial",11),bg="#091e42",fg="White")
    rt.place(x=200,y=50)
    tr=Entry(font=("Arial",11),textvariable=s1)
    tr.place(x=300,y=50,width=130)

    op = Label(text="Enter Name", font=("Arial", 11), bg="#091e42", fg="White")
    op.place(x=200, y=100)
    bn = Entry(font=("Arial", 11),textvariable=s2)
    bn.place(x=300, y=100, width=130)

    mm = Label(text="Enter Physics", font=("Arial", 11), bg="#091e42", fg="White")
    mm.place(x=200, y=150)
    nn = Entry(font=("Arial", 11),textvariable=s3)
    nn.place(x=300, y=150, width=130)

    zz = Label(text="Enter Chem", font=("Arial", 11), bg="#091e42", fg="White")
    zz.place(x=200, y=200)
    qo = Entry(font=("Arial", 11),textvariable=s4)
    qo.place(x=300, y=200, width=130)

    uu = Label(text="Enter Maths", font=("Arial", 11), bg="#091e42", fg="White")
    uu.place(x=200, y=250)
    gz = Entry(font=("Arial", 11),textvariable=s5)
    gz.place(x=300, y=250, width=130)



    yy=Button(f4,text="Insert",command=insertdemo1)
    yy.place(x=260,y=330,width=80,height=40)










def insertdemo1():
    db = sqlite3.connect('vivek.db')
    cr = db.cursor()
    cr.execute("insert into aa values('" + s1.get() + "','" + s2.get() + "','"+s3.get()+"','"+s4.get()+"',+'"+s5.get()+"')")
    db.commit()
    db.close()
    messagebox.showinfo('Title', 'Data Inserted')
    r1.set("")
    r2.set("")
    r3.set("")
    showthedata(f55)
















def showalldata(n)   :
    f5=Frame(bg="#091e42")
    n.add(f5,text="ShowAll")
    global f55
    f55=f5

    showthedata(f5)
def searchdata(n):
    f6=Frame(bg="#091e42")
    n.add(f6,text="Search")
    global f56
    f56=f6
    iii = Label(f6,text="Enter Roll No", font=("Arial", 11), bg="#091e42", fg="White")
    iii.place(x=100, y=100)
    fff = Entry(f6,font=("Arial", 11),textvariable=a1)
    fff.place(x=200, y=100, width=130)
    hh = Button(f6, text="Search", font=("Arial", 11), command=searchdata1)
    hh.place(x=360, y=100, height=25)


def searchdata1():



    db = sqlite3.connect('vivek.db')
    cr = db.cursor()
    r = cr.execute("select * from aa where URNO='" + a1.get() + "' ")
    for r1 in r:
        xx = Label(f56,font=("Arial",11), text="Name is",bg="#091e42",fg="White")
        xx.place(x=100, y=160)
        tr=Label(f56,font=("",11),text=r1[1],bg="#091e42",fg="White")
        tr.place(x=240,y=160)

        s = Label(f56,font=("Arial", 11), text="Physics Marks is", bg="#091e42", fg="White")
        s.place(x=100, y=180)
        gx = Label(f56,font=("", 11), text=r1[2], bg="#091e42", fg="White")
        gx.place(x=240, y=180)



        nb = Label(f56,font=("Arial", 11), text="Chemistry Marks is", bg="#091e42",fg="White")
        nb.place(x=100, y=200)
        uui = Label(f56,font=("", 11), text=r1[3],bg="#091e42",fg="White")
        uui.place(x=240, y=200)

        ds = Label(f56,font=("Arial", 11), text="Maths Marks is", bg="#091e42",fg="White")
        ds.place(x=100, y=220)
        bg = Label(f56,font=("", 11), text=r1[4],bg="#091e42",fg="White")
        bg.place(x=240, y=220)

        break

    else:
        messagebox.showinfo('Title','Invalid Roll No')
        uuu = Label(f56,font=("Arial", 11), text="", bg="#091e42", fg="White")
        uuu.place(x=100, y=160,width=300)

        kkk = Label(f56,font=("Arial", 11), text="", bg="#091e42", fg="White")
        kkk.place(x=100, y=180,width=300)

        bbb = Label(f56,font=("Arial", 11), text="", bg="#091e42",fg="White")
        bbb.place(x=100, y=200,width=300)

        ooo = Label(f56,font=("Arial", 11), text="", bg="#091e42", fg="White")
        ooo.place(x=100, y=220,width=300)











    db.commit()
    db.close()








def updatedata(n) :
    f7=Frame(bg="#091e42")
    n.add(f7,text="Update")
    global f57
    f57=f7
    iii = Label(f7, text="Enter Roll No", font=("Arial", 11), bg="#091e42", fg="White")
    iii.place(x=100, y=100)
    fff = Entry(f7, font=("Arial", 11),textvariable=b1)
    fff.place(x=200, y=100, width=130)
    hhh = Button(f7, text="Update", font=("Arial", 11), command=updatedata1)
    hhh.place(x=360, y=100, height=25)


def updatedata1():
        db = sqlite3.connect('vivek.db')
        cr = db.cursor()
        r = cr.execute("select * from aa where URNO='" + b1.get() + "' ")
        for r1 in r:
            sss = Label(f57,font=("Arial", 11), text="Name is", bg="#091e42", fg="White")
            sss.place(x=100, y=160)
            yu = Entry(f57,font=("", 11),textvariable=d1,fg="White",bg="#091e42")
            yu.insert(0,r1[1])
            yu.place(x=240, y=160)

            sss = Label(f57,font=("Arial", 11), text="Physics is", bg="#091e42", fg="White")
            sss.place(x=100, y=180)
            yu = Entry(f57,font=("", 11),textvariable=d2, fg="White",bg="#091e42")
            yu.insert(0,r1[2])
            yu.place(x=240, y=180)

            sss = Label(f57,font=("Arial", 11), text="Chemistry", bg="#091e42", fg="White")
            sss.place(x=100, y=200)
            yu = Entry(f57,font=("", 11),textvariable=d3, fg="White",bg="#091e42")
            yu.insert(0,r1[3])
            yu.place(x=240, y=200)

            sss = Label(f57,font=("Arial", 11), text="Maths is", bg="#091e42", fg="White")
            sss.place(x=100, y=220)
            yu = Entry(f57,font=("", 11),textvariable=d4, fg="White",bg="#091e42")
            yu.insert(0,r1[4])
            yu.place(x=240, y=220)

            b7 = Button(f57,font=("Arial", 11), text="Update", command=updatedata2)
            b7.place(x=250, y=310, width=80)

            break

        else:
            messagebox.showinfo('Title', 'Invalid Roll No')
            uuu = Label(f57,font=("Arial", 11), text="", bg="#091e42", fg="White")
            uuu.place(x=100, y=160, width=300)

            kkk = Label(f57,font=("Arial", 11), text="", bg="#091e42", fg="White")
            kkk.place(x=100, y=180, width=300)

            bbb = Label(f57,font=("Arial", 11), text="", bg="#091e42", fg="White")
            bbb.place(x=100, y=200, width=300)

            ooo = Label(f57,font=("Arial", 11), text="", bg="#091e42", fg="White")
            ooo.place(x=100, y=220, width=300)

def updatedata2():
    db = sqlite3.connect('vivek.db')
    cr = db.cursor()
    cr.execute("update aa set UNAME='"+d1.get()+"',UPHY='"+d2.get()+"',UNC='"+d3.get()+"',UMATHS='"+d4.get()+"'")
    db.commit()
    db.close()
    showthedata(f55)
    messagebox.showinfo('Title', 'Data Update')














def deletedata(n):
    f8=Frame(bg="#091e42")
    n.add(f8,text="Delete")
    eew = Label(f8, text="Enter Roll No", font=("Arial", 11), bg="#091e42", fg="White")
    eew.place(x=100, y=100)
    qqa = Entry(f8, font=("Arial", 11), textvariable=e1)
    qqa.place(x=200, y=100, width=130)

    b98 = Button(f8,font=("Arial", 11), text="Delete",command=deletedata1)
    b98.place(x=360, y=100, width=80)
def deletedata1():
    db = sqlite3.connect('vivek.db')
    cr = db.cursor()
    cr.execute("delete from aa where URNO='"+e1.get()+"'")
    db.commit()
    db.close()
    showthedata(f55)
    messagebox.showinfo('Title', 'Data Deleted')
    e1.set("")










def logoutdata(n) :
    f9=Frame(bg="#091e42")
    n.add(f9,text="Logout")


def home():
    f1 = Frame(bg="#091e42")
    f1.place(x=0, y=0, width=600, height=400)
    c2 = Button(f1, text="LOGIN", command=login)
    c2.place(x=220, y=100, width=80, height=40)
    b2 = Button(f1, text="REGISTER", command=register)
    b2.place(x=310, y=100, width=80, height=40)


home()
root.mainloop()
