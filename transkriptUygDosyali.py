# ****DAHA ÖNCE YAPTIĞIM TRANSKRRİPT UYGULAMASINI DOSYADAN VERİ ÇEKEREK YAPMAYA ÇALIŞICAM****

import codecs
#pdf dosyalarını açmak için bu modül kullanılır
import PyPDF2
import pdfplumber

dosyaAdi = input("Dosya ismini yazınız lütfen : ")
a = dosyaAdi + ".pdf"

oku = PyPDF2.PdfReader(a)

for i, page in enumerate(oku.pages):
    print(f"Sayfa {i + 1}:")
    print(page.extract_text())
    print("-" * 50)


# with pdfplumber.open(a) as pdf:
#     page = pdf.pages[0]  # İlk sayfa
#     tables = page.extract_tables()
    
#     for table in tables:
#         for row in table:
#             print(row)  



# PDFPLUMBER KULLANMAK DAHA MANTIKLI GİBİ DURUYO AMA HENÜZ İHTİYACIMI KARŞILAYACAK KADAR ŞEY ÖĞRENMEDİM
# BU KONU ÜZERİNE DAHA ÇOK VERİ ANALİZİ KONULARINDA GİRİYOLAR