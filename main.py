from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import datetime
def GUIadd():
    def adding():
        x = e1.get()
        y = e2.get()
        with open("superdata.txt", "r") as read:
            superdata = read.read()
            Search_for_widget = superdata.find(x)
            q = len(x)
            pice = superdata[Search_for_widget:Search_for_widget + q]
            if pice == x:
                messagebox.showerror("تنبيه","الطعة موجودة بالفعل")
            else:
                with open("superdata.txt", "a") as superdata:
                    superdata.write(x + "\t")
                    superdata.write(y + "\t\t\n")
                    messagebox.showinfo("info","تمت اضافة القطعة")
    rootadd = Tk()
    rootadd.geometry("854x480+330+170")
    rootadd.resizable(False, False)
    f = Frame(rootadd, width=854, height=480, bg="#0B2F3A")
    f.pack()
    title = Label(f, text=": ادخل اسم السلعة", bg="#0B2F3A", fg="white", font=("tajwal", 17))
    title.place(x=600, y=120)
    e1 = Entry(f, font=("tajwal", 17), width=30, justify="center")
    e1.place(x=140, y=120)
    title2 = Label(f, text=": ادخل سعر السعة", bg="#0B2F3A", fg="white", font=("tajwal", 17))
    title2.place(x=600, y=200)
    e2 = Entry(f, font=("tajwal", 17), width=30, justify="center")
    e2.place(x=140, y=200)
    b1 = Button(f, text="اضافة",command=adding)
    b1.place(x=140, y=250)
    rootadd.mainloop()
def GUIfatora():
    def subtraction():
        window = tk.Tk()
        window.geometry("250x250+700+300")
    def fatora():
        pice = e1.get()
        the_number_of_pieces = int(e2.get())
        with open("superdata.txt", "r") as read:
            superdata = read.read()
            Search_for_widget = superdata.find(pice)
            q = len(pice)
            x = superdata[Search_for_widget:Search_for_widget + q]
            if x != pice:
                messagebox.showerror("تنبيه","القطعة غير موجودة")
            else:
                with open("superdata.txt","r") as read:
                    superdata = read.read()
                    q = len(pice)
                    Search_for_widget = superdata.find(pice)
                    Unit_price = int(superdata[Search_for_widget+q:q+Search_for_widget+9])
                    Price_of_total_pieces = int(Unit_price) * the_number_of_pieces
                    textaeria.insert(END,"\n"+str(pice)+"\t\t         "+str(Price_of_total_pieces)+"\t\t                    "+str(the_number_of_pieces)+"\t\t                    "+str(Unit_price))
    def finish():
        all_text = textaeria.get("1.0","end-1c")
        lines = all_text.split("\n")
        x = 0
        y=0
        for line in lines[1:]:
            lins = line.split()
            for i , lin in enumerate(lins):
                if i == 1:
                    x = int(lin) + y
                else:
                    continue     
            y = x
        print(x)
        window = tk.Toplevel()
        window.title("القائمة جاهزة للطباعة")
        window.geometry("750x750+400+100")
        window.configure(bg="white")
        window.resizable(False,False)
        Label_window = tk.Label(window,text="قائمة الفاتورة الاجمالية",font=("tajawal","15","bold"),bg="white",fg="black")
        Label_window.pack(pady=10)
        text_print = tk.Text(window,font=("courier","12"))
        text_print.pack(fill="both",expand=True)
        text_print.insert(END,"سعر القطعة الواحدة    عدد القطع     مجموع سعر القطع   اسم السلعة\n")
        li =  lines[1:]
        with open("datauser.txt","a",encoding="utf-8") as file:
            file.write("\nسعر القطعة الواحدة      عدد القطع       مجموع سعر القطع     اسم السلعة\n")
            for l in li:
                l = l.split()
                for b in l:
                    text_print.insert(END,"  "+b+"\t\t")
                    file.write(b+"\t\t\t\t")
                text_print.insert(END,"\n")
                file.write("\n")
            text_print.insert(END,"\n"+"__________________________________________________________________________"+"\n"+"total:"+"                            "+str(x)+"\n"+e3.get()+"\t"+str(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S:%p")))
            file.write("\n"+"total:"+str(x)+"\n"+e3.get()+"\t"+str(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S:%p"))+"\n"+"__________________________________________________________________________")        
    rootfatora = Tk()
    rootfatora.geometry("854x480+330+170")
    rootfatora.resizable(False, False)
    f = Frame(rootfatora, width=300, height=480, bg="#0B2F3A")
    f.place(x=554)
    title = Label(f, text=": ادخل اسم السلعة", bg="#0B2F3A", fg="white", font=("tajwal", 17))
    title.place(x=140, y=50)
    title2 = Label(f, text=": ادخل عدد القطع", bg="#0B2F3A", fg="white", font=("tajwal", 17))
    title2.place(x=140, y=100)
    title3 = Label(f, text=": ادخل اسم المشتري", bg="#0B2F3A", fg="white", font=("tajwal", 17))
    title3.place(x=140, y=150)
    title3 = Label(f, text="ابو محي الدين", bg="#0B2F3A", fg="yellow", font=("tajwal", 30, "bold"))
    title4 = Label(f, text="الشامي", bg="#0B2F3A", fg="yellow", font=("tajwal", 30, "bold"))
    title5 = Label(rootfatora, text="حساب الفواتير", bg="#0B2F3A", fg="white", font=("tajwal", 17))
    title3.place(x=50, y=180)
    title4.place(x=100, y=230)
    title5.pack(fill=X)
    e1 = Entry(f, font=("tajwal", 17), width=10, justify="center")
    e1.place(x=5, y=50)
    e2 = Entry(f, font=("tajwal", 17), width=10, justify="center")
    e2.place(x=5, y=100)
    e3 = Entry(f, font=("tajwal", 17), width=10, justify="center")
    e3.place(x=5, y=150)
    b1 = Button(f, bg="#0B2F3A", font=("tajawal", 15, "bold"), fg="white", text="اضافة الى الفاتورة",command=fatora)
    b1.place(x=75, y=280)
    b2 = Button(f, bg="#0B2F3A", font=("tajawal", 15, "bold"), fg="white", text="ازالة من الفاتورة",command=subtraction)
    b2.place(x=80, y=330)
    b3 = Button(f, bg="#0B2F3A", font=("tajawal", 15, "bold"), fg="white", text="انهاء الفاتورة",command=finish)
    b3.place(x=90, y=380)
    scrol = Scrollbar(rootfatora, orient=VERTICAL)
    textaeria = Text(rootfatora, width=67, bd=2, height=28, font=("tajawal", 11, "bold"), fg="white", bg="black",yscrollcommand=scrol.set)
    textaeria.place(x=14, y=30)
    scrol.pack(side=LEFT, fill=Y)
    scrol.config(command=textaeria.yview)
    textaeria.insert(END,"سعر القطعة الواحدة                   عدد القطع                      مجموع سعر القطع                    اسم السلعة")
    rootfatora.mainloop()
root = Tk()
root.geometry("480x240+500+300")
root.title("الشامي")
root.resizable(False,False)
title = Label(root,text="القائمة الرئيسية")
title.place(x=140,y=0)
f1 = Frame(root,width=120,height=240,bg="#0B2F3A")
f1.place(x=360,y=0)
title1 = Label(f1,text=":الخيارات",bg="#0B2F3A",fg="white",font=('tajawal',13,"bold"))
title1.place(x=37,y=10)
#the buttom
b1 = Button(f1,text="اضافة سلعة",width=15,bg="#0B2F3A",fg="white",command=GUIadd)
b2 = Button(f1,text="عرض قائمة السلع",width=15,bg="#0B2F3A",fg="white")
b3 = Button(f1,text="الفوترة",width=15,bg="#0B2F3A",fg="white",command=GUIfatora)
b4 = Button(f1,text="تعديل سعر قطعة",width=15,bg="#0B2F3A",fg="white")
b5 = Button(f1,text="عرض سعر قطعة",width=15,bg="#0B2F3A",fg="white")
b6 = Button(f1,text="خروج",width=15,bg="#0B2F3A",fg="white",command=quit)
#the view buttom
b1.place(x=3,y=40)
b2.place(x=3,y=70)
b3.place(x=3,y=100)
b4.place(x=3,y=130)
b5.place(x=3,y=160)
b6.place(x=3,y=190)
#photo
photo = PhotoImage(file="super1.png")
imo = Label(root,image=photo,width=360,height=300)
imo.place(x=-4,y=19)
root.mainloop()