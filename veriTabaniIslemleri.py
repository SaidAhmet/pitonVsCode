# burada veritabanı kütüphanesini çağırıyoruz
import sqlite3
# veritabanı bağlantısını sağlıyoruz
# db = sqlite3.connect("deneme.db")
# veritabanı üzerinde gezinmek için bu komuta ihtiyacımız var
# yetki = db.cursor()
# ad = input("Adınızı Giriniz : ")
# soyAd = input("Soyadınızı Giriniz : ")
# yas = input("Yaşınızı Giriniz : ")
# tablo oluşturmak için create table ifadesi kullanılır
# parantez içerisine tablo bulunması gereken sütun isimleri yazılır
# IF NOT EXISTS kullanılmazsa ve tablo halihazırda var ise program hata verir
# yetki.execute("CREATE TABLE IF NOT EXISTS dEnEmE(ad,soyad,numero)")
# insert into ifadesi ile var olan sütunlara sırasıyla veri girişi yapılır
# yetki.execute(f"INSERT INTO dEnEmE VALUES ('{ad}','{soyAd}','{yas}')")
# veritabanında bir alanı seçmek için kullanılır
# veritabanından veri çekmek için kullanılır '*' ifadesi herşeyi kapsar
# select ten sonra ekranda görünecek kısım yazılır from hangi tablodan çekileceğini ifade eder
# yetki.execute("SELECT * FROM dEnEmE")
# where den sonra koşul belirtiyoruz
# yetki.execute("SELECT * FROM dEnEmE WHERE numero='24' and ad='ahmet'")
# yetki.execute("SELECT ad FROM dEnEmE WHERE numero='24' or ad='ahmet'")
# seçili alanın hepsini gösteren builtin function
# yazdir = yetki.fetchall()
#  yetki.fetchmany(2) ifadesi ile kaç tane veri çekilmesinin belirtiriz içindeki değeri
# boş bırakırsak ilk satırı verir verileri çekerkende en yukarıdaki veriden başlar
# print(yazdir)
# ekran çıktısı daha güzel olması için
# for i in yazdir:
    # print(i)
    # daha güzel ekran çıktısı
    # print(f"Ad : {i[0]} ")#\nSoyad : {i[1]}\nYaş : {i[2]}")
    # print("*"*15)







# verinin veritabanına yazılabilmesi için commit ifadesi kullanılır
# db.commit()
# veritabanını kapatmak için kullanılır
# db.close()


# ******************* VERESİYE DEFTERİ ÖRNEĞİ *******************

# kurs hocasının yaptığı

db = sqlite3.connect("veresiyeDefteri.db")

imlec = db.cursor()

imlec.execute("""CREATE TABLE IF NOT EXISTS veresiyeDef(isim TEXT, borc INTEGER)""")

# while True:
#     print("***Veresiye Defterine Hoşgeldiniz***")
#     secim = input("1-Borçlu Ekle\n2-Borçluları Gör\n")
#     if secim == "1":
#         borcluAdi = input("Borçlunun Adını Giriniz : ")
#         borcMiktari = input("Borç Miktarını Yazınız : ")
#         imlec.execute(f"INSERT INTO veresiyeDef VALUES('{borcluAdi}','{borcMiktari}')")
#         db.commit()
#         print(f"{borcluAdi} adlı kişi borç listesine eklendi.")
#     elif secim == "2":
#         imlec.execute("SELECT * FROM veresiyeDef")
#         gor = imlec.fetchall()
#         for i in gor:
#             print(f"{i[0]} adlı kişinin borç miktarı {i[1]} TL'dir.")


# BENİM YAPTIĞIM


def ekle(x,y):
    imlec.execute(f"INSERT INTO veresiyeDef VALUES('{x}','{y}')")
    db.commit()

def ekranaYaz(x):
    for i in x:
        print(f"{i[0]} adlı kişinin borcu {i[1]} TL'dir.")
        print("*"*20)

def hepsiniGoster():
    imlec.execute("SELECT * FROM veresiyeDef")
    bak = imlec.fetchall()
    ekranaYaz(bak)


def kucukBuyukGor(x,y,z):
    if x == "1":
        if y == "1":
            imlec.execute(f"SELECT * FROM veresiyeDef WHERE borc < {z}")
            bak = imlec.fetchall()
            ekranaYaz(bak)
        elif y == "2":
            imlec.execute(f"SELECT * FROM veresiyeDef WHERE borc > {z}")
            bak = imlec.fetchall()
            ekranaYaz(bak)
    elif x == "2":
        hepsiniGoster()


while True:
    print("***VERESİYE DEFTERİNE HOŞGELDİNİZ***")
    secim = input("1-Borçlu Ekle\n2-Borçluları Gör\n3-Çıkış Yap\n")
    if secim == "1":
        ad = input("Borçlu Adını Giriniz : ")
        borc = int(input("Borç Miktarını Giriniz : "))
        ekle(ad,borc)
    elif secim == "2":
        secim1 = input("1-Spesifik Sorgulama\n2-Hepsini Gör\n")
        if secim1 == "1":
            secim2 = input("1-Belirlediğiniz Sayıdan Az Olanlar\n2-Belirlediğiniz Sayıdan Büyük Olanlar\n")
            if secim2 == "1":
                sayi = int(input("Miktar Giriniz : "))
                print(f"{sayi} TL'den az borcu olanlar : ")
                kucukBuyukGor(secim1,secim2,sayi)
            elif secim2 == "2":
                sayi = int(input("Miktar Giriniz : "))
                print(f"{sayi} TL'den fazla borcu olanlar : ")
                kucukBuyukGor(secim1,secim2,sayi)
        elif secim1 == "2":
            hepsiniGoster()
    elif secim == "3":
        break
