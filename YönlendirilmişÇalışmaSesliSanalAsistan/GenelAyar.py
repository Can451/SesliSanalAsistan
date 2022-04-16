import json


Dosyaİsim = "düzen_ayarlari.json"
GenelDüzenleme = {
    "personalization": {
        "user": {
            "name": ""
        }
    },
    "speechRecognition": {
        "language": "tr_TR"
    },
    "speechGeneration": {
        "language": "tr",
        "tld": "com.tr",
        "slow_talk": "false"
    },
    "debug_mode": "true",
    "services": {

    }
}


def ayar_dosya():
    with open(Dosyaİsim, "w") as yeniayardosyası:
        json.dump(GenelDüzenleme, yeniayardosyası, indent=4)
    print("####---YENİ DÜZENLEME DOSYASI OLUŞTURURLUYOR---####")


def genelayarlar(param: str, *args):
    ayarlar = GenelDüzenleme.get(param)

    for arg in args[0]:
        d = ayarlar.get(arg)

        if d:
            if d == "true" or d == "false":
                ayarlar = bool(d == "true")
            else:
                ayarlar = d

    if isinstance(ayarlar, dict):
        return None
    else:
        return ayarlar


def GenelAyar(param: str, *args):
    try:
        with open(Dosyaİsim, "r") as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        ayar_dosya()
        return genelayarlar(param, args)
    else:
        bul = config_data.get(param)

        for arg in args:
            d = bul.get(arg)
            if d:
                if d == "true" or d == "false":
                    bul = bool(d == "true")
                else:
                    bul = d

        return bul if bul and not isinstance(bul, dict) \
            else genelayarlar(param, args)




