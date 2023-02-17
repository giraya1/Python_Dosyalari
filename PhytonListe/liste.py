
liste = {}
a = 0

while a < 3:
    a += 1
    id = int(input("No giriniz:"))
    ad = str(input("Ad giriniz:"))
    soyad = str(input("Soyad giriniz:"))
    yas = int(input("yaş giriniz:"))

    liste.update({
        id: {
            "Adınız": ad,
            "Soyadınız": soyad,
            "Yaşınız": yas
        }

    }

    )
    print(liste)

ovno = input("Aradığınız numarayı giriniz:")
kisiler=liste[id]
print(kisiler)