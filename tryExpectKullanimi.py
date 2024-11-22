import time as tm
try : 
    sayi1 = int(input("İlk sayıyı giriniz : "))
    sayi2 = int(input("İkinci sayıyı giriniz : "))
    bol = sayi1/sayi2
    print(bol)
# sayı sıfıra bölünemez hatası
# except ZeroDivisionError:
#     print("Sayı sıfıra bölünemez...")
# except ValueError:
#     print("Lütfen sayısal değer giriniz...")
except (ZeroDivisionError,ValueError):
    print("Hata var...")
#finally de yazılan kod ne olursa olsun çalışacak
finally:
    print("İşlem bitti..")
    # burada sayaç oluşturuyoruz geri sayım için
    sayac = 5
    # sınır için 5'i belirledik 0,1,2,3,4 olarak sayıcak 5 dahil değil for için
    for i in range(5):
        # burada döngüye girdiğinde her seferinde 1 sn bekliyecek
        tm.sleep(1)
        print("Geri sayım : ",sayac)
        #sayacı bir azaltıyoruz döngü her çalıştığında
        sayac-=1