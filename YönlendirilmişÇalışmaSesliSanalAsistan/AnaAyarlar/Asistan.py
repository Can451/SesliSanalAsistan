import speech_recognition as sr
from AnaAyarlar.ArayüzAyarlar import Arayüz
from AnaAyarlar.CalistirAyar import Calistir

class Asistan(sr.Recognizer):
    def __init__(self):
        super().__init__()

        self.arayuz_penceresi = Arayüz()
        self.konusmaya_basla = self.arayuz_penceresi.arayüz_düzenleme(command = self.asistan_calis)
        self.calistir=Calistir()

    def arayüz_basla(self):
        self.arayuz_penceresi.mainloop()

    def kullanilabilir_mikrofonlar(self):
        from prettytable import PrettyTable
        yazdir = PrettyTable()
        yazdir.title="Kullanılabilir Mikrofonlar"
        yazdir.field_names=["Numara","Mikrofon İsmi"]
        yazdir.add_rows(enumerate(sr.Microphone.list_microphone_names()))
        yazdir.align="l"
        print(yazdir)

    def tus_yazi_ayar(self, is_listening):
        tusyazi = "Dinliyorum..." if is_listening else "Konuşmak için Bas"
        self.konusmaya_basla.config(text=tusyazi)
        self.konusmaya_basla.update()

    def sesalgilama(self):
        try:
            with sr.Microphone() as source:
                self.tus_yazi_ayar(True)


                audio = self.listen(source)
                try:
                    new_input = self.recognize_google(audio_data=audio, language="tr_TR")
                except sr.UnknownValueError:
                    print("Anlayamadım")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                else:
                    return new_input
        except:
            self.arayuz_penceresi.mikrofon_bulunamadi()
        finally:
            self.tus_yazi_ayar(False)

    def asistan_calis(self):


            sesalma = self.sesalgilama()

            self.calistir.calistir(sesalma)



