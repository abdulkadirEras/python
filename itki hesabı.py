
def secim():
    
    sec=input("1) İHA'nın itki hesabı yapmak\n2) İHA'nın ne kadar havada kalacağını öğrenmek\nseçiminiz=")
    if sec=="1":
        itki_hesabi()
    elif sec=="2":
        ihanin_ucus_suresi()
    else:
        print("yanlış seçim ")
        
    
def itki_hesabi():
    arac_agirligi=float(input("araç ağırlığını kg cinsinden giri= "))
    motorun_kv_degeri=float(input("Sabit Kanat İHA'nın KV değerini girin= "))
    pil=float(input("pilin kaç s olduğunu girin= "))
    pil_gerilimi=pil*4.2
    pil_yarisi=pil_gerilimi/2
    pervane_capi=float(input("pervanenin boyu inch cinsinden= "))
    pervane_burgu=float(input("burgu ölçüsü inch cinsinden= "))
    yari_devir=motorun_kv_degeri*pil_yarisi
    pervane_capi_m=pervane_capi*0.0254
    cT=float(input("pervane itki sabitini(CT) girin= "))
    n_tam_devir=(motorun_kv_degeri*pil_gerilimi)/60#RPS birimi
    n_yari_devir=(motorun_kv_degeri*pil_yarisi)/60
    ro=float(input("havanın yoğunluğunu girin(deniz seviyesinde 1,225Kg/m3)= "))
    #tam devir
    T_kuvvet_elde_edilen=cT*ro*(n_tam_devir**2)*(pervane_capi_m**4)
    T_gerekli=(arac_agirligi*9.81)
    #Yarı devir
    T_kuvvet_elde_edilen_yari=cT*ro*(n_yari_devir**2)*(pervane_capi_m**4)
    #motor devir
    maks_devir=motorun_kv_degeri*pil_gerilimi
    print("******************************HESAP SONUÇLARI*****************************")
    print(f"Sabit kanat İHA'yı kaldırmak için gerekli olan kuvvet={T_gerekli} N")
    print(f"Sabit kanat İHA'yı seçtiğiniz elemanlarla tam gaz verdiğinde oluşacak kuvvet={T_kuvvet_elde_edilen} N")
    print(f"Sabit kanat İHA'yı seçtiğiniz elemanlarla yarım gaz verdiğinde oluşacak kuvvet={T_kuvvet_elde_edilen_yari} N")
    print(f"motorda maksimum üretilen devir sayısı= {maks_devir} devir/dakika")

def ihanin_ucus_suresi():
    iha_cektigi_akim=float(input("İHA'nın ortalama çektiği akımı girin= "))
    pilin_akimi=float(input("pilin üzerinde yazan mAh değerini girin= "))
    pilin_c_degeri=float(input("pilin üzerinde yazan C değerini girin= "))
    sure=((pilin_akimi/1000)*60)/20#dakika olarak
    anlik_akim=(pilin_akimi/1000)*pilin_c_degeri
    print("******************************HESAP SONUÇLARI*****************************")
    print(f"\nuçuşta kalma süresi (pilin sağlığı için 2 dakika azaltıldı)= {sure-2} dakika")
    print(f"anlık olarak çekebileceğiniz max akım(pk akım)= {anlik_akim} A")

print(secim())