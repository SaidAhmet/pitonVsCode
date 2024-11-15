# #TELEFON REHBERİ ÖRNEĞİ 

# ******************************BENİM YAPTIĞIM ÖRNEK******************************
# #Sözlük kullanarak yapıyorum

# #boş sözlük oluşturdum
# telefon_rehberi = dict()
        
# #rehberi görüntüleme işlemini her menü de yaptığım için bu şekilde kısaltıyorum
# def rehber_goruntule():
#     for i,j in telefon_rehberi.items():
#         print(i," : ",j)

# #rehbere ekleme yapmak için fonksiyon oluşturuyorum
# def ekle_rehber ():
#     print("*"*20)
#     print("Kişi Eklemeye Hoşgeldiniz")
#     print("*"*20)
#     ad_ekle = input("Lütfen İsim Yazınız : ")
#     num_ekle = input("Lütfen Telefon Numarasını Yazınız : ")
#     print(f"{ad_ekle} adlı kişi telefon rehberine ekleniyor...")
#     telefon_rehberi.setdefault(ad_ekle,num_ekle)
#     print("*"*20)
#     print("Yeni Rehber : ")
#     rehber_goruntule()

# # ekle_rehber()

# #rehberden kişi silmek için oluşturduğum fonksiyon
# def sil_rehber ():
#     print("*"*20)
#     print("Kişi Silmeye Hoşgeldiniz")
#     print("*"*20)
#     rehber_goruntule()
#     ad_sil = input("Lütfen İsim Yazınız : ")
#     print(f"Silinen Kişi : {ad_sil}")
#     telefon_rehberi.pop(ad_sil)
#     print("*"*20)
#     print("Yeni Rehber : ")
#     rehber_goruntule()

# #böyle bir üst menü fonksiyonu oluşturdum fakat çıkış yap çalışmıyor
# #break yazsam da hata veriyor 
# #chatgpt amcanın yardımıyla çözdüm
# #ust menu fonksiyonuna değer olarak dışarı gönderdim 

# def ust_menu():
#     print("Rehbere Hoşgeldiniz...")
#     print("1-Rehberi Görüntüle\n2-Rehbere Yeni Ekle\n3-Rehberden Kayıt Sil\n4-Çıkış Yap")
#     secim = input("Lütfen İşlem Yapmak İstediğiniz Menüyü Seçin : ")
#     if (secim == "1"):
#         rehber_goruntule()
#     elif (secim == "2"):
#         ekle_rehber()
#     elif (secim == "3"):
#         sil_rehber()
#     elif (secim == "4"):
#         print("Çıkış Yapılıyor...")
#         return False
#     else:
#         print("Hatalı Giriş Yaptınız...\nLütfen Tekrar Seçim Yapınız")
#     return True

# #chatgpt ile şunları ekledim
# #önce yaptığımdan ne farkı var bilmiyorum ama çalışıyor
# #usul usul devamke

# program_devam = True

# while program_devam:
#     program_devam = ust_menu()



# ******************************İZLEDİĞİM KURSUN YAPTIĞI ÖRNEK******************************

tel_rehberi =dict()

#kullanılan x parametresi telefon rehberinin yerine kullanıldı
def tel_no_ekle(x):
    print("****NUMARA EKLEME EKRANINA HOŞGELDİNİZ****")
    numara_isim_al = input("Lütfen Kayıt Edilecek Kişinin Adını Yazınız : ")
    numara_no_al = input("Lütfen Telefon Numarası Giriniz : ")

    x = tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f"{numara_isim_al} adlı kişi telefon listesine eklendi...")

def tel_rehber_goster(x):
    print("****REHBERE HOŞGELDİNİZ****")
    kisi_sayisi = len(tel_rehberi)
    print(f"Rehberinizde ki kayıtlı kişi sayısı {kisi_sayisi}")
    for i,j in x.items():
        print(i,":",j)

def no_sil(x):
    print("****KİŞİ SİLME EKRANINA HOŞGELDİNİZ****")
    silinecek_kisi = input("Silinecek Kişiyi Yazınız : ")
    x = tel_rehberi.pop(silinecek_kisi)

while True:
    print("****HOŞGELDİNİZ****")
    print("***Seçim Yapınız***")
    secim_yap = int(input("1-Ekle\n2-Sil\n3-Rehberi Göster\n"))

    if secim_yap == 1:
        tel_no_ekle(tel_rehberi)
    elif secim_yap == 2:
        no_sil(tel_rehberi)
    elif secim_yap == 3:
        tel_rehber_goster(tel_rehberi)
    else:
        print("Lütfen Uygun Tuşlara Basınız...")

#PROGRAMI BU ŞEKİLDE GELİŞTİRİLEBİLİR OLARAK BİZE BIRAKTI
#AŞAĞIDA BEN DEVAM EDİCEM BUNA YARIN VEYA ERTESİ GÜN