
from tkinter import *
# from tkinter import ttk
from tkinter import messagebox
#Pale Goldenrod
pencere = Tk()
pencere.configure(background="Pale Goldenrod")
pencere.tk_setPalette("#d8bfd8") #hex-color kodunu bazı sitelerden elde edebilirsiniz.
pencere.geometry("800x800")



#etiket = Tk.Label(text='Merhaba Zalim Dünya')
#etiket.pack()
pencere.title("KARBON SALINIMI HESAPLAMA")
pencere.resizable(TRUE, TRUE)


def topla():
    s1 = float(ent1.get())
    s2 = float(ent2.get())
    s3 = float(ent3.get())
    s4 = float(ent4.get())
    lbl4["text"] = float(((s1 * 0.43 * (1.085)) / 1000)) + (s2 * 0.19 * ((0.35)) + (s3 * 0.000089) + (s4 * 0.6))
    # lbl4["text"]=float(s3*0.09)
    lbl7["text"] = "Ton"

    messagebox.showinfo("KARBON SALINIMINIZ", "AĞAÇLARIMIZ YOK OLUYOR!")


def Temizle():
    lbl4["text"] = ""
    lbl7["text"] = ""


lbl1 = Label(text="Elektrik Tüketiminiz(TL)", font="Times 12 bold")
lbl1.place(x=10, y=20)
# katsayı 0.43 alındı


lbl2 = Label(text="Doğalgaz Tüketiminiz(TL)", font="Times 12 bold")
lbl2.place(x=10, y=70)
# katsayı 0.19 alındı


lbl5 = Label(text="Otobüs kullanımı (KM)", font="Times 12 bold")
lbl5.place(x=10, y=120)
# 0.09 carbon salınımı yapar ortalama alındı.

lbl6 = Label(text="Kısa Mesafeli Uçuş Adet(Türkiye-Avrupa)", font="Times 12 bold ")
lbl6.place(x=10, y=160)
# adet olarak yazıldı 1 adet 0,6 Ton carbon salınımı yapmakta.


###KARBON PARAMETRELERİ.
lbl3 = Label(text="Karbon Salınımınız", font="Times 14 bold")
lbl3.place(x=10, y=600)

lbl4 = Label(font="Times 12 bold", bg="silver", width="25")
lbl4.place(x=200, y=600)

lbl7 = Label(font="Times 12 bold", bg="silver", width="8")
lbl7.place(x=431, y=600)

# 0.43 çarpanı
# lbl5 = Label(font ="Times 12 bold", bg="silver", width="4")
# lbl5.place(x=180, y=40)


# yakıt carpanı
# lbl6 = Label(font ="Times 12 bold", bg="silver", width="12")
# lbl6.place(x=180, y=90)

# ent1=Entry(font="Times 12 bold", fg="green", width="12")
# ent1.place(x=180, y=20)

# kullanıcının input yeri.
ent1 = Entry(font="Times 12 bold", fg="green", width="12")
ent1.place(x=310, y=20)

# kullanıcının input yeri
ent2 = Entry(font="Times 12 bold", fg="green", width="12")
ent2.place(x=310, y=70)

# kullanıcının input yeri
ent3 = Entry(font="Times 12 bold", fg="green", width="12")
ent3.place(x=310, y=120)

# kullanıcının input yeri
ent4 = Entry(font="Times 12 bold", fg="green", width="12")
ent4.place(x=310, y=160)

# buton tıklama
btn1 = Button(pencere, text="Hesapla", font="Times 12 bold", command=topla)
# btn1.grid(column=100,row=105)
btn1.place(x=700, y=700)

# buton tıklama
btn2 = Button(text="Temizle", font="Times 12 bold", command=Temizle)
btn2.place(x=700, y=600)

pencere.mainloop()
