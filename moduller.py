import random
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


liste = [1,"ahmet","said",2,5,23,43]
#choice belirtilen listeden rastgele elemanı çeker
# a = random.choice(liste)

# print(a)
#listeyi karıştırmak için kullanılan ifade
# random.shuffle(liste)

# print(liste)
#liste içinden iki tane rastgele örnek almak için
a = random.sample(liste,2)

print(a)
