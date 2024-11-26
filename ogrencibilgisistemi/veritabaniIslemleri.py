# mssql veritabanı dosyası
import pypyodbc
import time

# veritabanı bağlantısı
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=AHMETSAID;'
    'Database=obs;'
    'Trusted_Connection=True;'
)


# veritabanı içinde gezinmek için
imlec = db.cursor()

# tabloları oluşturduğumuz kısım 
# # öğrencilerin bilgilerinin tutulduğu tablo
# imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ogrNo int not null, ogrAd varchar(50) not null, ogrSoyad varchar(50) not null)")
# # ders bilgilerinin tutulduğu tablo
# imlec.execute("CREATE TABLE IF NOT EXISTS dersler (dersKodu int not null, dersAdi varchar(50) not null, dersTeoSaat int, dersUygSaat int)")
# # devamsızlık durum tablosu
# imlec.execute("CREATE TABLE IF NOT EXISTS devamBilgisi (ogrNo int not null, dersKodu varchar(50) not null, devamsizSaat int )")
# # notların tutulduğu tablo
# imlec.execute("CREATE TABLE IF NOT EXISTS notDurumu (ogrNo int not null, dersKodu varchar(50) not null, vize int, final int, ortalama float, agNo float, harfNotu varchar(20) )")



def ogrenciEkle(ogrNo,ogrAd,ogrSoyad):
    # ogrNo = int(input("Öğrenci Numarası : "))
    # ogrAd = input("Öğrenci Adını Giriniz : ")
    # ogrSoyad = input("Öğrenci Soyadını Giriniz : ")
    imlec.execute(f"INSERT INTO ogrenciler VALUES('{ogrNo}','{ogrAd}','{ogrSoyad}')")
    db.commit()
    # yoruma aldığım satırları ana programda yazıcam bu dosyayı main.py dosyasına import edicem
    # print("Öğrenci Ekleniyor...")
    # for i in range(0,5):
    #     print("*", end = "", flush=True)
    #     time.sleep(1)
    # print(f"{ogrNo} numaralı öğrenci sisteme eklendi.")


def dersEkle(dersKodu,dersAdi,dersTeoSaat,dersUygSaat):
    # dersKodu = int(input("Öğrenci Numarası : "))
    # dersAdi = input("Öğrenci Adını Giriniz : ")
    # dersTeoDevHak = input("Öğrenci Soyadını Giriniz : ")
    # dersUygDevHak = input("Öğrenci Soyadını Giriniz : ")
    imlec.execute(f"INSERT INTO dersler VALUES('{dersKodu}','{dersAdi}','{dersTeoSaat}','{dersUygSaat}')")
    db.commit()


def devamDurumuEkle(ogrNo,dersKodu,dsizTeoSaat,dsizUygSaat):
    imlec.execute(f"INSERT INTO devamBilgisi VALUES('{ogrNo}','{dersKodu}','{dsizTeoSaat}','{dsizUygSaat}')")
    db.commit()


def notGir(ogrNo,dersKodu,vize,final,ortalama,agNo,harfNotu):
    imlec.execute(f"INSERT INTO notDurumu VALUES('{ogrNo}','{dersKodu}','{vize}','{final}','{ortalama}','{agNo}','{harfNotu}')")
    db.commit()



def ogrencileriGor():
    imlec.execute("SELECT * FROM ogrenciler")
    gor = imlec.fetchall()
    for i in gor:
        print(f"Öğrenci Numarası : {i[0]}\nÖğrenci Adı : {i[1]}\nÖğrenci Soyadı : {i[2]}")
        print("-"*50)

def dersleriGor():
    imlec.execute("SELECT * FROM dersler")
    gor = imlec.fetchall()
    for i in gor:
        print(f"Ders Kodu : {i[0]}\nDers Adı : {i[1]}\nTeorik Saati : {i[2]}\nUygulama Saati : {i[3]}")
        print("-"*50)


def dersNotGor(dersKodu):
    imlec.execute(f"SELECT * FROM notDurumu WHERE {dersKodu}")
    gor = imlec.fetchall()
    for i in gor:
        print(f"Öğrenci Numarası : {i[0]}\nDers Kodu : {i[1]}\nVize Notu : {i[2]}\nFinal Notu : {i[3]}\nOrtalama Not : {i[4]}\nAgNo : {i[5]}\nHarf Notu : {i[6]}")


# buraya öğrenci dersnotu görüntüleme, tek bir öğrenci bilgileri görme(aldığı dersleri de dahil ederek), gelicek yarın













# bunu can sıkıntısına yaptım
# print("Yükleniyor..",end="",flush=True)
# for i in range(0,5):
#     print(".",end="",flush=True)
#     time.sleep(1)