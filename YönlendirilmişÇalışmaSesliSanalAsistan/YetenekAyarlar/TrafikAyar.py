import requests
import random


class Trafik_Ayar:
    def __init__(self):
        pass

    trafik_cumle = [
        "trafik", "trafik yoğunluğu", "trafik seviyesi", "trafik durumu nedir", "trafik ne durumda",
        "trafik nasıl", "trafik yoğunluğu nasıl", "yollar açık mı","trafik var mı","trafiği söyler misin","trafik ne durumda"


    ]
    def trafik_yogunlugu(self):



        Trafik ="https://api.ibb.gov.tr/tkmservices/api/TrafficData/v1/TrafficIndexHistory/1/5M"
        try:
            res= requests.get(url=Trafik)
            res.raise_for_status()


        except requests.exceptions.RequestException:
            return None

        else:

            yogunluk = res.json()
            if len(yogunluk) == 0:
                return None
            else:
                t_density = yogunluk[0].get("TrafficIndex")

        return self.__karsilastirma(t_density)

    def __karsilastirma(self, val):

            if val <= 30:
                val_eval = "düşük"
            elif val > 30 and val <= 44:
                val_eval = "orta"
            else:
                val_eval = "yüksek"


            cümle_secenek = [
                f" Trafiğe baktığımda {val} ile {val_eval} seviyede patron.",
                f"Bugün İstanbulda {val} ile {val_eval} seviyede patron.",
                f"İstanbulda bugün  {val} ile {val_eval} seviyede patron.",
                f"Bugün için trafik seviyesi İstanbulda {val} ile {val_eval} seviyede patron "
            ]
            return random.choice(cümle_secenek)




