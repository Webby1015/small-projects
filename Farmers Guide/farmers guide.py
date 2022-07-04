from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
m=Tk()
import mysql.connector
con = mysql.connector.connect(host="localhost",
                              user="root",
                              passwd="tiger",
                              database="system2")

def cs():
    c=Frame(m)
    c.configure(background="grey")
    c.place(x=250,y=170)
    z1=Label(c,text="VISIT: www.farmer.gov.in ",width=40,fg="purple",font=("ariel",14))
    b=Button(c,text="BACK",bg="lightgrey",borderwidth=10,width=25,command=c.destroy)
    z1.grid(row=0,column=0)
    b.grid(row=1,column=0)
    
def buy(x,y,z):
    credit(x,y,z)
def csh(x,y,z):
    c=e.get()
    c1=e3.get()
    cursor1=con.cursor()
    sql="insert into  farshop values('"+c+"','"+x+"','"+y+"','"+c1+"','"+z+"')"
    
    cursor1.execute(sql)
    con.commit()
    cursor1.close()
    bi=Tk()
    bi.geometry("500x500")
    l=Label(bi,text= "NAME    :  "+c+"",fg="purple",font=("ariel",14))
    l.place(x=10,y=50)
    l1=Label(bi,text="PRODUCT :  "+x+"",fg="purple",font=("ariel",14))
    l1.place(x=10,y=100)
    l2=Label(bi,text="PRICE   :  "+y+"",fg="purple",font=("ariel",14))
    l2.place(x=10,y=150)
    l3=Label(bi,text="Address :  "+c1+"",fg="purple",font=("ariel",14))
    l3.place(x=10,y=200)
    l4=Label(bi,text="order succesful ,Your order will be ariving within 3 days",fg="purple",font=("ariel",14))
    l4.place(x=10,y=250)
def credit(x,y,z):
    k=Tk()
    global e
    global e3
    k.geometry("500x500")
    l=Label(k,text="Enter your name",fg="purple",font=("ariel",14))
    l.place(x=10,y=50)
    l1=Label(k,text="Enter your card no.",fg="purple",font=("ariel",14))
    l1.place(x=10,y=100)
    l2=Label(k,text="Enter your card pin",fg="purple",font=("ariel",14))
    l2.place(x=10,y=150)
    l3=Label(k,text="Address",fg="purple",font=("ariel",14))
    l3.place(x=10,y=200)
    e=Entry(k,textvariable=st)
    e.place(x=250,y=50)
    e1=Entry( k,text=IntVar())
    e1.place(x=250,y=100)
    e2=Entry(k,text=IntVar())
    e2.place(x=250,y=150)
    e3=Entry(k)
    e3.place(x=250,y=200)
    b=Button(k,text="PROCEED TO PAY",bg="red",borderwidth=10,command=lambda:csh(x,y,z))
    b.place(x=180,y=350)
    



def trac(): 
        
    t=Frame(m)
    t.place(x=250,y=145)
    t.configure(background="grey",)
    p=PhotoImage(file="ab.PNG")
    image=Label(t,image=p)
    image.grid(row=0,column=2)
    p1=PhotoImage(file="download.PNG")
    image=Label(t,image=p1)
    image.grid(row=1,column=2)
    p2=PhotoImage(file="qwe.PNG")
    image=Label(t,image=p2)
    image.grid(row=2,column=2)
    p3=PhotoImage(file="abcd.PNG")
    image=Label(t,image=p3)
    image.grid(row=3,column=2)
    z1=Label(t,text="Mahindra yuvo 255DI,\n32 hp,Tractor,1500kg",width=30,fg="purple",font=("ariel",14))
    z2=Button(t,text="BUY\n(Rs. 5.6lakh)",bg="red",borderwidth=10,command=lambda:buy('Mahindra yuvo 255DI','560000','Tractor'))
    z3=Label(t,text="Mahindra yuvo 235DI,\n30 hp,Tractor,1200kg",width=30,fg="purple",font=("arabic",14))
    z4=Button(t,text="BUY\n(Rs. 5.1lakh)",bg="red",borderwidth=10,command=lambda:buy('Mahindra yuvo 235DI','510000','Tractor'))
    z5=Label(t,text="Mahindra mm 220DI,\n15 hp,Tractor,1600kg",width=30,fg="purple",font=("arabic",14))
    z6=Button(t,text="BUY\n(Rs. 5.3lakh)",bg="red",borderwidth=10,command=lambda:buy('Mahindra mm 220DI','530000','Tractor'))
    z7=Label(t,text="Mahindra rie 260DI,\n40 hp,Tractor,1800kg",width=30,fg="purple",font=("arabic",14))
    z8=Button(t,text="BUY\n(Rs. 7.3lakh)",bg="red",borderwidth=10,command=lambda:buy('Mahindra rie 260DI','730000','Tractor'))
    b=Button(t,text="BACK",bg="lightgrey",borderwidth=10,width=25,command=t.destroy)
    z7.grid(row=3,column=0)
    z8.grid(row=3,column=1)
    z6.grid(row=2,column=1)
    z5.grid(row=2,column=0)
    z3.grid(row=1,column=0)
    z4.grid(row=1,column=1)
    z2.grid(row=0,column=1)
    z1.grid(row=0,column=0)
    b.grid(row=4,column=0)
    t.mainloop()
def Fer():
    fe=Frame(m)
    fe.configure(background="grey")
    fe.place(x=250,y=170)
    z1=Label(fe,text="Akash Bio    \nStimulant   ,25kg",width=40,fg="purple",font=("ariel",14))
    z2=Button(fe,text="BUY\n(Rs. 650 )",bg="red",borderwidth=10,command=lambda:buy('Akash Bio Stimulant','650','Fertilizers'))
    z3=Label(fe,text="Super Potassium\nHumate,5kg",fg="purple",width=40,font=("arabic",14))
    z4=Button(fe,text="BUY\n(Rs.5000 )",bg="red",borderwidth=10,command=lambda:buy('Super Potassium Humate','5000','Fertilizers'))
    z5=Label(fe,text="  Loar organic    \nfertilizer     ",fg="purple",width=40,font=("arabic",14))
    z6=Button(fe,text="BUY\n(Rs.3700 )",bg="red",borderwidth=10,command=lambda:buy('Loar organic fertilizers','3700','Fertilizers'))
    z7=Label(fe,text="bio star organic\nfertilizer",fg="purple",width=40,font=("arabic",14))
    z8=Button(fe,text="BUY\n(Rs.4500 )",bg="red",borderwidth=10,command=lambda:buy('bio star organic fertilizers','4500','Fertilizers'))
    b=Button(fe,text="BACK",bg="lightgrey",borderwidth=10,width=35,command=fe.destroy)
    z7.grid(row=3,column=0)
    z8.grid(row=3,column=1)
    z6.grid(row=2,column=1)
    z5.grid(row=2,column=0)
    z3.grid(row=1,column=0)
    z4.grid(row=1,column=1)
    z2.grid(row=0,column=1)
    z1.grid(row=0,column=0)
    b.grid(row=4,column=0)
    fe.mainloop()

    
    
def SEE():
        se=Frame(m)
        se.configure(background="grey")
        se.place(x=200,y=145)
        z1=Label(se,text="BLUE BERRIES,1kg",width=20,height=5,fg="red",font=("ariel",10))
        z2=Button(se,text="BUY\n(Rs. 800 )",bg="red",borderwidth=10,width=18,command=lambda:buy('BLUE BERRIES','800','Seed'))
        z3=Label(se,text="IRISH POTATOES,1kg",width=20,height=5,fg="red",font=("arabic",10))
        z4=Button(se,text="BUY\n(Rs.1600)",bg="red",borderwidth=10,width=18,command=lambda:buy('Irish potatoes','1600','Seed'))
        z5=Label(se,text="SWEET POTATOES,1kg",width=20,height=5,fg="red",font=("arabic",10))
        z6=Button(se,text="BUY\n(Rs.1800)",bg="red",borderwidth=10,width=18,command=lambda:buy('Sweet potatoes','1800','Seed'))
        z7=Label(se,text="BARLEY,1kg",fg="red",width=20,height=5,font=("arabic",10))
        z8=Button(se,text="BUY\n(Rs. 900 )",bg="red",borderwidth=10,width=18,command=lambda:buy('Barley','900','Seed'))
        z9=Label(se,text="COTTON,1kg",fg="red",width=20,height=5,font=("arabic",10))
        z10=Button(se,text="BUY\n(Rs.1800)",bg="red",borderwidth=10,width=18,command=lambda:buy('Cotton','1800','Seed'))
        z11=Label(se,text="SUGAR BEETS,1kg",width=20,height=5,fg="red",font=("arabic",10))
        z12=Button(se,text="BUY\n(Rs.5930)",bg="red",borderwidth=10,width=18,command=lambda:buy('Sugar beets','5930','Seed'))
        b=Button(se,text="BACK",bg="lightgrey",borderwidth=10,width=35,command=se.destroy)
        z11.grid(row=2,column=2)
        z12.grid(row=3,column=2)
        z9.grid(row=2,column=1)
        z10.grid(row=3,column=1)
        z7.grid(row=2,column=0)
        z8.grid(row=3,column=0)
        z6.grid(row=1,column=2)
        z5.grid(row=0,column=2)
        z3.grid(row=0,column=1)
        z4.grid(row=1,column=1)
        z2.grid(row=1,column=0)
        z1.grid(row=0,column=0)
        b.grid(row=4,column=1)
        se.mainloop()
def equ():
        e=Frame()
        e.place(x=250,y=145)
        e.configure(background="grey")
        
        
        z1=Label(e,text="CULTIVATOR",fg="purple",width=40,height=2,font=("ariel",14))
        z2=Button(e,text="BUY\n(Rs.80000)",bg="red",borderwidth=10,command=lambda:buy('Cultivator','80000','Equipment'))
        z3=Label(e,text="PLOWS",fg="purple",width=40,height=2,font=("arabic",14))
        z4=Button(e,text="BUY\n(Rs.35000)",bg="red",borderwidth=10,command=lambda:buy('Plows','35000','Equipment'))
        z5=Label(e,text="HARROWS",fg="purple",width=40,height=2,font=("arabic",14))
        z6=Button(e,text="BUY\n(Rs.16000)",bg="red",borderwidth=10,command=lambda:buy('Harrows','16000','Equipment'))
        z7=Label(e,text="SPRAYERS",fg="purple",width=40,height=2,font=("arabic",14))
        z8=Button(e,text="BUY\n(Rs. 4500)",bg="red",borderwidth=10,command=lambda:buy('Sprayers','4500','Equipment'))
        b=Button(e,text="BACK",bg="lightgrey",borderwidth=10,width=35,command=e.destroy)
        z7.grid(row=3,column=0)
        z8.grid(row=3,column=1)
        z6.grid(row=2,column=1)
        z5.grid(row=2,column=0)
        z3.grid(row=1,column=0)
        z4.grid(row=1,column=1)
        z2.grid(row=0,column=1)
        z1.grid(row=0,column=0)
        b.grid(row=4,column=0)
        e.mainloop()
def store():
    s=Frame(m)
    s.configure(background="light gray")
    s.place(x=130,y=210)
    z=Label(s,text="STORE",width=13,height=2,fg="WHITE",bg="blue",font=("fixedsys",18))
    l1=Button(s,text=" TRACTORS   ",borderwidth=10,bg="powder blue",font=("fixedsys",18),command=trac)
    l1.grid(row=2,column=0)
    l2=Button(s,text=" FERTILIZERS",borderwidth=10,bg="powder blue",font=("fixedsys",18),command=Fer)
    l2.grid(row=2,column=2)
    l3=Button(s,text=" SEEDS      ",borderwidth=10,bg="powder blue",font=("fixedsys",18),command=SEE)
    l3.grid(row=3,column=0)
    l4=Button(s,text=" EQUIPMENT  ",borderwidth=10,bg="powder blue",font=("fixedsys",18),command=equ)
    l4.grid(row=3,column=1)
    b=Button(s,text=" BACK       ",borderwidth=10,bg="light grey",font=("fixedsys",18),command=s.destroy)
    b.grid(row=3,column=2)
    z.grid(row=2,column=1)
    
   
    
def al():
    a=Frame(m)
    a.configure(background="orange")
    a.place(x=150,y=200)
    Label(a,text=">They are mostly flat and regular soils and are best suited for agriculture.\n>They are best suited to irrigation and respond well to canal and well/tube-well\n irrigation.\n>They yield splendid crops of rice, wheat, sugarcane, tobacco, cotton, jute, maize, \noilseeds, vegetables and fruits.",font=("fixedsys",15),fg="white",bg="black").grid(row=0,column=0)
    b1=Button(a,text="STORE",command=store,font=("fixedsys",15),fg="black",borderwidth=5,bg="yellow",width=25).grid(row=2,column=0)
    b6=Button(a,text="BACK",font=("fixedsys",15),fg="black",borderwidth=10,command=a.destroy,bg="lightblue",width=25).grid(row=3,column=0)
    a.mainloop()
def bl():
    b=Frame(m)
    b.configure(background="orange")
    b.place(x=150,y=200)
    Label(b,text=">These soils are best suited for cotton crop. Hence these soils are called as\n regur and black cotton soils.\n>Other major crops grown on the black soils include wheat, jowar, linseed, virginia \ntobacco, castor, sunflower and millets. ",font=("fixedsys",15),fg="white",bg="black").grid(row=0,column=0)
    b1=Button(b,text="STORE",command=store,font=("fixedsys",15),fg="black",borderwidth=5,bg="yellow",width=25).grid(row=2,column=0)
    b6=Button(b,text="BACK",font=("fixedsys",15),fg="black",borderwidth=10,command=b.destroy,bg="lightblue",width=25).grid(row=3,column=0)
    b.mainloop()
def red():
    r=Frame(m)
    r.configure(background="orange")
    r.place(x=150,y=200)
    Label(r,text=">They are mostly flat and regular soils and are best suited for agriculture.\n>They are best suited to irrigation and respond well to canal and well/tube-well\n irrigation.\n>They yield splendid crops of rice, wheat, sugarcane, tobacco, cotton, jute, maize, \noilseeds, vegetables and fruits.",font=("fixedsys",15),fg="white",bg="black").grid(row=0,column=0)
    b1=Button(r,text="STORE",command=store,font=("fixedsys",15),fg="black",borderwidth=5,bg="yellow",width=25).grid(row=2,column=0)
    b6=Button(r,text="BACK",font=("fixedsys",15),fg="black",borderwidth=10,command=r.destroy,bg="lightblue",width=25).grid(row=3,column=0)
    r.mainloop()
def des():
    d=Frame(m)
    d.configure(background="orange")
    d.place(x=150,y=200)
    Label(d,text=">They are mostly flat and regular soils and are best suited for agriculture.\n>They are best suited to irrigation and respond well to canal and well/tube-well\n irrigation.\n>They yield splendid crops of rice, wheat, sugarcane, tobacco, cotton, jute, maize, \noilseeds, vegetables and fruits.",font=("fixedsys",15),fg="white",bg="black").grid(row=0,column=0)
    b1=Button(d,text="STORE",command=store,font=("fixedsys",15),fg="black",borderwidth=5,bg="yellow",width=25).grid(row=2,column=0)
    b6=Button(d,text="BACK",font=("fixedsys",15),fg="black",borderwidth=10,command=d.destroy,bg="lightblue",width=25).grid(row=3,column=0)
    d.mainloop()

def lat():
    l=Frame(m)
    l.configure(background="orange")
    l.place(x=150,y=200)
    Label(l,text=">They are mostly flat and regular soils and are best suited for agriculture.\n>They are best suited to irrigation and respond well to canal and well/tube-well\n irrigation.\n>They yield splendid crops of rice, wheat, sugarcane, tobacco, cotton, jute, maize, \noilseeds, vegetables and fruits.",font=("fixedsys",15),fg="white",bg="black").grid(row=0,column=0)
    b1=Button(l,text="STORE",command=store,font=("fixedsys",15),fg="black",borderwidth=5,bg="yellow",width=25).grid(row=2,column=0)
    b6=Button(l,text="BACK",font=("fixedsys",15),fg="black",borderwidth=10,command=l.destroy,bg="lightblue",width=25).grid(row=3,column=0)
    l.mainloop()
def moun():
    mo=Frame(m)
    mo.configure(background="orange")
    mo.place(x=150,y=200)
    Label(mo,text=">They are mostly flat and regular soils and are best suited for agriculture.\n>They are best suited to irrigation and respond well to canal and well/tube-well\n irrigation.\n>They yield splendid crops of rice, wheat, sugarcane, tobacco, cotton, jute, maize, \noilseeds, vegetables and fruits.",font=("fixedsys",15),fg="white",bg="black").grid(row=0,column=0)
    b1=Button(mo,text="STORE",command=store,font=("fixedsys",15),fg="black",borderwidth=5,bg="yellow",width=25).grid(row=2,column=0)
    b6=Button(mo,text="BACK",font=("fixedsys",15),fg="black",borderwidth=10,command=mo.destroy,bg="lightblue",width=25).grid(row=3,column=0)
    mo.mainloop()
def psoil():
        x=[22,29,28,2,6,1,2,7]
        y=["Alluvial ","Black ","red and yellow","laterite","arid","saline","peaty and organic","forest"]
        plt.pie(x,labels=y,shadow="true",autopct='%1.1f%%',explode=(0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05))
        plt.show()
def lm():
        cursor1=con.cursor()
        sql="select count(*),Type from farshop group by type;"
        cursor1.execute(sql)
        rec=cursor1.fetchall()
        l=[]
        l1=[]
        colours=["r","g","b","c"]
        for i in rec:
            l.append(i[0])
            l1.append(i[1])    
        plt.bar(l1,l,color=colours)
        plt.xlabel("Type")
        plt.ylabel("Sales")
        plt.show()
def grap():
    g=Frame(m)
    g.configure(background="green")
    g.place(x=250,y=220)
    b1=Button(g,text="RECENT SALES",font=("fixedsys",15),fg="black",borderwidth=20,command=lm,bg="lightgreen",width=25).grid(row=0,column=0)
    b2=Button(g,text="SOILS IN INDIA",font=("fixedsys",15),fg="black",borderwidth=20,command=psoil,bg="lightgreen",width=25).grid(row=0,column=1)
    b1=Button(g,text="BACK",font=("fixedsys",15),fg="black",borderwidth=20,command=g.destroy,bg="LIGHTGREY",width=25).grid(row=1,column=0)
    g.mainloop()
    
    
def hand():
    n=Frame(m)
    
   
    n.configure(background="orange")
    n.place(x=150,y=200)
    
    x=Label(n,text="TYPES OF SOILS",font=("fixedsys",20),fg="brown",bg="black").grid(row=0,column=1)
    b1=Button(n,text=" 1. Alluvial Soils ",font=("fixedsys",15),command=al,borderwidth=5,fg="black",bg="yellow",width=25).grid(row=1,column=0)
    b2=Button(n,text=" 2. Black Soils ",font=("fixedsys",15),command=bl,fg="black",borderwidth=5,bg="yellow",width=25).grid(row=2,column=0)
    b3=Button(n,text=" 3. Red Soils ",font=("fixedsys",15),command=red,fg="black",borderwidth=5,bg="yellow",width=25).grid(row=1,column=1)
    b4=Button(n,text=" 4. Desert Soils ",font=("fixedsys",15),command=des,fg="black",borderwidth=5,bg="yellow",width=25).grid(row=2,column=1)
    b5=Button(n,text=" 5. Laterite Soils ",font=("fixedsys",15),command=lat,fg="black",borderwidth=5,bg="yellow",width=25).grid(row=1,column=2)
    b6=Button(n,text=" 6. Mountain Soils ",font=("fixedsys",15),command=moun,fg="black",borderwidth=5,bg="yellow",width=25).grid(row=2,column=2)
    b7=Button(n,text="BACK",font=("fixedsys",15),fg="black",borderwidth=10,command=n.destroy,width=25).grid(row=3,column=1)
    n.mainloop()
def ph(a):
    fe.destroy()
    ph=Frame(m)
    ph.configure(background="orange")
    ph.place(x=220,y=200)
    cursor1=con.cursor()
    if a==1:
        sql="select one from ph"
        cursor1.execute(sql)
        rec=cursor1.fetchall()
        c=0
        for i in rec:
            c=c+1
            for j in i:
                x=Label(ph,text=str(j)+"\n",font=("Ariel",20),fg="Blue",bg="orange").grid(row=c,column=1)
    elif a==2:
        sql="select two from ph"
        cursor1.execute(sql)
        rec=cursor1.fetchall()
        c=0
        for i in rec:
            c=c+1
            for j in i:
                x=Label(ph,text=str(j)+"\n",font=("Ariel",20),fg="Blue",bg="orange").grid(row=c,column=1)
    elif a==3:
        sql="select three from ph"
        cursor1.execute(sql)
        rec=cursor1.fetchall()
        c=0
        for i in rec:
            c=c+1
            for j in i:
                x=Label(ph,text=str(j)+"\n",font=("Ariel",20),fg="Blue",bg="orange").grid(row=c,column=1)
    b7=Button(ph,text="BACK",font=("fixedsys",13),fg="black",borderwidth=10,command=ph.destroy,width=60).grid(row=15,column=1)

    ph.mainloop()
def ferana():
    global fe
    fe=Frame(m)
    fe.configure(background="orange")
    fe.place(x=220,y=135)
    s0=Label(fe,text=" ",bg="orange",font=("ariel",14)).grid(row=0,column=1)
    l=Label(fe,text="STEP 1: Buy a pH paper from your nearest chemist.                       ",fg="blue",font=("ariel",12)).grid(row=1,column=1)
    s=Label(fe,text=" ",bg="orange",font=("ariel",14)).grid(row=2,column=1)
    l1=Label(fe,text="STEP 2: Collect some of your soil in a bowl and add water.            ",fg="blue",font=("ariel",12)).grid(row=3,column=1)
    s1=Label(fe,text=" ",bg="orange",font=("ariel",14)).grid(row=4,column=1)
    l2=Label(fe,text="STEP 3: Put one end of the pH paper to the solution.                      ",fg="blue",font=("ariel",12)).grid(row=5,column=1)
    s2=Label(fe,text=" ",bg="orange",font=("ariel",14)).grid(row=6,column=1)
    l3=Label(fe,text="STEP 4: Check the ph from a ph scale and Enter the value below. ",fg="blue",font=("ariel",12)).grid(row=7,column=1)
    s3=Label(fe,text=" ",bg="orange",font=("ariel",14)).grid(row=8,column=1)
    b=Button(fe,text="5.0 - 5.5",font=("fixedsys",13),fg="black",command=lambda:ph(1),borderwidth=3,width=60).grid(row=9,column=1)
    b1=Button(fe,text="5.5 - 6.5",font=("fixedsys",13),fg="black",command=lambda:ph(2),borderwidth=3,width=60).grid(row=11,column=1)
    b=Button(fe,text="6.5 - 7.0",font=("fixedsys",13),fg="black",command=lambda:ph(3),borderwidth=3,width=60).grid(row=13,column=1)
    b7=Button(fe,text="BACK",font=("fixedsys",13),fg="black",borderwidth=10,command=fe.destroy,width=60).grid(row=15,column=1)
    fe.mainloop()
    
    

far=PhotoImage(file="1000x.PNG")
image=Label(m,image=far)
image.grid(row=0,column=0)
    
m.configure(background="orange")
m.geometry("950x500")
    
m.title("\t\t\t  FARMERS GUIDE\t\t")
    
Label(m,text="     FARMERS GUIDE     ",font=("fixedsys",30),fg="white",bg="black").place(x=230,y=0)
cat=Frame(m)
cat.place(x=120,y=100)
b1=Button(cat,text="CROP HANDBOOK ",font=("fixedsys",15),fg="black",bg="yellow",command=hand,borderwidth=5,width=20).grid(row=1,column=0)
b2=Button(cat,text="NEWSFEED",font=("fixedsys",15),fg="black",bg="yellow",command=grap,borderwidth=5,width=15,).grid(row=1,column=1)
b3=Button(cat,text="FERTILITY ANALYSER",font=("fixedsys",15),command=ferana,fg="black",bg="yellow",borderwidth=5,width=20).grid(row=1,column=2)
b4=Button(cat,text="FARMER'S SHOP",font=("fixedsys",15),fg="black",command=store,bg="yellow",borderwidth=5,width=18).grid(row=1,column=3)
b6=Button(cat,text="CONTACT US",font=("fixedsys",15),fg="black",bg="yellow",command=cs,borderwidth=5,width=12).grid(row=1,column=4)
st=StringVar()
m.mainloop()




