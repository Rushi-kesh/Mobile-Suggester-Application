import matplotlib.pyplot as plt
import numpy as np
import Tkinter
from Tkinter import*
import pandas as pd
data=pd.read_csv("data.csv")
top = Tkinter.Tk()

w=Canvas(top, width=500, height=100,bg="yellow")

def welcome():
   
   top.destroy()
   global top1
   top1 = Tkinter.Tk()
   w1=Canvas(top1, width=500, height=500,bg="yellow")

   v= StringVar()
   l1= Label( w1, textvariable=v,relief=RAISED,fg = "black",bg = "blue", font = "Verdana 10 bold",justify=CENTER).grid(row=0,pady=4)
   v.set("Mobile sholud have better?")
   
   
   
   global var1
   var1 = IntVar()


   c1=Tkinter.Checkbutton(w1, text="Camera(in pixel)", variable=var1, onvalue=1, offvalue=0,activebackground="red",bg="yellow")
   
   c1.grid(row=1, sticky=W, pady=4)
   global var2
   var2 = IntVar()


   c2=Tkinter.Checkbutton(w1, text="Screen size(in inches)", variable=var2, onvalue=1, offvalue=0,activebackground="red",bg="yellow")
   c2.grid(row=2, sticky=W, pady=4)
   global var3
   var3 = IntVar()


   c3=Tkinter.Checkbutton(w1, text="Battery(in mAH)", variable=var3, onvalue=1, offvalue=0,activebackground="red",bg="yellow")
   c3.grid(row=3, sticky=W, pady=4)
   global var4
   var4 = IntVar()

   c4=Tkinter.Checkbutton(w1, text="Price", variable=var4, onvalue=1, offvalue=0,activebackground="red",bg="yellow")
   c4.grid(row=4, sticky=W, pady=4)

   j = Tkinter.Button(w1, text ="submit ", command = main_code,fg="white",bg ="black",bd=3,width = 10, activebackground = "#33B5E5").grid(row=6, sticky=W)   
   
   w1.pack(fill=BOTH,expand=1)
   top1.mainloop()


def main_code():
   global cflag
   cflag=0
   global sflag
   sflag=0
   global bflag
   bflag=0
   global chflag
   chflag=0
   top1.destroy()
   global top2
   top2 = Tkinter.Tk()
   w2=Canvas(top2, width=500, height=600,bg="yellow")
   l= Label( w2, text="ENTER RANGES OF SPECS",relief=FLAT,fg = "black",bg = "red", font = "Verdana 10 bold").grid(row=0)
   lb1= Label( w2, text="MIN",relief=FLAT,bg = "white",fg = "blue", font = "Verdana 10 bold").grid(row=0,column=1)
   lb2= Label( w2, text="MAX",relief=FLAT,bg = "white",fg = "red", font = "Verdana 10 bold").grid(row=0,column=2)
   l1=""
   cam1=StringVar()
   batt1=StringVar()
   scr1=StringVar()
   price1=StringVar()
   cam2=StringVar()
   batt2=StringVar()
   scr2=StringVar()
   price2=StringVar()
   l2=""
   l3=""
   l4=""
   global lcamera
   global lscreen
   global lbattery
   global lcheap
   global hcamera
   global hscreen
   global hbattery
   global hcheap


   if(var1.get()==1):
      cflag=1
      l1=Label(w2, text="Camera(In PIXELS)",fg="white",bg ="black")
      l1.grid(row=1, sticky=W)
      lcamera=Entry(w2,textvariable=cam1,width=20,bd=3)
      lcamera.grid(row=1,column=1)
      hcamera=Entry(w2,textvariable=cam2,width=20,bd=3)
      hcamera.grid(row=1,column=2)
   if(var2.get()==1):
      sflag=1
      l2=Label(w2, text="Screen size(In INCHES)",fg="white",bg ="black")
      l2.grid(row=2, sticky=W)
      lscreen=Entry(w2,textvariable=scr1,width=20,bd=3)
      lscreen.grid(row=2,column=1)
      hscreen=Entry(w2,textvariable=scr2,width=20,bd=3)
      hscreen.grid(row=2,column=2)

   if(var3.get()==1):
      bflag=1
      l3=Label(w2, text="Battery(In mAh)",fg="white",bg ="black")
      l3.grid(row=3, sticky=W)
      lbattery=Entry(w2,textvariable=batt1,width=20,bd=3)
      lbattery.grid(row=3,column=1)
      hbattery=Entry(w2,textvariable=batt2,width=20,bd=3)
      hbattery.grid(row=3,column=2)

   if(var4.get()==1):
      chflag=1
      l4=Label(w2, text="Price(In RUPEE)",fg="white",bg ="black")
      l4.grid(row=4, sticky=W)
      lcheap=Entry(w2,textvariable=price1,width=20,bd=3)
      lcheap.grid(row=4,column=1)
      hcheap=Entry(w2,textvariable=price2,width=20,bd=3)
      hcheap.grid(row=4,column=2)

   j = Tkinter.Button(w2, text ="Submit ",command=det,fg="white",bg ="black",bd=3,width = 10, activebackground = "#33B5E5").grid(row=6, sticky=W)
   
   w2.pack(fill=BOTH,expand=1)
   
   
   
   top2.mainloop()


def det():
   global company
   company=[]
   global model
   model=[]
   global screen
   screen=[]
   global camera
   camera=[]
   global battery
   battery=[]
   global price
   price=[]
   for i in range(0,27):
      cp=data.iloc[i][0]
      company.append(cp)
      md=data.iloc[i][1]
      model.append(md)
      cm=data.iloc[i][2]
      camera.append(cm)
      sc=data.iloc[i][3]
      screen.append(sc)
      batt=data.iloc[i][4]
      battery.append(batt)
      pc=data.iloc[i][5]
      price.append(pc)
   global nGlobe
   nGlobe = []
   lcam = 8
   hcam = 24
   lscr = 4.7
   hscr = 6.44
   lbatt = 1810
   hbatt = 5300
   lprice = 6000
   hprice = 64000

   if (cflag==1):
      
      lcam=lcamera.get()
      hcam=hcamera.get()
      

   if (sflag==1):
      
      lscr=lscreen.get()
      hscr=hscreen.get()
      
      
   if (bflag==1):
      
      lbatt=lbattery.get()
      hbatt=hbattery.get()
      
      

   if (chflag==1):
      
      lprice=lcheap.get()
      hprice=hcheap.get()
      
   for i in range(0,27):
          if (int(lprice)<=int(price[i])<=int(hprice) and int(lbatt)<=int(battery[i])<=int(hbatt) and int(lscr)<=int(screen[i])<=int(hscr) and int(lcam)<=int(camera[i])<=int(hcam)):
	     nGlobe.append(i)
   
   if (True):
      Tx = []
      Ty = []
      global top3
      top2.destroy()
      top3=Tkinter.Tk()
      
      text2 = Text(top3, height=50, width=150)
      scroll = Scrollbar(top3, command=text2.yview)
      text2.configure(yscrollcommand=scroll.set)
      text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
      text2.tag_configure('big', font=('Verdana', 20, 'bold'))
      text2.tag_configure('color', foreground='grey',font=('Tempus Sans ITC', 12, 'bold'))
      text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
      text2.insert(END,'\nMobiles Acording to your requirements are\n', 'big')
      text2.pack(side=LEFT)
      scroll.pack(side=RIGHT, fill=Y)
      
      j=1
      for i in nGlobe:
      	   
           text2.insert(END,j, 'color')
           text2.insert(END,'  company=', 'color')
           text2.insert(END,company[i], 'color')
           text2.insert(END,'\t\t model=', 'color')
           text2.insert(END,model[i], 'color')
           text2.insert(END,'\t\t camera=', 'color')
           text2.insert(END,camera[i], 'color')
           text2.insert(END,'\t\t screen size=', 'color')
           text2.insert(END,screen[i], 'color')
           text2.insert(END,'\t\t battery=', 'color')
           text2.insert(END,battery[i], 'color')
           text2.insert(END,'\t\t price=', 'color')
           text2.insert(END,price[i], 'color')
           text2.insert(END,'\t', 'color')
           text2.insert(END,'\n\n', 'color')
           j=j+1
	   Tx.append([2,7,12,17])
	   Ty.append([(float(camera[i])/24)*100,(float(screen[i])/6.44)*100,(float(battery[i])/5300)*100,(float(price[i])/35000)*100])
	   
     
      L = []
      L2 = []
      for i in range(len(Tx)):
	L.append(Tx[i])
	L.append(Ty[i])
	L2.append(model[nGlobe[i]])
      Lins = plt.plot(*L)
      plt.legend(Lins,L2)	
      plt.xticks([2,7,12,17],['Camera','Screen','Battery','Price'])
      plt.yticks(np.arange(0,100,10),np.arange(0,100,10))
      plt.grid(True)
      plt.ylabel('Quality')
      plt.show()
      
      


var = StringVar()
label = Label( w, textvariable=var, relief=FLAT ,fg="red",bg="black", font = "Verdana 10 bold")
var.set("Welcome if you are interested in buying new phone then please\n")
B = Tkinter.Button(w, text ="Click here", command = welcome,bg="black",fg="white",bd =4)
B.configure(width = 10, activebackground = "#33B5E5",relief = RAISED)


label.pack(fill=X)
B.pack()
w.pack(fill=BOTH,expand=1)
top.mainloop()
