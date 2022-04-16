from gtts import gTTS
import os
from playsound import playsound
from GenelAyar import GenelAyar

SesDosyası = "temp.mp3"

class KonusmaAyar:
    def __init__(self):
        self.lang = GenelAyar("speechGeneration", "language")
        self.tld = GenelAyar("speechGeneration", "tld")
        self.slow_talk = GenelAyar("speechGeneration", "slow_talk")

    def asistansesi(self, text):
        try:
            tts = gTTS(text=text, lang=self.lang, tld=self.tld, slow=self.slow_talk)
            tts.save(SesDosyası)
        except UnicodeDecodeError as err:
            print(err)
        else:
            playsound(SesDosyası)
        finally:
            os.remove(SesDosyası)