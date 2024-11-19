#***************ÇEKİLİŞ UYGULAMASI****************
#amaç : bir listeye kişiler eklenicek ver ardından rastgele içinden 
#kazananlar çekilecek

import random

kullanicilar = list()

def kullaniciEkle(a):
    i = 0
    while True:
        yeni_kullanici = input("Listeye eklemek istediğiniz kişileri yazınız : ")
        a.append(yeni_kullanici)
        secim = input("Başka Kullanıcı Eklemek İster Misiniz ? (E/H)").lower()
        if secim == "e":
            continue
        elif secim == "h":
            break

# kullaniciEkle(kullanicilar)

def listeyiGoster(a):
    x = 0
    for i in a:
        x+=1
        print(f"Listede ki {x}'nci eleman : {i}")
        
def karistir(a):
    random.shuffle(a)

while True:
    secim = int(input("1-Listeyi Görüntüle\n2-Listeye Kullanıcı Ekle\n3-Listeyi Karıştır\n4-Çekiliş Yap\n5-Çıkış Yap\n"))
    if secim == 1:
        listeyiGoster(kullanicilar)
    elif secim == 2:
        kullaniciEkle(kullanicilar)
    elif secim == 3:
        print("Liste Karıştırılıyor...")
        karistir(kullanicilar)
    elif secim == 4:
        print("Çekiliş Yapılıyor....")
        sonuc = random.sample(a,1)
        print("Kazanan Talihli : ")
    elif secim == 5:
        break
