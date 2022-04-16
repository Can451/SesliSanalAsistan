import types
import os
import webbrowser
from AnaAyarlar.KonusmaAyar import KonusmaAyar
from YetenekAyarlar.TakvimAyar import Takvim
from YetenekAyarlar.TrafikAyar import Trafik_Ayar
from YetenekAyarlar.SelamlamaAyar import Selamlama
from YetenekAyarlar.EglenceAyar import Eglence

class Calistir:
    def __init__(self):
        self.soyle = KonusmaAyar().asistansesi

    def giriskontrol(self, input, keywords):
        return bool(any(key in input for key in keywords))

    def feedback(self,get_result,for_context):
        if isinstance(get_result, types.FunctionType):
            res = get_result()
        else:
            res = get_result

        if not res or isinstance(res,Exception):
            self.soyle(f"{for_context} bilgisine ulaşılamadı.")
        else:
            self.soyle(res)

    def calistir(self, input):
        if not input:
            return

        alinanses = input.casefold()

        if self.giriskontrol(alinanses, Takvim.saat_cümle):
            self.soyle(Takvim().saat_söyle())
        elif self.giriskontrol(alinanses, Selamlama.selamlama_cümle):
            self.soyle(Selamlama().selamlama_saat_ayar())
        elif self.giriskontrol(alinanses,Eglence.Güzel_Cümle):
            self.soyle(Eglence().güzel_cümle())
        elif self.giriskontrol(alinanses,Eglence.Espiri_Cümle):
            self.soyle(Eglence().espiri_cümle())
        elif self.giriskontrol(alinanses, Takvim.tarih_cümle):
            self.soyle(Takvim().tarih_söyle()[0])
        elif self.giriskontrol(alinanses, Trafik_Ayar.trafik_cumle):
            self.feedback(Trafik_Ayar().trafik_yogunlugu(), "Trafik Yoğunluğu")
        elif "müzik" in alinanses and alinanses.casefold():
            self.soyle("Hemen hallediyorum patron")
            os.startfile("C:\\Users\\Can\\OneDrive\Masaüstü\\Spotify.lnk")
        elif "google" in alinanses and alinanses.casefold():
            self.soyle("Hemen hallediyorum patron")
            os.startfile("C:\\Users\\Can\\OneDrive\Masaüstü\\Google Chrome")
        elif alinanses.casefold():

                arama = alinanses.casefold()
                site = "https://www.google.com/search?q={}".format(arama)
                webbrowser.get().open(site)
                self.soyle("{} i hemen araştırıyorum".format(arama))

























