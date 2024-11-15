#TELEFON REHBERİ ÖRNEĞİ 
#Sözlük kullanarak yapıyorum

#boş sözlük oluşturdum
telefon_rehberi = dict()
        
#rehberi görüntüleme işlemini her menü de yaptığım için bu şekilde kısaltıyorum
def rehber_goruntule():
    for i,j in telefon_rehberi.items():
        print(i," : ",j)

#rehbere ekleme yapmak için fonksiyon oluşturuyorum
def ekle_rehber ():
    print("*"*20)
    print("Kişi Eklemeye Hoşgeldiniz")
    print("*"*20)
    ad_ekle = input("Lütfen İsim Yazınız : ")
    num_ekle = input("Lütfen Telefon Numarasını Yazınız : ")
    telefon_rehberi.setdefault(ad_ekle,num_ekle)
    print("*"*20)
    print("Yeni Rehber : ")
    rehber_goruntule()

# ekle_rehber()

#rehberden kişi silmek için oluşturduğum fonksiyon
def sil_rehber ():
    print("*"*20)
    print("Kişi Silmeye Hoşgeldiniz")
    print("*"*20)
    rehber_goruntule()
    ad_sil = input("Lütfen İsim Yazınız : ")
    print(f"Silinen Kişi : {ad_sil}")
    telefon_rehberi.pop(ad_sil)
    print("*"*20)
    print("Yeni Rehber : ")
    rehber_goruntule()

#böyle bir üst menü fonksiyonu oluşturdum fakat çıkış yap çalışmıyor
#break yazsam da hata veriyor 
def ust_menu():
    print("Rehbere Hoşgeldiniz...")
    print("1-Rehberi Görüntüle\n2-Rehbere Yeni Ekle\n3-Rehberden Kayıt Sil\n4-Çıkış Yap")
    secim = input("Lütfen İşlem Yapmak İstediğiniz Menüyü Seçin : ").lower()
    if (secim == "1"):
        rehber_goruntule()
    elif (secim == "2"):
        ekle_rehber()
    elif (secim == "3"):
        sil_rehber()
    elif (secim == "4"):
        print("Çıkış Yapılıyor...")
    else:
        print("Hatalı Giriş Yaptınız...\nLütfen Tekrar Seçim Yapınız")

while True:
    ust_menu()