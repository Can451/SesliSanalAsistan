from AnaAyarlar.Asistan import Asistan
from GenelAyar import GenelAyar

asistan = Asistan()

if GenelAyar("debug_mode"):
    asistan.kullanilabilir_mikrofonlar()

asistan.arayüz_basla()

