import openpyxl
from openpyxl import *
def rgb_den_hsvye(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    tepe = max(r, g, b)
    cukur = min(r, g, b)
    fark = tepe-cukur
    if tepe == cukur:
        h = 0
    elif tepe == r:
        h = (60 * ((g-b)/fark) + 360) % 360
    elif tepe == g:
        h = (60 * ((b-r)/fark) + 120) % 360
    elif tepe == b:
        h = (60 * ((r-g)/fark) + 240) % 360
    if tepe == 0:
        s = 0
    else:
        s = (fark/tepe)*100
    v = tepe*100
    return h, s, v

while True:
    print("r,g,b degerlerini sırayla girin:")
    rgb_degerler=[]
    renk=["kırmızı(red)","yesil(green)","mavi(blue)"]
    for i in renk:
        deger=int(input(f"{i}->"))
        rgb_degerler.append(deger)
    h,s,v=rgb_den_hsvye(rgb_degerler[0],rgb_degerler[1],rgb_degerler[2])
    print("=====>renk özü (hue)={0}   doygunluk (saturation)={1}   parlaklık(value)={2}<=====".format(h,s,v))
    # Excel'e yazmak(Writing to an excel)  
    # Python kullanarak sayfa (sheet using Python )

  
    #Çalışma kitabı oluşturuldu (Workbook is created) 
    calisma_kitabi = Workbook() 
  
    #add_sheet, sayfa oluşturmak için kullanılır. (add_sheet is used to create sheet.) 
    sayfa_1 = calisma_kitabi.active 
    sayfa_1=calisma_kitabi.create_sheet("sayfa 1")
    
    
    sayfa_1.append(("","renk özü","doygunluk","parlaklık"))
    sayfa_1["B3"]=h
    sayfa_1["C4"]=s
    sayfa_1["D3"]=v
    
   
  
    calisma_kitabi.save('renk_degerleri.xls') 

    tekr=input("tekrar hesap yapmak için e ye basın çıkmak için herhangi bir tuşa basın.")
    if tekr=="e":
        continue
    else:
        calisma_kitabi.close()
        break
    
