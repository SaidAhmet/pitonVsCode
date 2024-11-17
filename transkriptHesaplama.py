#***********************TRANSKRİPT HESAPLAMA UYGULAMASI***********************

#burada dersleri tanımlıyoruz

birinciYariyilDersKodu = ["MOB101","MOB103","MOB105","MOB107","MOB113","MOB115","MOB117","MOB119","ZYD101"]
birinciYariyilDersAdlari = ["PROGRAMLAMAYA GİRİŞ VE ALGORİTMALAR","MOBİL WEB SAYFASI TASARIMI VE OPTİMİZASYONU",
                   "AĞ TEMELLERİ","VERİ TABANI TASARIMI",
                   "MESLEKİ MATEMATİK","İŞ SAĞLIĞI VE GÜVENLİĞİ","MOBİL CİHAZLAR İÇİN İŞLETİM SİSTEMLERİ",
                   "MOBİL CİHAZ DONANIMLARI","ZORUNLU YABANCI DİL II (ing.)"]

#ilk olarak ikisini beraber bir sözlük olarak tanımlamıştım ama sözlüklerde indeksleme olayı key ile olduğu için farklı şekilde erişmek ve 
#indeksleme işini çok rahat yapamadım onun yerine iki liste oluşturdum bunları birleştirip bir sözlük yapabilirim 
#ve kullanıcıdan not girişi alıp ortamala ve harf notlarını hesapladıktan sonra ekrana sadece derskodlarını ve harf notlarını rahatça yazdırabilirim

#burada seçmeli dersler eklenicek bunun da fonksiyonu ilerleyen aşamada güncellenicek
#3'üncü ve 4'üncü yarıyıl da aynı şekilde olucak
# ikinci_yariyil = {"MOB102":" ANDROİD PROGRAMLAMA","MOB124":"MİKRODENETLEYİCİLER VE MİKROİŞLEMCİLER",
#                   "MOB126":"OYUN TASARIMI VE GELİŞTİRİLMESİ","ZYD102":"ZORUNLU YABANCI DİL II (ing.)"}

#print(dersNotları)
#iki listeyi bir sözlük haline getiriyor
dersKodlariVeAdlari = dict(zip(birinciYariyilDersKodu,birinciYariyilDersAdlari))


def dersleriGoster(a):
    print("***DERSLERE HOŞGELDİNİZ***")
    dersSayisi = len(birinciYariyilDersKodu)
    print(f"Bulunduğunuz Dönemde Aldığınız Ders Sayısı {dersSayisi} ve Ders Listesi Aşağıda Yer Almaktadır : ")
    for i,j in a.items():
        print("***"*20)
        print(i,":",j)

#fonksiyon çalışıyor mu onu denedim
# dersleriGoster(dersKodlariVeAdlari)

#ekranda ders kodlarını göstermek için kullandım bunu ders notları girerken de kullanıcam
# i = 0
# while i<len(birinciYariyilDersKodu):
#     a = birinciYariyilDersKodu[i]
#     i+=1
#     print(a)

def ortHesapla(vizeNotu,finalNotu):
    ort = (vizeNotu*0.30)+(finalNotu*0.70)
    return ort

ortalamalar = list()
dersKoduOrtalamalar = dict(zip(birinciYariyilDersKodu,ortalamalar))
harfNotlari = ["AA","BA","BB","CB","CC","DD","FD","FF"]
basariKatsayilari = [4,3.5,3,2.5,2,1.5,1,0]
alinanHarfNotu = list()
alinanBasariKatSayisi = list()
dersKoduVeHarfi = dict(zip(birinciYariyilDersKodu,alinanHarfNotu))
dersKoduVeBasariKatsayisi = dict(zip(birinciYariyilDersKodu,alinanBasariKatSayisi))
ort = 0


def agnoHesapla(a):
    print(f"Aldığınız dersler ve not ortalamaları aşağıdaki gibidir : ")
    toplam = 0 # toplam değişkenini burada başlatmazsak çıktı olarak en sondaki değerin iki katını verir 
    #onun  için yukarıda başlatıyorum ki döngü her yenilendiğinde o da sıfırlanmıyor
    for i,j in a.items():
        print(i,":",j)
        toplam += j
    ort = (toplam)/(len(ortalamalar))
    return ort    
def alinanHarfNotunuGoster(a):
        print("Aldığınız Ders Kodları ve Harf Notları : ")
        for x,y in a.items():
            print(x,":",y)

def notGiris():
    listeUzunluk = len(birinciYariyilDersKodu)
    i=0
    while i<listeUzunluk:
        a = birinciYariyilDersKodu[i]
        muafMı = input(f"{a} Kodlu Dersten Muaf Mısınız ? (E/H)").lower()
        if muafMı == "e":
            global dersNotOrt
            dersNotOrt = int(input("Not ortalamanızı Giriniz : "))
            print(f"{a} Dersi Not Ortalamanız : {dersNotOrt}")
            ortalamalar.append(dersNotOrt)
            dersKoduOrtalamalar[a] = dersNotOrt  # sözlüğü güncellemek için chatgpt böyle birşey önerdi 
            harfNotuHesapla(dersNotOrt,a)
            # bunu döngünün dışında tanımlayınca out of range hatası veriyordu ben de burda denedim
            b = alinanHarfNotu[i] 
            ganoHesapla(a,b)
            i+=1
        elif muafMı == "h":
            vizeNotu = int(input("Vize Notunu Giriniz : "))
            finalNotu = int(input("Final Notunu Giriniz : "))
            print(f"{a} kodlu dersinizin not ortalaması : {ortHesapla(vizeNotu,finalNotu)}")
            ortalamalar.append(ortHesapla(vizeNotu,finalNotu))
            dersNotOrt = ort
            dersKoduOrtalamalar[a] = dersNotOrt  # sözlüğü güncellemek için chatgpt böyle birşey önerdi
            harfNotuHesapla(dersNotOrt,a)
            b = alinanHarfNotu[i] 
            ganoHesapla(a,b)
            i+=1
        else:
            print("Hatalı Giriş Yaptınız...")
    # agnoHesapla(dersKoduOrtalamalar)
    # alinanHarfNotunuGoster(dersKoduVeHarfi)
    # ganoGoster(dersKoduVeBasariKatsayisi)



#altta bulunan fonksiyonu tamamıyla chatgpt yazdı ben en aşağıda yorum satırı olarak belirticem 
#biraz daha karışık ve benim problemimi çözmeyen şeklinde yazmıştım
def harfNotuHesapla(x, dersKodu):
    if 100 >= x >= 90:
        harfNotu = harfNotlari[0]
    elif 89 >= x >= 80:
        harfNotu = harfNotlari[1]
    elif 79 >= x >= 70:
        harfNotu = harfNotlari[2]
    elif 69 >= x >= 65:
        harfNotu = harfNotlari[3]
    elif 64 >= x >= 60:
        harfNotu = harfNotlari[4]
    elif 59 >= x >= 50:
        harfNotu = harfNotlari[5]
    elif 49 >= x >= 30:
        harfNotu = harfNotlari[6]
    elif 29 >= x >= 0:
        harfNotu = harfNotlari[7]
    alinanHarfNotu.append(harfNotu)
    dersKoduVeHarfi[dersKodu] = harfNotu

def ganoHesapla(dersKodu,c):
    if c == harfNotlari[0]:
        basariKatsayisi = basariKatsayilari[0]
    elif c == harfNotlari[1]:
        basariKatsayisi = basariKatsayilari[1]
    elif c == harfNotlari[2]:
        basariKatsayisi = basariKatsayilari[2]
    elif c == harfNotlari[3]:
        basariKatsayisi = basariKatsayilari[3]
    elif c == harfNotlari[4]:
        basariKatsayisi = basariKatsayilari[4]
    elif c == harfNotlari[5]:
        basariKatsayisi = basariKatsayilari[5]
    elif c == harfNotlari[6]:
        basariKatsayisi = basariKatsayilari[6]
    elif c == harfNotlari[7]:
        basariKatsayisi = basariKatsayilari[7]
    alinanBasariKatSayisi.append(basariKatsayisi)
    dersKoduVeBasariKatsayisi[dersKodu] = basariKatsayisi


def ganoGoster(x):
    print("Aldığınız Derslerin Genel Ağırlık Not Ortalaması : ")
    toplam = 0
    for i,j in x.items():
        print(i,":",j)
        toplam += j
    ganoOrt = (toplam)/(len(alinanBasariKatSayisi))
    print(f"Ağırlıklı Genel Not Ortalamanız : {ganoOrt}")
    return ganoOrt

def devamMi():
        neIstersin = input("Not Girişi Yapmak İstiyor Musunuz ? E/H (H seçeneği sizi ana menüye döndürecektir...)").lower()
        if neIstersin == "e":
            notGiris()
        elif neIstersin == "h":
            return True
        
def agnoHesapla(a):
    print(f"Aldığınız dersler ve not ortalamaları aşağıdaki gibidir : ")
    toplam = 0 # toplam değişkenini burada başlatmazsak çıktı olarak en sondaki değerin iki katını verir 
    #onun  için yukarıda başlatıyorum ki döngü her yenilendiğinde o da sıfırlanmıyor
    for i,j in a.items():
        print(i,":",j)
        toplam += j
    ort = (toplam)/(len(ortalamalar))
    return ort   


#************PROGRAM AGNOHESAPLA VE GANOGOSTER FONKSİYONUNDA PATLIYOR*****************
#********ARKASI YARIN******


while True:
    print("***Transkript Hesaplama Uygulamasına Hoşgeldiniz***")
    menuSecim = int(input("1-Alınan Dersleri Görüntüle\n2-Not Girişi Yap\n3-Ders Ortalamalarını Gör\n4-Notların Harf Notlarını Gör\n5-Notların Başarı Katsayılarını Gör\n6-Çıkış Yap\n"))
    if menuSecim == 1:
        dersleriGoster(dersKodlariVeAdlari)
        devamMi()
    elif menuSecim == 2:
        notGiris()
    elif menuSecim == 3:
        agnoHesapla(dersKoduOrtalamalar)
    elif menuSecim == 4:
        alinanHarfNotunuGoster(dersKoduVeHarfi)
    elif menuSecim == 5:
        ganoGoster(dersKoduVeBasariKatsayisi)
    elif menuSecim == 6:
        break
    else:
        print("Hatalı Tuşlama Yaptınız...")

# notGiris()


# print(dersKoduOrtalamalar)

# print(ortalamalar)



#*****************BENİM YAZDIĞIM DÜZGÜN ÇALIŞMAYAN KOD***********************
# def harfNotuHesapla(x):
#     if(x <= 100) and (x >= 90):
#         alinanHarfNotu.append(harfNotlari[0])
#         dersKoduVeHarfi.setdefault(birinciYariyilDersKodu[0],harfNotlari[0])
#     elif(x <= 89) and (x >= 80):
#         alinanHarfNotu.append(harfNotlari[1])
#         dersKoduVeHarfi.setdefault(birinciYariyilDersKodu[1],harfNotlari[1])
        
#     elif(x <= 79) and (x >= 70):
#         alinanHarfNotu.append(harfNotlari[2])
#         dersKoduVeHarfi.setdefault(birinciYariyilDersKodu[2],harfNotlari[2])
#     elif(x <= 69) and (x >= 65):
#         alinanHarfNotu.append(harfNotlari[3])
#         dersKoduVeHarfi.setdefault(birinciYariyilDersKodu[3],harfNotlari[3])
        
#     elif(x <= 64) and (x >= 60):
#         alinanHarfNotu.append(harfNotlari[4])
#         dersKoduVeHarfi.setdefault(birinciYariyilDersKodu[4],harfNotlari[4])
        
#     elif(x <= 59) and (x >= 50):
#         alinanHarfNotu.append(harfNotlari[5])
#         dersKoduVeHarfi.setdefault(birinciYariyilDersKodu[5],harfNotlari[5])
        
#     elif(x <= 49) and (x >= 30):
#         alinanHarfNotu.append(harfNotlari[6])
#         dersKoduVeHarfi.setdefault(birinciYariyilDersKodu[6],harfNotlari[6])
        
#     elif(x <= 29) and (x >= 0):
#         alinanHarfNotu.append(harfNotlari[7])
#         dersKoduVeHarfi.setdefault(birinciYariyilDersKodu[7],harfNotlari[7])