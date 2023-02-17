liste = dict()
a = 0

while a < 3:
    a += 1
    no = int(input("No giriniz:"))
    ad = str(input("Ad giriniz:"))
    soyad = str(input("Soyad giriniz:"))
    yas = int(input("yaş giriniz:"))

    liste.update({
        no: {
            "Adınız": ad,
            "Soyadınız": soyad,
            "Yaşınız": yas
        }
    })
    print(liste)

ovno = int(input("Aradığınız numarayı giriniz:"))
if ovno in liste:
    kisiler = liste[ovno]
    print(kisiler)
else:
    print("Kayıt bulunamadı")
