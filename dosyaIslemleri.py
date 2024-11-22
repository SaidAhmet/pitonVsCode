# open komutu ile ilk parametreye dosya ismini yazıyoruz eğer ki 
# böyle bir adda dosya yok ise dosyayı oluşturur
# ikinci parametre w = write demek
# dosya = open("deneme.txt","w")
# write komutu ile içine istediğimiz metni yazıyoruz
# write komutu dosyanın içini silip tekrardan yazar üstüne güncelleme yapmaz
# dosya.write("Merhaba Ahmet")
# a = append var olan dosyanın üstüne ekleme yapıyor
# dosya = open("deneme.txt","a")

# dosya.write("Burada dosyanın üstüne yazıyor yani var olan dosyayı silmiyor")
# r = read dosyayı okumak için
# dosya = open("deneme.txt","r")
# eğer dosya.read() ifadesini bir değişkene atamazsak ekranda yazdıramayız
# a = dosya.read()
# print(a)


# bu modül karakter sorunu için kullanıyoruz
# import codecs
# encoding ile hangi karakter kodlaması olmasını seçiyoruz
# with codecs.open("deneme.txt","r",encoding="utf-8") as dosya:

    # a = dosya.read()
    # readline tek bir satır okumak için kullanılır 
    # ve önceki kodlarla koordineli çalışır birinci satir değişkeninde ilk satırı okuduğunu bilir
    # ve ikinci satır değişkeninde ikinci satırı okur
    # birinci_satir = dosya.readline()
    # ikinci_satir = dosya.readline()

    # print(birinci_satir+ikinci_satir)
# readlines komutu ile dosyadaki bütün satırları okur
# ve bir array haline getirir
    # a = dosya.readlines()
    # print(a)
    # array ı daha güzel yazdırmak için
    # for i in a:
    #     print(i)
    # a bir array olduğu için bu şekilde index kullanarak yazdırabiliriz
    # print(a[1])
# böyle dışarıda da kullanabiliyoruz
# print(a[0]) 

# with codecs.open("deneme.txt","a",encoding="utf-8") as dosya:
#     # dosyanın sonuna veri eklemek için
#     dosya.write("\nAli Veli")
# r+ ifadesi hem okuyup hem de yazmak için kullanılır
# with codecs.open("deneme.txt","r+",encoding="utf-8") as dosya:
    # dosya okumasını bir değişkene atadık
    # db = dosya.read()
    # seek komutu dosyayı byte olarak sayar içine yazılan değer ile 0'ncı bytedan itibaren dosyayı görüyor
    # dosya.seek(0)
    # db = "Bu çalıştı mı ?\n" + db
    # dosya.write(db)
    # dosya.seek(20)
    # db = "bunun başladığı yer 20'nci byte\n"+db
    # dosya.write(db)

    # db = dosya.readlines()
    # üst satırda dosyamızı arraye çevirdiğimiz için array ile yapabildiğimiz herşeyi yapabiliriz
    # db.insert(2,"Burası 3'üncü indeks\n")
    # dosya.seek(0)
    # dosya.writelines(db)



# ************************NOT DEFTERİ UYGULAMASI************************

# import codecs

# dosyaOlustur = input("Dosya Adını Giriniz : ")
# dosyaNew = dosyaOlustur + ".txt"
# veriGir = input(f"Lütfen {dosyaNew} Dosyasına Eklemek İstediğiniz Veriyi Giriniz : ")

# with codecs.open(dosyaNew,"w",encoding="utf-8") as dosya:
#     dosya.write(veriGir)
#     soruSor = input("Dosya Üzerine ekleme yapmak ister misiniz ? (E/H)").lower()
#     if soruSor == "e":
#         open(dosyaNew,"a")
#         yeniVeri = input("Lütfen Eklemek İstediğiniz Veriyi Giriniz : ")
#         yeniVeri = "\n" + yeniVeri
#         dosya.write(yeniVeri)
#         print("Verileriniz Güncellendi...")
#     else:
#         print("Çıkış Yapıldı...")

# info = codecs.open(dosyaNew,"r",encoding="utf-8")
# a = info.read()
# print(a)