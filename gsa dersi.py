import cmath
import math
import time
import numpy as np
def radyandan_dereceye(radyan):
    derece=float(radyan*(180/cmath.pi))
    return derece
def dereceden_radyana(derece):
    radyan=float( derece * (cmath.pi / 180))
    return radyan
def per_unit():
    a=2
    while a==2:
        sistemin_faz_sayisi=input("sistemin kaç fazlı olduğunu giriniz= ")
        trafolar_ideal_mi=input("trafo ideal mi?(ideal ise + değil ise -)=")
        trafo_sayisi=input("trafo sayisini girin: ")
        if trafolar_ideal_mi=="+":
            if sistemin_faz_sayisi=="1":
                if trafo_sayisi=="1":
                    sistemde_belirlenen_baz_guc=float(input("Tüm sistem için ortak olacak bir Sbaz değeri girin(VA)="))
                    Vgercek,Vderece=float(input("generatör geriliminin büyüklüğünü giriniz(V)=")),float(input("derecesini giriniz="))
                    Zgercek,Zgercek_derece=float(input("1.bölgenin toplam empedansı(Zg)= ")),float(input("1.bölgenin toplam empedansı derecesi(Zg)= "))
                    Vbaz1=float(input("generatör tarafının Vbaz değerini girin(V)="))
                    iletim_hatti_empedansi_buyukluk=float(input("iletim hattı empedansının büyüklüğünü girin="))
                    iletim_hatti_empedansi_derece=float(input("iletim hattı empedansının derecesini kısmını girin="))
                    Sbaz1,Sbaz2=sistemde_belirlenen_baz_guc,sistemde_belirlenen_baz_guc
                    trafo_oranı_primer=float(input("trafonun oranının primer kısmını girin= "))
                    trafo_oranı_sekonder=float(input("trafonun oranının sekonder kısmını girin="))
                elif trafo_sayisi=="2":
                    sistemde_belirlenen_baz_guc=float(input("Tüm sistem için ortak olacak bir Sbaz değeri girin(VA)="))
                    Vgercek,Vderece=float(input("generatör geriliminin büyüklüğünü giriniz(V)=")),float(input("derecesini giriniz="))
                    Zgercek,Zgercek_derece=float(input("1.bölgenin toplam empedansı(Zg)= ")),float(input("1.bölgenin toplam empedansı derecesi(Zg)= "))
                    Vbaz1=float(input("generatör tarafının Vbaz değerini girin(V)="))
                    iletim_hatti_empedansi_buyukluk=float(input("iletim hattı empedansının büyüklüğünü girin="))
                    iletim_hatti_empedansi_derece=float(input("iletim hattı empedansının derecesini kısmını girin="))
                    Sbaz1,Sbaz2,Sbaz3=sistemde_belirlenen_baz_guc,sistemde_belirlenen_baz_guc,sistemde_belirlenen_baz_guc
                    trafo_oranı_primer1=float(input("1.trafonun primer kısmını oranının  girin= "))
                    trafo_oranı_sekonder1=float(input("1.trafonun sekonder kısmını oranının girin="))
                    trafo_oranı_primer2=float(input("2.trafonun primer kısmını oranının  girin= "))
                    trafo_oranı_sekonder2=float(input("2.trafonun sekonder kısmını oranının girin="))
                    yuk_empedansi_buyukluk=float(input("3. bölgenin toplam empedansı büyüklük="))
                    yuk_empedansi_derece=float(input("3. bölgenin toplam empedansı derecesi="))
                    Vbaz2=(Vbaz1*trafo_oranı_sekonder1)/trafo_oranı_primer1
                    Vbaz3=(Vbaz2*trafo_oranı_sekonder2)/trafo_oranı_primer2 
                    Ibaz1=Sbaz1/Vbaz1
                    Ibaz2=Sbaz1/Vbaz2
                    Ibaz3=Sbaz1/Vbaz3
                    Zbaz1=Vbaz1**2/Sbaz1
                    Zbaz2=Vbaz2**2/Sbaz1
                    Zbaz3=Vbaz3**2/Sbaz1
                    print(f"1. bölgenin Vbaz1={Vbaz1} V, Ibaz1={Ibaz1} A, Zbaz1={Zbaz1} ohm\n")
                    print(f"2. bölgenin Vbaz2={Vbaz2} V, Ibaz2={Ibaz2} A, Zbaz2={Zbaz2} ohm\n")
                    print(f"3. bölgenin Vbaz3={Vbaz3} V, Ibaz3={Ibaz3} A, Zbaz3={Zbaz3} ohm\n")
                    Vpu1=Vgercek/Vbaz1
                    Vpu1_derece=Vderece
                    Zpu1=Zgercek/Zbaz1
                    Zpu1_derece=Zgercek_derece

                    Vpu1rad=(Vpu1_derece*cmath.pi)/180
                    Zpu1rad=(Zpu1_derece*cmath.pi)/180
                    
                    
                    Zpu2=iletim_hatti_empedansi_buyukluk/Zbaz2
                    Zpu2_derece=iletim_hatti_empedansi_derece
                    Zpu2rad=(Zpu2_derece*cmath.pi)/180

                    Zpu3=yuk_empedansi_buyukluk/Zbaz3
                    Zpu3_derece=yuk_empedansi_derece
                    Zpu3rad=(Zpu3_derece*cmath.pi)/180
                    
                    print("******************************CEVAPLAR*****************************************")
                    Ipu=cmath.polar((cmath.rect(Vpu1,Vpu1rad))/(cmath.rect(Zpu2,Zpu2rad)+cmath.rect(Zpu3,Zpu3rad)+cmath.rect(Zpu1,Zpu1rad)))
                    Ipu_buyukluk=Ipu[0]
                    Ipu_derece=(Ipu[1]*180)/cmath.pi
                    print(f"Ipu={Ipu_buyukluk}<{Ipu_derece}")

                    Ihat_akimi=Ipu[0]*Ibaz2
                    Ihat_akimi_derece=(Ipu[1]*180)/cmath.pi
                    print(f"Ihat_akımı={Ihat_akimi}<{Ihat_akimi_derece} A")

                    Iyuk_akimi=Ipu[0]*Ibaz3
                    Iyuk_akimi_derece=(Ipu[1]*180)/cmath.pi
                    print(f"Iyük_akımı={Iyuk_akimi}<{Iyuk_akimi_derece} A")

                    Vyuk_pu=Ipu[0]*Zpu3
                    Vyuk_pu_derece=Ipu_derece+Zpu3_derece#DERECE YANLIŞ ÇIKIYOR
                    Vyuk_gerilimi_buyukluk=Vyuk_pu*Vbaz3
                    print(f"Vyük_gerilimi={Vyuk_gerilimi_buyukluk}<{Vyuk_pu_derece} V")   
                
                elif trafo_sayisi=="3":
                    pass
                elif trafo_sayisi=="4":
                    pass
                else :
                    print("yanlış değer girdiniz.")
            elif sistemin_faz_sayisi=="3":
                pass
            else :
                    print("yanlış değer girdiniz.")
        elif trafolar_ideal_mi=="-":
            if sistemin_faz_sayisi=="1":
                if trafo_sayisi=="1":
                    pass
                elif trafo_sayisi=="2":
                    sistemde_belirlenen_baz_guc=float(input("Tüm sistem için ortak olacak bir Sbaz değeri girin(VA)="))
                    Vgercek,Vderece=float(input("generatör geriliminin büyüklüğünü giriniz(V)=")),float(input("derecesini giriniz="))
                    Zgercek,Zgercek_derece=float(input("1.bölgenin toplam empedansı(Zg)= ")),float(input("1.bölgenin toplam empedansı derecesi(Zg)= "))
                    Vbaz1=float(input("generatör tarafının Vbaz değerini girin(V)="))
                    iletim_hatti_empedansi_buyukluk=float(input("iletim hattı empedansının büyüklüğünü girin="))
                    iletim_hatti_empedansi_derece=float(input("iletim hattı empedansının derecesini kısmını girin="))
                    Sbaz1,Sbaz2,Sbaz3=sistemde_belirlenen_baz_guc,sistemde_belirlenen_baz_guc,sistemde_belirlenen_baz_guc
                    
                    trafo_etiket_pu1=float(input("1.trafonun etiket empedansı(yüzdesiz olarak) girin="))
                    trafo_etiket_pu2=float(input("2.trafonun etiket empedansı(yüzdesiz olarak) girin="))
                    trafo_oranı_primer1=float(input("1.trafonun primer kısmını oranının  girin= "))
                    trafo_oranı_sekonder1=float(input("1.trafonun sekonder kısmını oranının girin="))
                    trafo_oranı_primer2=float(input("2.trafonun primer kısmını oranının  girin= "))
                    trafo_oranı_sekonder2=float(input("2.trafonun sekonder kısmını oranının girin="))
                    
                    yuk_empedansi_buyukluk=float(input("3. bölgenin toplam empedansı büyüklük="))
                    yuk_empedansi_derece=float(input("3. bölgenin toplam empedansı derecesi="))


                    Vbaz2=(Vbaz1*trafo_oranı_sekonder1)/trafo_oranı_primer1
                    Vbaz3=(Vbaz2*trafo_oranı_sekonder2)/trafo_oranı_primer2
                    Ibaz1=Sbaz1/Vbaz1
                    Ibaz2=Sbaz1/Vbaz2
                    Ibaz3=Sbaz1/Vbaz3
                    Zbaz1=Vbaz1**2/Sbaz1
                    Zbaz2=Vbaz2**2/Sbaz1
                    Zbaz3=Vbaz3**2/Sbaz1
                    print(f"1. bölgenin Vbaz1={Vbaz1} V, Ibaz1={Ibaz1} A, Zbaz1={Zbaz1} ohm\n")
                    print(f"2. bölgenin Vbaz2={Vbaz2} V, Ibaz2={Ibaz2} A, Zbaz2={Zbaz2} ohm\n")
                    print(f"3. bölgenin Vbaz3={Vbaz3} V, Ibaz3={Ibaz3} A, Zbaz3={Zbaz3} ohm\n")
                    
                    Vpu1=Vgercek/Vbaz1
                    Vpu1_derece=Vderece
                    Zpu1=Zgercek/Zbaz1
                    Zpu1_derece=Zgercek_derece

                    Vpu1rad=(Vpu1_derece*cmath.pi)/180
                    Zpu1rad=(Zpu1_derece*cmath.pi)/180
                    
                    
                    Zpu2=iletim_hatti_empedansi_buyukluk/Zbaz2
                    Zpu2_derece=iletim_hatti_empedansi_derece
                    Zpu2rad=(Zpu2_derece*cmath.pi)/180

                    Zpu3=yuk_empedansi_buyukluk/Zbaz3
                    Zpu3_derece=yuk_empedansi_derece
                    Zpu3rad=(Zpu3_derece*cmath.pi)/180
                    
                    print("******************************CEVAPLAR*****************************************")
                    Ipu=cmath.polar((cmath.rect(Vpu1,Vpu1rad))/(cmath.rect(Zpu2,Zpu2rad)+cmath.rect(Zpu3,Zpu3rad)+cmath.rect(Zpu1,Zpu1rad)))
                    Ipu_buyukluk=Ipu[0]
                    Ipu_derece=(Ipu[1]*180)/cmath.pi
                    print(f"Ipu={Ipu_buyukluk}<{Ipu_derece}\n")

                    Ihat_akimi=Ipu[0]*Ibaz2
                    Ihat_akimi_derece=(Ipu[1]*180)/cmath.pi
                    print(f"Ihat_akımı={Ihat_akimi}<{Ihat_akimi_derece} A\n")

                    Iyuk_akimi=Ipu[0]*Ibaz3
                    Iyuk_akimi_derece=(Ipu[1]*180)/cmath.pi
                    print(f"Iyük_akımı={Iyuk_akimi}<{Iyuk_akimi_derece} A\n")

                    Vyuk_pu=Ipu[0]*Zpu3
                    Vyuk_pu_derece=Ipu_derece+Zpu3_derece
                    Vyuk_gerilimi_buyukluk=Vyuk_pu*Vbaz3
                    print(f"Vyük_gerilimi={Vyuk_gerilimi_buyukluk}<{Vyuk_pu_derece} V\n")   
                    
                elif trafo_sayisi=="3":
                    pass
                elif trafo_sayisi=="4":
                    pass
                else :
                    print("yanlış değer girdiniz.")
            elif sistemin_faz_sayisi=="3":
                a=0
                while a==0:
                    
                    generator_etiket=input("generatör etiket değeri var mı?(evet ise + hayır ise -)")
                    if generator_etiket=="+":
                        etiket_guc=float(input("generatörün etiketinde yazan güç değeri girin (VA): "))
                        
                        etiket_pu=float(input("generatörün etiketinde yazan pu değerini yüzdesiz olarak girin: "))

                    
                    sistemde_belirlenen_baz_guc=float(input("Tüm sistem için ortak olacak bir Sbaz değeri girin(VA)="))
                    Vgercek,Vderece=float(input("generatör geriliminin büyüklüğünü giriniz(V)=")),float(input("derecesini giriniz="))
                    Zgercek,Zgercek_derece=float(input("1.bölgenin toplam empedansı(Zg)= ")),float(input("1.bölgenin toplam empedansı derecesi(Zg)= "))
                    Vbaz1=float(input("generatör tarafının Vbaz değerini girin(V)="))
                    iletim_hatti_empedansi_buyukluk=float(input("iletim hattı empedansının büyüklüğünü girin="))
                    iletim_hatti_empedansi_derece=float(input("iletim hattı empedansının derecesini kısmını girin="))
                    Sbaz1,Sbaz2,Sbaz3=sistemde_belirlenen_baz_guc,sistemde_belirlenen_baz_guc,sistemde_belirlenen_baz_guc
                    
                    trafo_etiket_pu1=float(input("1.trafonun etiket empedansı(yüzdesiz olarak) girin="))
                    trafo_etiket_pu2=float(input("2.trafonun etiket empedansı(yüzdesiz olarak) girin="))
                    trafo_etiket_guc1=float(input("1.trafonun etiket gücünü girin="))
                    trafo_etiket_guc2=float(input("2.trafonun etiket gücünü girin="))
                    trafo_etiket_primer_gerilimi1=float(input("1.trafonun etiket primer gerilini girin="))
                    trafo_etiket_primer_gerilimi2=float(input("2.trafonun etiket primer gerilimini girin="))
                    trafo_oranı_primer1=float(input("1.trafonun primer kısmını oranının  girin= "))
                    trafo_oranı_sekonder1=float(input("1.trafonun sekonder kısmını oranının girin="))
                    trafo_oranı_primer2=float(input("2.trafonun primer kısmını oranının  girin= "))
                    trafo_oranı_sekonder2=float(input("2.trafonun sekonder kısmını oranının girin="))
                    yuk_empedansi_buyukluk=float(input("3. bölgenin toplam empedansı büyüklük="))
                    yuk_empedansi_derece=float(input("3. bölgenin toplam empedansı derecesi="))

                    
                    Vbaz2=(Vbaz1*trafo_oranı_sekonder1)/trafo_oranı_primer1
                    Vbaz3=(Vbaz2*trafo_oranı_sekonder2)/trafo_oranı_primer2
                        
                    Zt1_pu=trafo_etiket_pu1*(Sbaz1/trafo_etiket_guc1)*((trafo_etiket_primer_gerilimi1**2)/(Vbaz1**2))
                    Zt2_pu=trafo_etiket_pu2*(Sbaz2/trafo_etiket_guc2)*((trafo_etiket_primer_gerilimi2**2)/(Vbaz2**2))
                    if generator_etiket=="+":
                        Zg_pu=etiket_pu*(Sbaz1/etiket_guc)*((Vgercek/Vbaz1)**2)
                        
                    Zt1_pu_karmasik=complex(0,Zt1_pu)
                    Zt1_pu_polar=cmath.polar(Zt1_pu_karmasik)
                    Zt1_pu_buyukluk=Zt1_pu_polar[0]
                    Zt1_pu_derece=radyandan_dereceye(Zt1_pu_polar[1])
                        
                    Zt2_pu_karmasik=complex(0,Zt2_pu)
                    Zt2_pu_polar=cmath.polar(Zt2_pu_karmasik)
                    Zt2_pu_buyukluk=Zt2_pu_polar[0]
                    Zt2_pu_derece=radyandan_dereceye(Zt2_pu_polar[1])

                    Ibaz1=Sbaz1/(math.sqrt(3)*Vbaz1)
                    Ibaz2=Sbaz1/(math.sqrt(3)*Vbaz2)
                    Ibaz3=Sbaz1/(math.sqrt(3)*Vbaz3)
                        
                    Zbaz1=Vbaz1**2/Sbaz1
                    Zbaz2=Vbaz2**2/Sbaz1
                    Zbaz3=Vbaz3**2/Sbaz1
                    print("******************************CEVAPLAR*****************************************")
                    print(f"1. bölgenin Vbaz1={Vbaz1} V, Ibaz1={Ibaz1} A, Zbaz1={Zbaz1} ohm")
                    print(f"2. bölgenin Vbaz2={Vbaz2} V, Ibaz2={Ibaz2} A, Zbaz2={Zbaz2} ohm")
                    print(f"3. bölgenin Vbaz3={Vbaz3} V, Ibaz3={Ibaz3} A, Zbaz3={Zbaz3} ohm\n")

                    print(f"1.trafonun yeni Zpu değeri= j{Zt1_pu} pu")
                    print(f"2.trafonun yeni Zpu değeri= j{Zt2_pu} pu")
                    if generator_etiket=="+":
                        print(f"Generatör yeni Zg_pu değeri= j{Zg_pu}\n")

                    

                    Vpu1=Vgercek/Vbaz1
                    Vpu1_derece=Vderece
                    Zpu1=Zgercek/Zbaz1
                    Zpu1_derece=Zgercek_derece
                    print(f"Vg_pu değeri= {Vpu1}<{Vpu1_derece}")

                    Vpu1rad=(Vpu1_derece*cmath.pi)/180
                    Zpu1rad=(Zpu1_derece*cmath.pi)/180
                        
                        
                    Zpu2=iletim_hatti_empedansi_buyukluk/Zbaz2
                    Zpu2_derece=iletim_hatti_empedansi_derece
                    Zpu2rad=(Zpu2_derece*cmath.pi)/180
                    print(f"Zhat_pu değeri= {Zpu2}<{Zpu2_derece}")

                    Zpu3=yuk_empedansi_buyukluk/Zbaz3
                    Zpu3_derece=yuk_empedansi_derece
                    Zpu3rad=(Zpu3_derece*cmath.pi)/180
                    print(f"Zyük_pu değeri= {Zpu3}<{Zpu3_derece}\n")
                    
                    if generator_etiket=="-":
                        Ipu=cmath.polar((cmath.rect(Vpu1,Vpu1rad))/(cmath.rect(Zpu2,Zpu2rad)+cmath.rect(Zpu3,Zpu3rad)+cmath.rect(Zpu1,Zpu1rad)+complex(0,Zt2_pu)+complex(0,Zt1_pu)))
                    if generator_etiket=="+":
                        Ipu=cmath.polar((cmath.rect(Vpu1,Vpu1rad))/(cmath.rect(Zpu2,Zpu2rad)+cmath.rect(Zpu3,Zpu3rad)+cmath.rect(Zpu1,Zpu1rad)+complex(0,Zt2_pu)+complex(0,Zt1_pu)+complex(0,Zg_pu)))
                    Ipu_buyukluk=Ipu[0]
                    Ipu_derece=(Ipu[1]*180)/cmath.pi
                    print(f"Ipu={Ipu_buyukluk}<{Ipu_derece}\n")

                    Ihat_akimi=Ipu[0]*Ibaz2
                    Ihat_akimi_derece=(Ipu[1]*180)/cmath.pi
                    print(f"Ihat_akımı={Ihat_akimi}<{Ihat_akimi_derece} A\n")

                    Iyuk_akimi=Ipu[0]*Ibaz3
                    Iyuk_akimi_derece=(Ipu[1]*180)/cmath.pi
                    print(f"Iyük_akımı={Iyuk_akimi}<{Iyuk_akimi_derece} A\n")

                    
                    Vyuk_gerilimi_buyukluk=Iyuk_akimi*yuk_empedansi_buyukluk
                    Vyuk_gerilimi_derecesi=Iyuk_akimi_derece+yuk_empedansi_derece
                    print(f"Vyük_gerilimi={Vyuk_gerilimi_buyukluk}<{Vyuk_gerilimi_derecesi} V\n")  
                    sorutekrar=input("tekrar aynı 3 fazlı sistemi hesaplamak istiyor musunuz?(evet ise e hayır ise herhangi bir tuş)=")
                    if sorutekrar=="e":
                        a=0
                    else:
                        a=2
                        print("per unit hesaplama bölümüne aktarılıyorsunuz.")

            else :
                    print("yanlış değer girdiniz.")
        else:
            print("yanlış karakter girdiniz!")
        tekrar=input("tekrar per unit hesaplamak istiyor musunuz?(evet ise e hayır ise herhangi bir tuş)=")
        if tekrar=="e":
            a=2
        else:
            a=3
            print("çıkılıyor...")    





def simetrik_olmayan_sistemler():
    b=0
    while b==0:
        a=-0.500001+0.866025403j
        a_kare=-0.500001-0.866025403j
        secim=input("\n1)pozitif, negatif ve sıfır bileşenleri girerek dengesiz sistemi bulmak\n2)simetrik olmayan sistemlerin pozitif, negatif ve sıfır bileşenlerini bulma\nHangi işlemi yaptırmak istiyorsanız numarasını yazın= ")
        if secim=="1":#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            c=0
            while c==0:#----------------------------------------------------------------------------
                Va_0_buyukluk,Va_0_derece=float(input("sıfır bileşenin büyüklüğünü giriniz= ")),float(input("sıfır bileşenin derecesini giriniz= "))
                Va_0_kartezyen=cmath.rect(Va_0_buyukluk,dereceden_radyana(Va_0_derece))
                
                
                Va_1_buyukluk,Va_1_derece=float(input("pozitif bileşenin büyüklüğünü giriniz= ")),float(input("pozitif bileşenin derecesini giriniz= "))
                Va_1_kartezyen=cmath.rect(Va_1_buyukluk,dereceden_radyana(Va_1_derece))

                Va_2_buyukluk,Va_2_derece=float(input("negatif bileşenin büyüklüğünü giriniz= ")),float(input("negatif bileşenin derecesini giriniz= "))
                Va_2_kartezyen=cmath.rect(Va_2_buyukluk,dereceden_radyana(Va_2_derece))

                

                Va=1*(Va_0_kartezyen)+1*(Va_1_kartezyen)+1*(Va_2_kartezyen)
                Vb=1*(Va_0_kartezyen)+a_kare*(Va_1_kartezyen)+a*(Va_2_kartezyen)
                Vc=1*(Va_0_kartezyen)+a*(Va_1_kartezyen)+a_kare*(Va_2_kartezyen)

                Va_polar=cmath.polar(Va)
                Vb_polar=cmath.polar(Vb)
                Vc_polar=cmath.polar(Vc)
                print("******************************************CEVAPLAR*********************************************************")
                print(f"dengesiz sistemin Va fazının büyüklüğü= {Va_polar[0]} Derecesi= {radyandan_dereceye(Va_polar[1])} V")
                print(f"dengesiz sistemin Vb fazının büyüklüğü= {Vb_polar[0]} Derecesi= {radyandan_dereceye(Vb_polar[1])} V")
                print(f"dengesiz sistemin Vc fazının büyüklüğü= {Vc_polar[0]} Derecesi= {radyandan_dereceye(Vc_polar[1])} V")

                bolumtekrr=input("\nsimetrik olmayan sistemlerin pozitif, negatif ve sıfır bileşenlerini bulma işlemini tekrarlamak için e ye basın ana menuye geçmek için herhangi bir tuşa basın.")
                if bolumtekrr=="e":
                    c=0
                    
                else:
                    c=2
                    print("simetrik olmayan sistemler menüsüne aktarılıyorsunuz...")
                    time.sleep(0.2)
        elif secim=="2":#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            c=0
            while c==0:#--------------------------------------------------------------------------------
                Va_buyukluk,Va_derece=float(input("Dengesiz sistemin Va nın büyüklüğünü giriniz= ")),float(input("Dengesiz sistemin Va nın derecesini giriniz=  "))
                Va_kartezyen=cmath.rect(Va_buyukluk,dereceden_radyana(Va_derece))

                Vb_buyukluk,Vb_derece=float(input("Dengesiz sistemin Vb nın büyüklüğünü giriniz= ")),float(input("Dengesiz sistemin Vb nın derecesini giriniz= "))
                Vb_kartezyen=cmath.rect(Vb_buyukluk,dereceden_radyana(Vb_derece))

                Vc_buyukluk,Vc_derece=float(input("Dengesiz sistemin Vc nın büyüklüğünü giriniz= ")),float(input("Dengesiz sistemin Vc nın derecesini giriniz= "))
                Vc_kartezyen=cmath.rect(Vc_buyukluk,dereceden_radyana(Vc_derece))

                Va_0=(1/3)*(1*(Va_kartezyen)+1*(Vb_kartezyen)+1*(Vc_kartezyen))
                Va_2=(1/3)*(1*(Va_kartezyen)+a_kare*(Vb_kartezyen)+a*(Vc_kartezyen))
                Va_1=(1/3)*(1*(Va_kartezyen)+a*(Vb_kartezyen)+a_kare*(Vc_kartezyen))

                Va_0_polar=cmath.polar(Va_0)
                Va_1_polar=cmath.polar(Va_1)
                Va_2_polar=cmath.polar(Va_2)
                print("******************************************CEVAPLAR*********************************************************")
                print(f"dengesiz sistemin sıfır(Va0) bileşenin büyüklüğü= {Va_0_polar[0]} Derecesi= {radyandan_dereceye(Va_0_polar[1])} V")
                print(f"dengesiz sistemin pozitif (Va1) bileşenin büyüklüğü= {Va_1_polar[0]} Derecesi= {radyandan_dereceye(Va_1_polar[1])} V")
                print(f"dengesiz sistemin negatif (Va2) bileşenin büyüklüğü= {Va_2_polar[0]} Derecesi= {radyandan_dereceye(Va_2_polar[1])} V\n")
                print(f"dengesiz sistemin sıfır(Va0) bileşenin büyüklüğü= {Va_0_polar[0]} Derecesi= {radyandan_dereceye(Va_0_polar[1])} V")
                print(f"dengesiz sistemin sıfır(Vb0) bileşenin büyüklüğü= {Va_0_polar[0]} Derecesi= {radyandan_dereceye(Va_0_polar[1])} V")
                print(f"dengesiz sistemin sıfır(Vc0) bileşenin büyüklüğü= {Va_0_polar[0]} Derecesi= {radyandan_dereceye(Va_0_polar[1])} V\n")

                Vb1=cmath.polar(a_kare*Va_1)
                Vc1=cmath.polar(a*Va_1)
                print(f"dengesiz sistemin pozitif (Va1) bileşenin büyüklüğü= {Va_1_polar[0]} Derecesi= {radyandan_dereceye(Va_1_polar[1])} V")
                print(f"dengesiz sistemin pozitif (Vb1) bileşenin büyüklüğü= {Vb1[0]} Derecesi= {radyandan_dereceye(Vb1[1])} V")
                print(f"dengesiz sistemin pozitif (Vc1) bileşenin büyüklüğü= {Vc1[0]} Derecesi= {radyandan_dereceye(Vc1[1])} V\n")

                Vb2=cmath.polar(a*Va_2)
                Vc2=cmath.polar(a_kare*Va_2)
                print(f"dengesiz sistemin negatif (Va2) bileşenin büyüklüğü= {Va_2_polar[0]} Derecesi= {radyandan_dereceye(Va_2_polar[1])} V")
                print(f"dengesiz sistemin negatif (Vb2) bileşenin büyüklüğü= {Vb2[0]} Derecesi= {radyandan_dereceye(Vb2[1])} V")
                print(f"dengesiz sistemin negatif (Vc2) bileşenin büyüklüğü= {Vc2[0]} Derecesi= {radyandan_dereceye(Vc2[1])} V\n")




                bolumtekrr=input("\nsimetrik olmayan sistemlerin pozitif, negatif ve sıfır bileşenlerini bulma işlemini tekrarlamak için e ye basın ana menuye geçmek için herhangi bir tuşa basın.")
                if bolumtekrr=="e":
                    c=0
                    
                else:
                    c=2
                    print("simetrik olmayan sistemler menüsüne aktarılıyorsunuz...")
                    time.sleep(0.2)
        else:
            print ("yanlis karakter girdiniz!")
        tekrr=input("tekrar bu menüde hesaplama yapmak istiyorsanız e ye basın çıkış için herhangi bir tuşa basın=")
        if tekrr=="e":
            b=0
        else:
            b=2
            print("çıkılıyor...")
#print(per_unit())
#print(simetrik_olmayan_sistemler())

def Ana_menu():
    d=0
    while d==0:
        print("\nKolsuzların(A,S,E) yaptığı programa HOŞGELDİNİZ...")
        secilen=input("1)Per-Unit Sistemler\n2)Simetrik Olmayan Sistemler\nHangi konuda hesaplama yapmak istiyorsanız onun başındaki numarayı girin= ")
        if secilen=="1":
            print(per_unit())
        elif secilen=="2":
            print(simetrik_olmayan_sistemler())
        else:
            print("yanlış karakter girdiniz!")
        anatekrar=input("tekrar konularda hesaplama yapmak için e ye basın, çıkış yapmak için herhangi bir tuşa basın=")
        if anatekrar=="e":
            d=0
        else:
            d=2
            print("program kapatılıyor...")
            time.sleep(0.2)
        
Ana_menu()
