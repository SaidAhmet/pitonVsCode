# burada subprocess modulünü çağırıp kullanırken sp olarak kullanıcaz
import subprocess as sp
#çağırdığımız modül ile aşağıdaki call komutunu kullanarak 
# istediğimiz dosyayı açtırabiliyoruz 
# bilgisayarımızda bulunan kodların tam yolunu bulmak için
# dosya gezgininde system32 dosyası içinde bulabiliriz
#yolu kopyaladığınızda "C:\Windows\System32\notepad.exe" bu şekilde oluyor
#arada ki \ bunları / bununla değiştirin çünkü ilki kaçış ifadesi
# hata veriyor

sifre = 12345

kullaniciSifre = int(input("Şifrenizi giriniz : "))

if kullaniciSifre == sifre :
    print("Şifre Doğru")
    while True:
        sp.call("C:/Windows/System32/notepad.exe")
        break
else:
    print("Hatalı Şifre")