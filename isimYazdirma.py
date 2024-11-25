import time as tm

isim = input("Lütfen İsminizi Giriniz : ")
i=0
while i < len(isim):
    print(isim[i],"* ",end="",flush=True)
    tm.sleep(1)
    i+=1