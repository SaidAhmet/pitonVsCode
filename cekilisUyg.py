#***************ÇEKİLİŞ UYGULAMASI****************
#amaç : bir listeye kişiler eklenicek ver ardından rastgele içinden 
#kazananlar çekilecek

import random
import time

#********************BU BENİM YAPTIĞIM********************

# kullanicilar = list()

# def kullaniciEkle(a):
#     i = 0
#     while True:
#         yeni_kullanici = input("Listeye eklemek istediğiniz kişileri yazınız : ")
#         a.append(yeni_kullanici)
#         secim = input("Başka Kullanıcı Eklemek İster Misiniz ? (E/H)").lower()
#         if secim == "e":
#             continue
#         elif secim == "h":
#             break
#         else:
#             print( "Hatalı Giriş Yaptınız...\nTekrar Giriş Yapınız...\n")

# # kullaniciEkle(kullanicilar)

# def listeyiGoster(a):
#     x = 0
#     for i in a:
#         x+=1
#         print(f"Listede ki {x}'nci eleman : {i}")
        
# def karistir(a):
#     random.shuffle(a)

# while True:
#     secim = int(input("1-Listeyi Görüntüle\n2-Listeye Kullanıcı Ekle\n3-Listeyi Karıştır\n4-Çekiliş Yap\n5-Çıkış Yap\n"))
#     if secim == 1:
#         listeyiGoster(kullanicilar)
#     elif secim == 2:
#         kullaniciEkle(kullanicilar)
#     elif secim == 3:
#         print("Liste Karıştırılıyor...")
#         karistir(kullanicilar)
#         print("Liste Karıştırıldı!!!")
#     elif secim == 4:
#         print("Çekiliş Yapılıyor....")
#         sonuc = random.sample(kullanicilar,1)
#         print(f"Kazanan Talihli : {sonuc}")
#     elif secim == 5:
#         break



#********************BU HOCANIN YAPTIĞIM********************


kullanicilar = list()

#kullanıcı ekleme fonksiyonu
def kullanici_ekle(x):
    print("-"*30)
    print("Kullanıcı Ekleme Ekranına Hoşgeldiniz")
    ekle = input("Lütfen eklenecek kullanıcıyı yazınız : ")
    kullanicilar.append(ekle)

#kullanıcı görme ekranı
def kullanici_gor(x):
    say = 1
    print("-"*30)
    for i in x:
        print(str(say)+"-Kullanıcı Adı: ",i)
    print("-"*30)
    
#programa rastgele seçim yaptırdığımız yer

def sec(x):
    say = 1
    kisi_sec = int(input("Kaç Kişi Seçilsin ? : "))
    rastgele_sec = random.sample(x,kisi_sec)
    print("Rastgele seçiliyor....")
    time.sleep(3)

    for i in rastgele_sec:
        print(str(say)+"-kullanıcı adı : ",i)
        say +=1
    print("-"*30)
    
def karistir(x):
    print("-"*30)
    say = 1
    random.shuffle(x)
    for i in x:
        print(str(say)+"-kullanıcı adı : ",i)
        say+=1
    print("-"*30)


while True:
    print("***Çekiliş Uygulamasına Hoşgeldiniz")
    secim = int(input("1-Kullanıcı Ekle\n2-Kullanıcı Gör\n3.Kullanıcıları Karıştır\n4-Rastgele Seç\n"))
    if secim == 1:
        kullanici_ekle(kullanicilar)
    elif secim == 2:
        kullanici_gor(kullanicilar)
    elif secim == 3:
        karistir(kullanicilar)
    elif secim == 4:
        sec(kullanicilar)
    else:
        print("Hatalı Tuşlama Yaptınız...")