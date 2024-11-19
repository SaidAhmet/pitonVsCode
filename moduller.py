# import random
# import datetime
#datetime modülünün hepsini kullanmıyacağımız için içinden sadece datetime fonksiyonunu çağırıyoruz
# from datetime import datetime
#local i import ediyoruz
# import locale
#locale ayarlıyoruz dil olarak Türkçe
#datetime modülünde çağırdığımız herşey Türk alfabesine göre Türkçe olarak çıktı alınıyor
# locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
#******************MODÜLLER******************

#Dahili ve harici modüller bulunur.

# modül aktarmak için "import modul_ismi"

#burada toplama dosyasını çağırdık
# import toplama
#toplama dosyası içinde bulunan toplam öğesini çağırdık
# toplama.toplam()

#aşağıdaki gibi de uzun dosya isimlerini as yazarak kullanacağımız dosyada kısasını oluşturup kullanabiliriz
#import uzun_dosya_ismi as kısaltılmışHali

#modul dosyasından sadece fonksiyon adlı öğeyi çağırmak için
#from modul import fonksiyon

# a = random.random()
# # "*10" ile sayıyı ondalıktan kurtardık
# #round fonksiyonu ile sayıyı yuvarladık paratez içinde virgülden sonra belirtilen kadar basamak olucak
# print(round(a*10,2))
# #unıform ile aralık belirliyoruz
# b = random.uniform(1.5,2.5)
# print(b)
# #randint ile tam sayı aralığı belirliyoruz
# c = random.randint(15,30)

# print(c)


# liste = [1,"ahmet","said",2,5,23,43]
#choice belirtilen listeden rastgele elemanı çeker
# a = random.choice(liste)

# print(a)
#listeyi karıştırmak için kullanılan ifade
# random.shuffle(liste)

# print(liste)
#liste içinden iki tane rastgele örnek almak için
# a = random.sample(liste,2)

# print(a)

#dir ile çağırılan modülün içindekileri görebiliyoruz
# print(dir(datetime))
#şimdiki zamanı yazdırmak için kullanıyoruz
#formatı YYYY-MM-DD HH-MM-SS
# a = datetime.now()
#verilen zamandan sadece yılı almak istersek
# a = a.year
#sadece günü almak için
# a = a.day 
#sadece ayı almak için
# a = a.month
#sadece saat için
# a = a.hour
#sadece dakikayı almak için
# a = a.minute
# sadece saniyeyi almak için 
# a  = a.second
# %a hafta gününün kısaltılmış adı
# %A hafta gününün tam adı
# %b ayın kısaltılmış adı
# %B ayın tam adı
# %c tam tarih, saat ve zaman bilgisi
# %d sayı değerli bir karakter dizisi olarak gün
# %j belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
# %m sayı değerli bir karakter dizisi olarak ay
# tam_tarih = datetime.strftime(a,"%a")
# print(tam_tarih)
# tam_tarih = datetime.strftime(a,"%A")
# print(tam_tarih)
# tam_tarih = datetime.strftime(a,"%b")
# print(tam_tarih)
# tam_tarih = datetime.strftime(a,"%B")
# print(tam_tarih)
# tam_tarih = datetime.strftime(a,"%c")
# print(tam_tarih)
# tam_tarih = datetime.strftime(a,"%d")
# print(tam_tarih)
# tam_tarih = datetime.strftime(a,"%j")
# print(tam_tarih)
# tam_tarih = datetime.strftime(a,"%m")
# print(tam_tarih)

# print(a)
