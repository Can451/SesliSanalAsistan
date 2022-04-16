from tkinter import *
from  tkinter import  messagebox

YaziTipi = ("Avenir",25,"bold")
Tus = ("Avenir",25,"bold")



class Arayüz(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sanal Asistan")
        self.config(padx=50, pady=50)

    def arayüz_düzenleme(self,command):
        yazitipi= Label(text="Asistan")
        yazitipi.config(pady=20, font=YaziTipi)
        yazitipi.pack()

        konusbuton = Button(text="Görev vermek için dokun", command=command)
        konusbuton.config(widt=40, pady=40, font=Tus)

        konusbuton.pack()
        return konusbuton

    def mikrofon_bulunamadi(self):
        messagebox.showinfo(title="HATA", message="Mikrofon Bulunamadı")