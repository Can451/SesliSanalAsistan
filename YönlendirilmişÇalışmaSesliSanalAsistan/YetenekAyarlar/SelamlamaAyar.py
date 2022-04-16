from datetime import datetime


class Selamlama:
    selamlama_cümle = [
        "merhaba","selamlar", "günaydın", "tünaydın", "iyi akşamlar", "iyi geceler",
        "naber", "ne haber", "nasılsın"
    ]



    def __init__(self):
        pass

    def selamlama_saat_ayar(self):
        saat = datetime.now().hour
        if saat >= 5 and saat < 12:
            return f"Günaydın patron ."
        elif saat >= 12 and saat < 18:
            return f"Tünaydın patron ."
        else:
            return f"İyi akşamlar patron ."


