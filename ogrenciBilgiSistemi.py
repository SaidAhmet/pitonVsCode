
# Bu programda iki kullanıcı olucak ; öğrenci ve öğretmen
# öğrenci öğretmenin veritabanına eklediği dersleri ve aldığı notları görüntüleyip 
# kişisel bilgilerini düzenleyebilecek
# öğretmen ; veritabanına ders ekleyip öğrencilere not verebilecek
# öğrencilerin devam durumlarını güncelleyebilecek
# sistem öğretmenin veri tabanına girdiği derslerin ders saatine göre otomatik olarak 
# devamsızlık hakkı hesaplayıp öğrenciyi devamdan bırakabilecek

# ilk önce veri tabanı bağlantısı kurup tabloları oluşturucaz
#veri tabanı bağlantısı için kullanıyoruz
import pypyodbc


# server bağlantısı için aşağıdaki kod bloğunu kullanıyoruz
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=AHMETSAID;'
    'Database=obs;'
    'Trusted_Connection=True;'
)

imlec = db.cursor()

class ogrenci:
    def __init__(self,ogrAd,ogrSoyad,ogrNo):
        self.ogrAd = ogrAd
        self.ogrSoyad = ogrSoyad
        self.ogrNo = ogrNo

class dersler():
    def __init__(self,dersKodu,dersAdi,teoSaat,uygSaat):
        self.dersKodu = dersKodu
        self.dersAdi = dersAdi
        self.teoSaat = teoSaat
        self.uygSaat = uygSaat       

class devamHakkı(dersler):
    def __init__(self, dersKodu, dersAdi, teoSaat, uygSaat,kalanTeo,kalanUyg):
        super().__init__(dersKodu, dersAdi, teoSaat, uygSaat)
        self.kalanTeo = kalanTeo
        self.kalanUyg = kalanUyg

def ogrEkle():
    ogrAd = input("Öğrenci Adını Giriniz : ")
    ogrSoyad = input("Öğrenci Soyadını Giriniz : ")
    ogrNo = input("Öğrenci Numarasını Giriniz : ")
    a = ogrenci(ogrAd,ogrSoyad,ogrNo)
    imlec.execute(f"INSERT INTO ogrenciler VALUES('{a.ogrNo}','{a.ogrAd}','{a.ogrSoyad}')")
    db.commit()


def ogrGor():
    imlec.execute("SELECT * FROM ogrenciler")
    goster = imlec.fetchall()

    for i in goster:
        print(f"Öğrenci Adı : {i[2]}\nÖğrenci Soyadı : {i[3]}\nÖğrenci Numarası : {i[1]}")

def dersEkle():
    dersAdi = input("Ders Adını Giriniz : ")
    dersKodu = input("Ders Kodunu Giriniz : ")
    teoSaat = int(input("Teorik Saati Giriniz : "))
    uygSaat = int(input("Uygulama Saatini Giriniz : "))
    a = dersler(dersAdi,dersKodu,teoSaat,uygSaat)
    imlec.execute(f"INSERT INTO dersler VALUES('{a.dersKodu}','{a.dersAdi}','{a.teoSaat}','{a.uygSaat}')")
    db.commit()

def dersGor():
    imlec.execute("SELECT * FROM dersler")
    goster = imlec.fetchall()
    for i in goster:
        print(f"Ders Kodu : {i[1]}\nDers Adı : {i[2]}\nTeorik Saat : {i[3]}\nUygulama Saat : {i[4]}")

def devamGir():
    teo = int(input("Teorik Derslerde Yapılan Devamsızlık : "))
    uyg = int(input("Uygulama Derslerinde Yapılan Devamsızlık : "))
    


# ogrEkle()
# ogrGor()
dersEkle()
dersGor()