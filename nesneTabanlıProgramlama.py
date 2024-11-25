

# class galeri:
#     marka = "Ferrari"
#     km = 5000
#     renk = "Kırmızı"

#     def arabaOzellikleri (self):

#         print(f"Araba Markası : {self.marka}\nAraç KM Miktarı : {self.km}\nAraç Rengi : {self.renk}")


# ahmet = galeri()

# ahmet.arabaOzellikleri()

class okul:
    # yapıcı fonksiyon olarak geçen bölüm
    def __init__(self,sinif,ogretmen,bolum,mevcut):
        self.sinif = sinif
        self.ogretmen = ogretmen
        self.bolum = bolum
        self.mevcut = mevcut
    
    def bilgileriGoster(self):
        print(f"Sınıf : {self.sinif}\nÖğretmen : {self.ogretmen}\nBölüm : {self.bolum}\nMevcudu : {self.mevcut}")
        print("*"*25)

    def bransDegistir(self):
        yeniBrans = input("Lütfen yeni branşınızı giriniz : ")
        self.bolum = yeniBrans
        # print(f"Sınıf : {self.sinif}\nÖğretmen : {self.ogretmen}\nBölüm : {self.bolum}\nMevcudu : {self.mevcut}") 

class mudur(okul):
    def __init__(self, sinif, ogretmen, bolum, mevcut,brans):
        super().__init__(sinif, ogretmen, bolum, mevcut)
        self.brans = brans
    def bilgileriGoster(self):
        print(f"Sınıf : {self.sinif}\nÖğretmen : {self.ogretmen}\nBölüm : {self.bolum}\nMevcudu : {self.mevcut}\nBranş : {self.brans}")




birinciSinif = okul("11/A","Ahmet","Bilişim","25")
birinciSinif.bilgileriGoster()
ikinciSinif = okul("11/B","Muhammed","Algoritma","30")
a = mudur("12","Veli","Tarih","34","Mudur")
ikinciSinif.bilgileriGoster()
ikinciSinif.bransDegistir()
ikinciSinif.bilgileriGoster()
a.bilgileriGoster()

