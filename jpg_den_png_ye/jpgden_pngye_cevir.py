from PIL import Image
import os
import time
#os kullanımı
#Mesela o anda içinde bulunduğumuz dizindeki dosya ve klasörleri listelemek istersek bu fonksiyonu şöyle
# kullanabiliriz:
#
#mevcut_dizin = os.getcwd()
#os.listdir(mevcut_dizin)
#Eğer farklı bir dizinin içeriğini listelemek istersek, parametre olarak o dizinin adını yazmamız yeterli olacaktır:
#
#os.listdir('/var/www')

liste= []
sayac=0
dizin=""
resim_dosya='dosya_yolu_yazilmali/jpg_den_png_ye/jpg'
if os.listdir(resim_dosya)==[]:
        print("dosyada resim yok")
else:
    for resimler in os.listdir(resim_dosya):

        dizin=f"dosya_yolu_yazilmali//jpg_den_png_ye/jpg/{resimler}"
        resim=Image.open(dizin)
        png_dizin=f"dosya_yolu_yazilmali//jpg_den_png_ye/png/resim_{sayac+1}.png"
        resim.save(png_dizin)
        sayac+=1
    
    print(f"{sayac} tane resim başarılı bir şekilde çevrildi")
time.sleep(1)
print("kapanıyor")
time.sleep(0.2)

