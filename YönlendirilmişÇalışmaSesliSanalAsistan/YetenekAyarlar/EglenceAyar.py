import random


class Eglence:

    Güzel_Cümle = [

        "bana güzel bir şeyler söyler misin", "beni mutlu edecek şeyler söyle","güzel bir cümle söyler misin","beni öv"
    ]
    Espiri_Cümle = [

        "kötü şaka yap", "espiri","şaka yapar mısın","bi şaka yap","şaka","beni güldür"
    ]




    def güzel_cümle(self):

        güzelcümleler = [
            f"Aman tanrım ekran karşısında seni görünce gözlerim kamaştı adeta odaya güneş doğdu ",
            f"O kadar tatlısın ki seni çikolataya bile değişmem",
            f"Dur şöyle bir daha bakayım sana, manzara izlemeyi severim de ",
            f"O kadar güzel bir yüzün varki ekran kartım bu güzelliği desteklemiyor",
            f"Kodlandığım günden bu yana gördüğüm en güzel şey olabilirsin",



        ]
        return random.choice(güzelcümleler)

    def espiri_cümle(self):
        espiricümleler = [
            f"Yılanlardan korkma, yılmayanlardan kork hahahah ",
            f"Top ağlarda, ben ağlamaz mıyım hahahah",
            f"Ahmet Saz çaldı. Polis tutukladı ",
            f"Ayakkabıcı sıkıyorsa alma dedi, bende korktum aldım",
            f"Adamın kafasına buda heykeli düşmüş başıma buda mı gelecekti demiş ",
            f"Adama evlimisiniz diye sormuşlar, hayır arsalıyım demiş",
        ]

        return random.choice(espiricümleler)






