from datetime import  datetime
import random

class Takvim:
    saat_cümle = [
        "saat", "saat kaç", "saati söyle",
        "şu an saat kaç", "saat kaç oldu",
        "saati söyleyebilir misin", "saat kaçı gösteriyor"
    ]
    tarih_cümle = [
        "tarih", "bugünün tarihi ne",  "bugün ayın kaçı", "hangi aydayız", "takvim", "tarihi söyler misin",
        "hangi gündeyiz", "bugün hangi gün", "ayın kaçındayız","ayın kaçı",


    ]

    def __init__(self):
        pass

    def saat_söyle(self):
        saat = datetime.now().hour
        dakika = str(datetime.now().minute)

        if saat in [1, 11, 21, 5, 15, 8, 18]:
            saat = str(saat) + " i"
        elif saat in [2, 12, 22, 7, 17, 20]:
            saat = str(saat) + " yi"
        elif saat in [6, 16]:
            saat = str(saat) + " yı"
        elif saat in [9, 19, 10]:
            saat = str(saat) + " u"
        elif saat in [4, 14, 3, 13, 23, 24]:
            saat = str(saat) + " ü"
        elif saat in [0, 00]:
            saat = str(saat) + " ı"
        else:
            saat = str(saat)

        sentences = [
            f"Saat, {saat} {dakika} geçiyor patron.",
            f"Şu anda saat {saat} {dakika} geçiyor patron.",
            f"Hemen bakıyorum patron. Şu an {saat} {dakika} geçiyor.",
            f"Şu anda {saat} {dakika} geçiyor patron.",
            f"Bakıyorum şu an {saat} {dakika} geçiyor patron."
        ]

        return random.choice(sentences)

    def tarih_söyle(self):
        aylar = [
            "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
            "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"
        ]
        gunler = [
            "Pazartesi", "Salı", "Çarşamba", "Perşembe",
            "Cuma", "Cumartesi", "Pazar"
        ]

        gun_sayi = datetime.now().day
        ay = datetime.now().month
        year = datetime.now().year
        onemli_gun = self.onemli_gun(gun_sayi, ay)


        gun = gunler[datetime.now().weekday()]
        ay = aylar[ay - 1]
        sentences = [
            f"Bugün {gun_sayi} {ay}, {gun} patron",
            f"Bugün tarih {gun_sayi} {ay}, {gun}'i gösteriyor patron",
            f"Tarihe  baktığımda {gun_sayi} {ay} {year}, {gun} patron.",
            f"{gun_sayi} {ay}, bugün günlerden {gun} patron.",
            f"Hemen bakıyorum {gun_sayi} {ay}, bugün günlerden {gun} patron."

        ]

        return (random.choice(sentences), onemli_gun)




    def onemli_gun(self, day, month):
        return None

