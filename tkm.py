import random
import time

kullanici_skor, bilgisayar_skor = 0,0

while True:
    girilen_hareket = input("Lütfen bir hareket girin : " + "Taş (1), Kağıt (2), Makas (3)" + "\n" + "Oyunu bitirmek için 'q' tuşuna basın ve enterleyin." + "\n")
    rastgele_hareket = random.choice(['1', '2', '3'])

    if girilen_hareket == "1":
        if rastgele_hareket == "1":
            print("Berabere, yazılım taşı seçmişti.")
        elif rastgele_hareket == "2":
            print("Kaybettiniz, yazılım kağıdı seçmişti.")
            bilgisayar_skor += 1
        elif rastgele_hareket == "3":
            print("Kazandınız, yazılım makası seçmişti.")
            kullanici_skor += 1

    
    elif girilen_hareket == "2":
        if rastgele_hareket == "2":
            print("Berabere, yazılım kağıdı seçmişti.")
        elif rastgele_hareket == "1":
            print("Kazandınız, yazılım taşı seçmişti.")
            kullanici_skor += 1
        elif rastgele_hareket == "3":
            print("Kaybettiniz, yazılım makası seçmişti.")
            bilgisayar_skor += 1
    
    elif girilen_hareket == "3":
        if rastgele_hareket == "3":
            print("Berabere, yazılım makası seçmişti.")
        elif rastgele_hareket == "2":
            print("Kazandınız, yazılım kağıdı seçmişti.")
            kullanici_skor += 1
        elif rastgele_hareket == "1":
            print("Kaybettiniz, yazılım taşı seçmişti.")
            bilgisayar_skor += 1

    elif girilen_hareket == "q":
        print("Oyun bitirildi. Skor tablosu getiriliyor.", "\n", "-"*(41), sep="")
        break
    else:
        print("Parantez içindeki sayılardan birini girin.")

print("Sizin skorunuz: {} \nYazılımın skoru: {}".format(kullanici_skor, bilgisayar_skor), "\n", "-"*(41), sep="")
