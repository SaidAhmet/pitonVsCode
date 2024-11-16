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

dersKodlariVeAdlari = dict(zip(birinciYariyilDersKodu,birinciYariyilDersAdlari))


def dersleriGoster(a):
    print("***DERSLERE HOŞGELDİNİZ***")
    dersSayisi = len(birinciYariyilDersKodu)
    print(f"Bulunduğunuz Dönemde Aldığınız Ders Sayısı {dersSayisi} ve Ders Listesi Aşağıda Yer Almaktadır : ")
    for i,j in a.items():
        print("***"*20)
        print(i,":",j)

#fonksiyon çalışıyor mu onu denedim
dersleriGoster(dersKodlariVeAdlari)

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


listeUzunluk = len(birinciYariyilDersKodu)
i=0
while i<listeUzunluk:
    a = birinciYariyilDersKodu[i]
    muafMı = input(f"{a} Kodlu Dersten Muaf Mısınız ? (E/H)").lower()
    if muafMı == "e":
        dersNotOrt = int(input("Not ortalamanızı Giriniz : "))
        print(f"{a} Dersi Not Ortalamanız : {dersNotOrt}")
        ortalamalar.append(dersNotOrt)
        i+=1
    elif muafMı == "h":
        vizeNotu = int(input("Vize Notunu Giriniz : "))
        finalNotu = int(input("Final Notunu Giriniz : "))
        print(f"{a} kodlu dersinizin not ortalaması : {ortHesapla(vizeNotu,finalNotu)}")
        ortalamalar.appen(ortHesapla(vizeNotu,finalNotu))
        i+=1
    else:
        print("Hatalı Giriş Yaptınız...")

dersKoduOrtalamalar = dict(zip(birinciYariyilDersKodu,ortalamalar))

for i,j in dersKoduOrtalamalar.items():
    print(i,":",j)


# print(dersKoduOrtalamalar)

# print(ortalamalar)