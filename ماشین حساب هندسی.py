import tkinter as TK

#روت
root = TK.Tk()

#تایتل
root.title("ماشین حساب هندسی")
#سایز برنامه
root.geometry("1600x900")
#بک
back1 = TK.PhotoImage(file="بورد7.png")
back2 = TK.Label(root, image=back1)
back2.pack()
back2.place(x=0, y=0, relwidth=1, relheight=1)

#مساحت بک

def open_new_window():
    if "condtion":
        new1 = TK.Toplevel(root)
        
        new1.title("مساحت")
        new1.geometry("1600x900")
        back1 = TK.PhotoImage(file="بورد7.png")
        back2 = TK.Label(new1, image=back1)
        back2.pack()       
        back2.place(x=0, y=0, relwidth=1, relheight=1)

        #مربع
        def open():
            if "condtion":
                morba1 =TK.Toplevel(new1)
                morba1.title("مربع")
                morba1.geometry("1600x900")
                back11 = TK.PhotoImage(file="بورد7.png")
                back22 = TK.Label(morba1, image=back11)
                back22.pack()       
                back2.place(x=0, y=0, relwidth=1, relheight=1)
                text_box = TK.Text(morba1, width= 5 , height=9)
                text_box.pack()
                morba1.mainloop()

        morba = TK.Button(new1, text="مربع", command=open)
        morba.pack()
        morba.config(width=25,height=9)
        morba.place(x=100,y=100)


       #مستطیل

        def open():
            if "condtion":
                mostatil1 =TK.Toplevel(new1)
                mostatil1.title("مستطیل")
                mostatil1.geometry("1600x900")
                back111 = TK.PhotoImage(file="بورد7.png")
                back222 = TK.Label(mostatil1, image=back111)
                back222.pack()       
                back222.place(x=0, y=0, relwidth=1, relheight=1)
                mostatil1.mainloop()
        mostatil = TK.Button(new1, text="مستطیل", command=open)
        mostatil.pack()
        mostatil.config(width=25,height=9)
        mostatil.place(x=433,y=100)
        mostatil.config(width=25,height=9)

        #مثلث 
        def open():
            if "condtion":
                mosalas1 =TK.Toplevel(new1)
                mosalas1.title("مثلث")
                mosalas1.geometry("1600x900")
                back1111 = TK.PhotoImage(file="بورد7.png")
                back2222 = TK.Label(mosalas1, image=back1111)
                back2222.pack()       
                back2222.place(x=0, y=0, relwidth=1, relheight=1)
                mosalas1.mainloop()
      
        mosalas = TK.Button(new1, text="مثلث", command=open)
        mosalas.pack()
        mosalas.config(width=25,height=9)
        mosalas.place(x=733,y=100)

        #دایره

        def open():
            if "condtion":
                daire1 =TK.Toplevel(new1)
                daire1.title("مربع")
                daire1.geometry("1600x900")
                back10 = TK.PhotoImage(file="بورد7.png")
                back20 = TK.Label(daire1, image=back10)
                back20.pack()       
                back2.place(x=0, y=0, relwidth=1, relheight=1)
                daire1.mainloop()
       
        daire = TK.Button(new1, text="دایره", command=open)
        daire.pack()
        daire.config(width=25,height=9)
        daire.place(x=1100,y=100)

        #ذوزنقه
        def open():
            if "condtion":
                zozange1 =TK.Toplevel(new1)
                zozange1.title("ذوزنقه")
                zozange1.geometry("1600x900")
                back100 = TK.PhotoImage(file="بورد7.png")
                back200 = TK.Label(zozange1, image=back100)
                back200.pack()       
                back200.place(x=0, y=0, relwidth=1, relheight=1)
                zozange1.mainloop()

        zozange =TK. Button(new1, text="ذوزنقه", command=open)
        zozange.pack()
        zozange.config(width=25,height=9)
        zozange.place(x=100,y=300)

        #متوازی الاضلاع

        def open():
            if "condtion":
                motavazi1 =TK.Toplevel(new1)
                motavazi1.title("متوازی الاضلاع")
                motavazi1.geometry("1600x900")
                back1000 = TK.PhotoImage(file="بورد7.png")
                back2000 = TK.Label(motavazi1, image=back1000)
                back2000.pack()       
                back2000.place(x=0, y=0, relwidth=1, relheight=1)
                motavazi1.mainloop()

        motavazi = TK.Button(new1, text="متوازی الاضلاع", command=open)
        motavazi.pack()
        motavazi.config(width=25,height=9)
        motavazi.place(x=1100,y=300)

        #منشور

        def open():
            if "condtion":
                sjan_3pahlo1 =TK.Toplevel(new1)
                sjan_3pahlo1.title("مساحت جانبی منشور")
                sjan_3pahlo1.geometry("1600x900")
                back13 = TK.PhotoImage(file="بورد7.png")
                back23= TK.Label(sjan_3pahlo1, image=back13)
                back23.pack()       
                back23.place(x=0, y=0, relwidth=1, relheight=1)
                sjan_3pahlo1.mainloop()

        sjan_3pahlo = TK.Button(new1, text="مساحت جانبی منشور سه پهلو", command=open)
        sjan_3pahlo.pack()
        sjan_3pahlo.config(width=26,height=4)
        sjan_3pahlo.place(y=300,x=733)

        #منشور کل
        def open():
            if "condtion":
                skol_3pahlo1 =TK.Toplevel(new1)
                skol_3pahlo1.title("مساحت کل منشور")
                skol_3pahlo1.geometry("1600x900")
                back133 = TK.PhotoImage(file="بورد7.png")
                back233= TK.Label(skol_3pahlo1, image=back133)
                back233.pack()       
                back233.place(x=0, y=0, relwidth=1, relheight=1)
                skol_3pahlo1.mainloop()
                
        skol_3pahlo = TK.Button(new1, text="مساحت کل منشور سه پهلو", command=open)
        skol_3pahlo.pack()
        skol_3pahlo.config(width=26,height=4)
        skol_3pahlo.place(y=375,x=733)

    #جانبی استوانه

        def open():
            if "condtion":
                sjan_ostovane1 =TK.Toplevel(new1)
                sjan_ostovane1.title("مساحت جانبی استوانه")
                sjan_ostovane1.geometry("1600x900")
                back1333 = TK.PhotoImage(file="بورد7.png")
                back2333= TK.Label(sjan_ostovane1, image=back1333)
                back2333.pack()       
                back2333.place(x=0, y=0, relwidth=1, relheight=1)
                sjan_ostovane1.mainloop()

        sjan_ostovane = TK.Button(new1, text="مساحت جانبی استوانه", command=open)
        sjan_ostovane.pack()
        sjan_ostovane.config(width=26,height=4)
        sjan_ostovane.place(y=300,x=433)

        #کل استوانه

        def open():
            if "condtion":
                skol_ostovane1 =TK.Toplevel(new1)
                skol_ostovane1.title("مساحت کل استوانه")
                skol_ostovane1.geometry("1600x900")
                back14 = TK.PhotoImage(file="بورد7.png")
                back24 = TK.Label(skol_ostovane1, image=back14)
                back24.pack()       
                back24.place(x=0, y=0, relwidth=1, relheight=1)
                skol_ostovane1.mainloop()

        skol_ostovane =TK.Button(new1, text="مساحت  کل استوانه", command=open)
        skol_ostovane.pack()
        skol_ostovane.config(width=26,height=4)
        skol_ostovane.place(y=375, x=433)


        
        new1.mainloop()      
#مساحت
button1 = TK.Button(root, text="مساحت", command=open_new_window)
button1.pack()
button1.place(x=600, y=100)

button1.config(width="20", height="8")


#محیط بک
def open_new_window():
    if "condtion":
        new2 = TK.Toplevel(root)
        new2.title("محیط")
        new2.geometry("1600x900")
        back1 = TK.PhotoImage(file="بورد7.png")
        back2 = TK.Label(new2, image=back1)
        back2.pack()
        back2.place(x=0, y=0, relwidth=1, relheight=1)

        #مربع
        def open():
            if "condtion":
                morba2 =TK.Toplevel(new2)
                morba2.title("مربع")
                morba2.geometry("1600x900")
                back3 = TK.PhotoImage(file="بورد7.png")
                back4= TK.Label(morba2, image=back3)
                back4.pack()       
                back4.place(x=0, y=0, relwidth=1, relheight=1)
                morba2.mainloop()

        morba = TK.Button(new2, text="مربع", command=open)
        morba.pack() 
        morba.config(width=25,height=9)
        morba.place(x=100,y=100)

        #مستطیل

        def open():
            if "condtion":
                mostatil2 =TK.Toplevel(new2)
                mostatil2.title("مستطیل")
                mostatil2.geometry("1600x900")
                back31 = TK.PhotoImage(file="بورد7.png")
                back41= TK.Label(mostatil2, image=back31)
                back41.pack()       
                back41.place(x=0, y=0, relwidth=1, relheight=1)
                mostatil2.mainloop()

        mostatil = TK.Button(new2, text="مستطیل", command=open)
        mostatil.pack()
        mostatil.config(width=25,height=9)
        mostatil.place(x=433,y=100)

        #مثلث
        def open():
            if "condtion":
                mosalas2 =TK.Toplevel(new2)
                mosalas2.title("مثلث")
                mosalas2.geometry("1600x900")
                back311 = TK.PhotoImage(file="بورد7.png")
                back411= TK.Label(mosalas2, image=back311)
                back411.pack()       
                back411.place(x=0, y=0, relwidth=1, relheight=1)
                mosalas2.mainloop()

        mosalas = TK.Button(new2, text="مثلث", command=open)
        mosalas.pack()
        mosalas.config(width=25,height=9)
        mosalas.place(x=733,y=100)

        #دایره 
        def open():
            if "condtion":
                daire2 =TK.Toplevel(new2)
                daire2.title("دایره")
                daire2.geometry("1600x900")
                back3111 = TK.PhotoImage(file="بورد7.png")
                back4111 = TK.Label(daire2, image=back3111)
                back4111.pack()       
                back4111.place(x=0, y=0, relwidth=1, relheight=1)
                daire2.mainloop()

        daire = TK.Button(new2, text="دایره", command=open)
        daire.pack()
        daire.config(width=25,height=9)
        daire.place(x=1100,y=100)

        #ذوذنقه
        def open():
            if "condtion":
                zozange2 =TK.Toplevel(new2)
                zozange2.title("ذوزنقه")
                zozange2.geometry("1600x900")
                back5 = TK.PhotoImage(file="بورد7.png")
                back6= TK.Label(zozange2, image=back5)
                back6.pack()       
                back6.place(x=0, y=0, relwidth=1, relheight=1)
                zozange2.mainloop()

        zozange =TK. Button(new2, text="ذوزنقه", command=open)
        zozange.pack()
        zozange.config(width=25,height=9)
        zozange.place(x=100,y=300)
        #متوازی الاضلاع
        def open():
            if "condtion":
                motavazi2 =TK.Toplevel(new2)
                motavazi2.title("متوازی الاضلاع")
                motavazi2.geometry("1600x900")
                back51 = TK.PhotoImage(file="بورد7.png")
                back61= TK.Label(motavazi2, image=back51)
                back61.pack()       
                back61.place(x=0, y=0, relwidth=1, relheight=1)
                motavazi2.mainloop()

        motavazi = TK.Button(new2, text="متوازی الاضلاع", command=open)
        motavazi.pack()
        motavazi.config(width=25,height=9)
        motavazi.place(x=1100,y=300)


        new2.mainloop()
#محیط        
button11 = TK.Button(root, text="محیط", command=open_new_window)
button11.pack(side="left")
button11.config(width="20", height="8")
button11.place(x=900, y=100)
#حجم بک 
def open_new_window():
    if "condtion":
        new3 = TK.Toplevel(root)
        new3.title("حجم")
        new3.geometry("1600x900")
        back1 = TK.PhotoImage(file="بورد7.png")
        back2 = TK.Label(new3, image=back1)
        back2.pack()
        back2.place(x=0, y=0, relwidth=1, relheight=1)

        #استوانه
        def open():
            if "condtion":
                ostovane2 =TK.Toplevel(new3)
                ostovane2.title("استوانه")
                ostovane2.geometry("1600x900")
                back62 = TK.PhotoImage(file="بورد7.png")
                back63= TK.Label(ostovane2, image=back62)
                back63.pack()       
                back63.place(x=0, y=0, relwidth=1, relheight=1)
                ostovane2.mainloop()


        ostovane = TK.Button(new3, text="استوانه" , command=open)
        ostovane.pack()
        ostovane.config(width=25,height=9)
        ostovane.place(y=250,x=275)

        #منشور

        def open():
            if "condtion":
                manshor2 =TK.Toplevel(new3)
                manshor2.title("منشور")
                manshor2.geometry("1600x900")
                back64 = TK.PhotoImage(file="بورد7.png")
                back65= TK.Label(manshor2, image=back64)
                back65.pack()       
                back65.place(x=0, y=0, relwidth=1, relheight=1)
                manshor2.mainloop()

        manshor = TK.Button(new3, text="منشور سه پهلو" , command=open)
        manshor.pack()
        manshor.config(width=25,height=9)
        manshor.place(y=250,x=850)

        new3.mainloop()
#حجم
button111 = TK.Button(root, text="حجم", command=open_new_window)
button111.pack()
button111.config(width="20", height="8")
button111.place(x=300 , y=100)

root.mainloop()




































































































































































































































