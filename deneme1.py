#sadece ilk harfleri büyük yapmak için
# ilk_harf_buyuk = "ne mutlu".capitalize()
# #bütün harfleri küçük yapmak için
# hepsi_kucuk = "NE MUTLU ".lower()
# #bütün harfleri büyük yapmak için
# hepsi_buyuk = "ne mutlu".upper()
#harfleri tersi yapmak için
# tam_tersi = "Ne MuTlU".swapcase()
# #belirtilen karakteri metinden silmek için
# sil = "+++ahmet+++".strip("+")


# print(ilk_harf_buyuk)
# print(hepsi_kucuk)
# print(hepsi_buyuk)
# print(tam_tersi)
# print(sil)

#sep parametresi ',' yerine koyulacak karakteri belirtir default olarak 'boşluk' tur.
# print("ahmet","said",sep="*")
#end parametresi metnin sonun ne koyulacağını belirtir.
# print("Ad Soyad",end=":")

# ad = "ahmet"
# soyad ="armağan"
# yas = 25

# print("Kişinin adı:{}\nKişinin Soyadı:{}\nKişinin Yaşı:{}".format(ad,soyad,yas))
  #üstteki satır ile aşağıdaki satır aynı sonucu verir
# print(f"Kişinin Adı:{ad}\nKişinin Soyadı:{soyad}\nKişinin yaşı:{yas}")


#KULLANICIDAN VERİ GİRİŞİ ALMAK İÇİN İNPUT() KULLANILIR
# kullanici_ad = input("Kullanıcı Adı Giriniz : ")
# kullanici_ps = int(input("Şifrenizi Giriniz : "))

# print(type(kullanici_ad))
# print(type(kullanici_ps))

#ORTAMALAYI BULAN PROGRAM
# vize = int(input("Vize Puanını Giriniz : "))
# final = int(input("Final Notunuzu Giriniz : "))
# ort = ((vize*0.30)+(final*0.70))

# print(f"Vize Notunuz : {vize}\nFinal Notunuz : {final}\nOrtalamanız : {ort}")


#FİNALDEN KAÇ ALINMASI GEREKİR PROGRAMI
# vize = int(input("Notu Giriniz : "))
# ort = 70
# final = ((ort-(vize*0.30))/0.70)
# if (vize >=70):
#     print("Final sınavından : 70 almanız yeterli.")
# else:
#     print(f"Final Sınavından {int(final)} notu almalısınız.")

#LİSTELER
# meyve = ["elma","erik",23]
# #listenin sonuna eklemek için kullanılıyor
# meyve.append("muz")

# print(meyve)
#  #listede belirtilen indexi değiştiriyoruz
# meyve[1] = "armut"

# print(meyve)
# #belirtilen indexi yazdırıyoruz
# #print(meyve[0])
# # 'a:b' a yerine başlaması gereken indexi yazıyoruz a'ncı indexi ekranda gösterir, b yerine bitmesi gereken indexi b'nci index ekrana yazdırılmaz
# #üstteki satırın özeti a'ncı indexten a dahil b'nci indexe kadar b dahil değil ekrana yazdırır
# print(meyve[1:3])
# # 2'nci indexe kadar olan değerlere yeni değerler atamak için
# meyve[:2] = ["Fenerbahçe","6Saray"]

# print(meyve)

#DEMETLER 'tuple'

# teams = ("Fenerbahçe","Kayserispor","Madrid FC","Barcelona")

# print(type(teams))
# print(teams)
# ilk index için
# print(teams[0])
# son index için
# print(teams[-1])

# ÖNEMLİ NOT
# Demetler ile listeler arasındaki fark demetlerin güncellenemeyeceği
#demetlere en başında girilen veriler sabit değişmez

#OPERATÖRLER

# x = 5
# y = 2
# x += y
# print(x)
# # x'in y'nci kuvvetini alıp ardından x'e eşitlemek için kullanılan operatör
# x **= y
# print(x)

#KARŞILAŞTIRMA OPERATÖRLERİ
#eşit mi
# deneme = 5==5
# print(deneme)
#eşit değil mi
# deneme1 = 5!=4
# print(deneme1)
#küçük mü
# deneme2 = 5<6
# print(deneme2)
#büyük mü
# denem3 = 5>4
# print(denem3)
#küçük eşit mi
# deneme4 = 5<=5
# print(deneme4)
#büyük eşit mi
# deneme5 = 5>=5
# print(deneme5)

#MANTIKSAL OPERATÖRLER
# and operatöründe iki koşul da true olursa çıktı true olur
# deneme6 = 8<10 and 4>3
# print(deneme6)

# or operatöründe koşullardan birinin doğru olması yeterli
# deneme7 = 4<5 or 3>4
# print(deneme7)

#KOŞULLAR

# ders seçim uygulaması
# ders1, ders2, ders3, ders4 = "Matematik", "Türkçe", "İngilizce", "Sosyal"
# yildiz = "*"
# ders_secim = int(input(f"1-{ders1}\n2-{ders2}\n3-{ders3}\n4-{ders4}\n Yukarıdaki derslerden birini seciniz : "))

# if ders_secim == 1:
#     print(yildiz*len(ders1))
#     print(f"{ders1} dersini seçtiniz.")
#     print(yildiz*len(ders1))
#     vize = int(input("Vize Notunuzu Giriniz : "))
#     final = int(input("Final Notunuzu Giriniz : "))
#     ort = (vize*0.30)+(final*0.70)
#     if ort <=70:
#         print(f"Ortalamanız : {ort}\n{yildiz*20}\nDersten kaldınız!!!\n{yildiz*20}")
#     elif ort >=70:
#         print(f"Ortalamanız : {ort}\n{yildiz*20}\nDersten Geçtiniz. :) \n{yildiz*20}")
#     else:
#         print("!!!!!Birşeyler Yanlış Gitti!!!!")
# elif ders_secim == 2:
#     print(yildiz*len(ders2))
#     print(f"{ders2} dersini seçtiniz.")
#     print(yildiz*len(ders2))
#     vize = int(input("Vize Notunuzu Giriniz : "))
#     final = int(input("Final Notunuzu Giriniz : "))
#     ort = (vize*0.30)+(final*0.70)
#     if ort <=70:
#         print(f"Ortalamanız : {ort}\n{yildiz*20}\nDersten kaldınız!!!\n{yildiz*20}")
#     elif ort >=70:
#         print(f"Ortalamanız : {ort}\n{yildiz*20}\nDersten Geçtiniz. :) \n{yildiz*20}")
#     else:
#         print("!!!!!Birşeyler Yanlış Gitti!!!!")
# elif ders_secim == 3:
#     print(yildiz*len(ders3))
#     print(f"{ders3} dersini seçtiniz.")
#     print(yildiz*len(ders3))
#     vize = int(input("Vize Notunuzu Giriniz : "))
#     final = int(input("Final Notunuzu Giriniz : "))
#     ort = (vize*0.30)+(final*0.70)
#     if ort <=70:
#         print(f"Ortalamanız : {ort}\n{yildiz*20}\nDersten kaldınız!!!\n{yildiz*20}")
#     elif ort >=70:
#         print(f"Ortalamanız : {ort}\n{yildiz*20}\nDersten Geçtiniz. :) \n{yildiz*20}")
#     else:
#         print("!!!!!Birşeyler Yanlış Gitti!!!!")
# elif ders_secim == 4:
#     print(yildiz*len(ders4))
#     print(f"{ders4} dersini seçtiniz.")
#     print(yildiz*len(ders4))
#     vize = int(input("Vize Notunuzu Giriniz : "))
#     final = int(input("Final Notunuzu Giriniz : "))
#     ort = (vize*0.30)+(final*0.70)
#     if ort <=70:
#         print(f"Ortalamanız : {ort}\n{yildiz*20}\nDersten kaldınız!!!\n{yildiz*20}")
#     elif ort >=70:
#         print(f"Ortalamanız : {ort}\n{yildiz*20}\nDersten Geçtiniz. :) \n{yildiz*20}")
#     else:
#         print("!!!!!Birşeyler Yanlış Gitti!!!!")
# else:
#     print("Hatalı Seçim Yaptınız!!! \nLütfen Tekrar Seçin")


#DÖNGÜLER


#WHİLE DÖNGÜSÜ
# sayi = 1

# while sayi<=10:
#   print("**")
#   print(sayi)
#   sayi+=1
#   print("**")

# k_adi = "admin"
# pss = "1234"

# while True:
#   kullaniciAdi = input("Kullanıcı Adını Giriniz : ")
#   kullaniciPss = input("Şifrenizi Giriniz : ")

#   if (k_adi == kullaniciAdi) and (pss == kullaniciPss):
#     print("Sisteme Başarıyla Giriş Yapıldı.")
#     print("***********\nHoşgeldiniz\n***********")
#     break
#   elif (k_adi==kullaniciAdi) and (pss != kullaniciPss):
#     print("!!!!! Hatalı Şifre Girdiniz !!!!!")
#     cvp = input("Şifreyi Değiştirmek İster Misiniz ? E\H\n").lower()
#     if cvp=="e":
#       yeni_sifre = input("Yeni Şifreyi Giriniz : \n")
#       pss = yeni_sifre
#     elif cvp=="h":
#       print("Eski Şifreni hatırlamaya çalış o zaman.")
#   elif (k_adi!=kullaniciAdi) and (pss == kullaniciPss):
#     print("!!!!! Kullanıcı Adını Hatalı Girdiniz !!!!!")
#   else:
#     print("Sen Kimsin Aq Herşeyi Yanlış Girdin.")

#FOR DÖNGÜSÜ

# liste = ["elma","armut","kiraz","erik"]

# for i in liste:
#   print(i)


# for i in range(11):
#   print(i)

# isim = "ahmet"

# for i in isim:
#   print("*")

# program 3 defa çalışacak
# for i in range(3):
#   sifre = input("Yeni Şifreyi Giriniz : ")
#   # kullanıcı bir değer girmezse bu koşul çalışacak
#   if not sifre:
#     print("Alan Boş Bırakılamaz.")
#     # eğer ki şifre 3 ile 8 karakter arasında ise program sonlanıcak
#   elif len(sifre) in range(3,8):
#     print(f"Yeni Şifreniz : {sifre}")
#     break
#   #for döngüsü 3 olduğunda program duracak 0,1,2
#   elif i == 2:
#     print("Çok Fazla Hatalı Deneme Yaptınız.....")
#     #yukarıdaki koşullar harici herhangibir koşulda aşağıdaki blok çalışacak
#   else:
#     print("Şifre 3 karakterden kısa 8 karakterden uzun olamaz.")

# kelimeleri ayırıp ekrana yazdıran program

# isim = input("İsminizi Giriniz : ")
# #kelimeyi bölüp ilk indexi ekrana yazdırır
# for i in isim.split():
#   print(i[0])


#FONKSİYONLAR
#temel fonksiyon örneği
# def topla():
#   a=int(input("İlk Sayıyı Giriniz : "))
#   b=int(input("İkinci Sayıyı Giriniz : "))
#   toplam=a+b
#   print(f"İşlem Sonucu : {toplam}")

# topla()

#fonksiyonlarda parametre kullanımı

# def kullaniciBilgileri (ad,soyad,yas,meslek):
#   print(f"Adınız : {ad}\nSoyadınız : {soyad}\nYaşınız : {yas}\nMesleğiniz : {meslek}")
#   print("*"*10)

# ad = input("Adınızı Giriniz : ")
# soyad = input("Soyadınızı Giriniz : ")
# yas = input("Yaşınızı Giriniz : ")
# meslek = input("Mesleğinizi Giriniz : ")

# kullaniciBilgileri(ad,soyad,yas,meslek)

# def su_hesabi (kilo):
#   e_hesap = kilo*0.04
#   k_hesap = kilo*0.03

#   cinsiyet = input("Lütfen Cinsiyetinizi Belirtiniz ? (E/K)\n").lower()

#   if cinsiyet == "e":
#     print(f"İçmeniz gereken su miktarı {e_hesap} litredir.")
#   elif cinsiyet == "k":
#     print(f"İçmeniz gereken su miktarı {k_hesap} litredir.")
#   else:
#     print("Cinsiyeti Hatalı Girdiniz.")

# kilo = int(input("Lütfen Kilonuzu Gİriniz : "))
# su_hesabi(kilo)

#return komutu

# def topla(a,b):
#   toplam = a+b
#   return (toplam)

# a = int(input("Sayı Gir : "))
# b = int(input("Sayı Gir : "))

# c = 5
# #return komutuyla fonksiyona global de bir değer olarak gösterebiliyoruz
# ilk = topla(a,b)
# print(ilk+c)

#fonksiyon parametrelerinde default değer
#eğer ki default olması gereken değişkeni sona yazmazsanız syntax hatası alınır
#onun için defaultu sona atamak gerekir ya da hepsine default atamalısınız
# def k_info(ad,soyad="boş bırakıldı",yas=25,meslek="boş bırakıldı"):
#   print(f"Adınız : {ad}\nSoyadınız : {soyad}\nYaşınız : {yas}\nMesleğiniz : {meslek}")

# k_info("ahmet","said")

# FONKSİYONUN İÇİNDE TANIMLANAN DEĞİŞKEN GLOBAL DENİLEREK TANIMLANDIĞINDA
# HERYER DE KULLANILABİLİR

#SÖZLÜKLER

# menu = {"Su":"25","Latte":"90","Türk Kahvesi":"75"}
# #sözlük içindeki değer için
# # print(menu["Su"]) 
# #sözlük içindeki hem keys hem de values görüntülenmesi için
# for i,j in menu.items():
#   print(i,j)

# puan_durumu = {"Fenerbahçe":"99 Puan","Kasımpaşa":"95 Puan",
#                 "Karagümrük":"93 Puan"}

# takim = input("Takım giriniz : ").capitalize()

# if takim not in puan_durumu:
#   print("Böyle bir takım yok...")
# else:
#   print(takim,":",puan_durumu[takim])

#yukarıdaki kod bloğunu kısası

# print(takim,":",puan_durumu.get(takim,"Böyle bir takım yok..."))

#sözlüğe veri ekleme puan_durumu isimli sözlüğü kullanıyorum tekrar yazmak yerine

# puan_durumu.setdefault("EdirneSpor","100 Puan")

# print(puan_durumu)

# takim = input("Takım Adını Giriniz : ").capitalize()
# puan = input("Puanını Giriniz : ")
# #kullanıcı puan kelimesini yazmazsa diye
# # puan += " Puan"
# #veri eklenen yer
# # puan_durumu.setdefault(takim,puan)
# # print(puan_durumu)

# #VERİ SİLME
# puan_durumu.pop("Kasımpaşa")

# for i,j in puan_durumu.items():
#   print(i,":",j)
#   print("-"*10)
