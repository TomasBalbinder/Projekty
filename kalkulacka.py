from tkinter import *


gui = Tk()
gui.title("Jednoducha kalkulacka")

kolonka = Entry(gui, width=35, borderwidth=2)
kolonka.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

def tlacitko_pridat(cislo):
    ted = kolonka.get()
    kolonka.delete(0, END)
    kolonka.insert(0, str(ted) + str(cislo))

def tlacitko_vymazat():
    kolonka.delete(0, END)

def tlacitko_plus():
    prvni_cislo = kolonka.get()
    global prvni_c
    prvni_c = int(prvni_cislo)
    kolonka.delete(0, END)

def tlacitko_rovnase():
    druhe_cislo = kolonka.get()
    kolonka.delete(0, END)
    kolonka.insert(0, prvni_c + int(druhe_cislo))

    




tlacitko_1 = Button(gui, text="1",padx=40, pady=20, command=lambda: tlacitko_pridat(1))
tlacitko_2 = Button(gui, text="2",padx=40, pady=20, command=lambda: tlacitko_pridat(2))
tlacitko_3 = Button(gui, text="3",padx=40, pady=20, command=lambda: tlacitko_pridat(3))
tlacitko_4 = Button(gui, text="4",padx=40, pady=20, command=lambda: tlacitko_pridat(4))
tlacitko_5 = Button(gui, text="5",padx=40, pady=20, command=lambda: tlacitko_pridat(5))
tlacitko_6 = Button(gui, text="6",padx=40, pady=20, command=lambda: tlacitko_pridat(6))
tlacitko_7 = Button(gui, text="7",padx=40, pady=20, command=lambda: tlacitko_pridat(7))
tlacitko_8 = Button(gui, text="8",padx=40, pady=20, command=lambda: tlacitko_pridat(8))
tlacitko_9 = Button(gui, text="9",padx=40, pady=20, command=lambda: tlacitko_pridat(9))
tlacitko_0 = Button(gui, text="0",padx=40, pady=20, command=lambda: tlacitko_pridat(0))

tlacitko_plus = Button(gui, text="+",padx=39, pady=20, command=tlacitko_plus)
tlacitko_rovnase = Button(gui, text="=",padx=88, pady=20, command=tlacitko_rovnase)
tlacitko_vymaz = Button(gui, text="Vymaz",padx=75, pady=20, command=tlacitko_vymazat)

tlacitko_1.grid(row=3, column=0,)
tlacitko_2.grid(row=3, column=1,)
tlacitko_3.grid(row=3, column=2,)

tlacitko_4.grid(row=2, column=0,)
tlacitko_5.grid(row=2, column=1,)
tlacitko_6.grid(row=2, column=2,)

tlacitko_7.grid(row=1, column=0,)
tlacitko_8.grid(row=1, column=1,)
tlacitko_9.grid(row=1, column=2,)

tlacitko_0.grid(row=4, column=0,)

tlacitko_rovnase.grid(row=4, column=1, columnspan=2)
tlacitko_plus.grid(row=5, column=0)
tlacitko_vymaz.grid(row=5, column=1, columnspan=2)



gui.mainloop()