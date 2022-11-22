durasiSewa=['6 jam', '12 jam','2 jam','10 jam','24 jam'];
jenisMobilHonda=['Honda Mobilio', 'Honda Crv','Honda Brv','Honda Hrv','Honda Jazz']
jenisMobilToyota=['Toyota Yaris','Toyota Camry','Toyota Hiace','Toyota Alphard','Toyota Innova']
tahunMobil=['2000','2021','2017']
warnaMobil=['Merah','Biru','Hitam']



def menuUtama(): 
    print("List Menu : \n 1. Menampilkan durasi, type mobil, tahun mobil & warna mobil \n 2. Menambah durasi sewa, type, tahun & warna mobil\n 3. Mengupdate durasi sewa, type,tahun & warna mobil \n 4. Menghapus durasi sewa, type,tahun dan warna mobil \n 5. Exit program")
    
def menuRead():
    print('1. Durasi sewa \n2. Mobil yang ready stock\n3. Tahun Mobil yang tersedia\n4. Warna Mobil yang tersedia\n5.Menu utama')
    pilih=int(input("Pilih menu yang dipilih[1-5]:"))
    if (pilih == 1):
        print("Durasi yang tersedia adalah {}".format(durasiSewa))
        menuRead()
    elif(pilih == 2):
        print("1. Honda, 2. Toyota")
        typeMobil=int(input('Pilih merk mobil yang dipilih [1-2]:'))
        if(typeMobil== 1):
            print("Yang anda pilih adalah {}".format(jenisMobilHonda))
            menuRead()
        elif(typeMobil==2):
            print("Yang anda pilih adalah {}".format(jenisMobilToyota))
            menuRead()
        else:
            print("Tidak ada data")
            menuRead()

    elif (pilih == 3):
        print("Tahun mobil yang tersedia adalah  {}".format(tahunMobil))
        menuRead()
    elif (pilih == 4 ):
        print("Warna mobil yang tersedia adalah  {}".format(warnaMobil))
        menuRead() 
    elif (pilih ==5):
        menuUtama()

    else :
        menuRead()
        
def menuCreate():
        print("1. Menambah durasi sewa mobil \n2. Menambah type mobil Honda\n3. Menambah type mobil Toyota\n4. Menambah tahun mobil \n5. Menambah warna mobil\n6. Menu utama")
        menu=int(input("Pilih menu yang diingikan [1-6]: "))
        if (menu ==1):
            print('Durasi yang sudah ada :{}'.format(durasiSewa))
            jenis=str(input('Tambah durasi sewa mobil yang diinginkan :'))
            if jenis not in durasiSewa:
                    pilihan=input("Apa anda akan menyimpan perubahan ?(Y/N)")
                    if (pilihan.upper ()== 'Y'):
                        durasiSewa.append(jenis)
                        print("Durasi sewa mobil terbaru adalah :{} ".format(durasiSewa))
                        print("Data tersimpan")
                        menuCreate()
                    elif (pilihan.upper()=='N'):
                        menuCreate()
            else :
                print("Data sudah ada") 
                menuCreate()
        elif (menu ==2):
            print('Type mobil Honda yang sudah ada :{}'.format(jenisMobilHonda))
            jenis=str(input('Tambah type mobil Honda yang diinginkan :'))
            if jenis not in jenisMobilHonda:
                    pilihan=input("Apa anda akan menyimpan perubahan ?(Y/N)")
                    if (pilihan.upper ()== 'Y'):
                        jenisMobilHonda.append(jenis.title())
                        print("Tipe mobil Honda terbaru adalah :{} ".format(jenisMobilHonda))
                        print("Data tersimpan")
                        menuCreate()
                    elif (pilihan.upper()=='N'):
                        menuCreate()
            else :
                print("Data sudah ada") 
                menuCreate()

        elif (menu ==3):
            print('Tipe mobil Toyota yang sudah ada :{}'.format(jenisMobilToyota))
            jenis=str(input('Tambah type mobil Toyota yang diinginkan :'))
            if jenis not in jenisMobilToyota:
                    pilihan=input("Apa anda akan menyimpan perubahan ?(Y/N)")
                    if (pilihan.upper ()== 'Y'):
                        jenisMobilToyota.append(jenis.title())
                        print("Tipe mobil Toyota terbaru adalah :{} ".format(jenisMobilToyota))
                        print("Data tersimpan")
                        menuCreate()
                    elif (pilihan.upper()=='N'):
                        menuCreate()
            else :
                print("Data sudah ada") 
                menuCreate()

        elif (menu ==4):
            print('Tahun mobil yang sudah ada :{}'.format(tahunMobil))
            jenis=str(input('Tambah tahun mobil yang diinginkan :'))
            if jenis not in tahunMobil:
                    pilihan=input("Apa anda akan menyimpan perubahan ?(Y/N)")
                    if (pilihan.upper ()== 'Y'):
                        tahunMobil.append(jenis.title())
                        print("Tahun mobil terbaru adalah :{} ".format(tahunMobil))
                        print("Data tersimpan")
                        menuCreate()
                    elif (pilihan.upper()=='N'):
                        menuCreate()
            else :
                print("Data sudah ada") 
                menuCreate()

        elif (menu ==5):
            print('Warna mobil yang sudah ada :{}'.format(warnaMobil))
            jenis=str(input('Warna mobil yang diinginkan :'))
            if jenis not in warnaMobil:
                    pilihan=input("Apa anda akan menyimpan perubahan ?(Y/N)")
                    if (pilihan.upper ()== 'Y'):
                        warnaMobil.append(jenis.title())
                        print("Tahun mobil terbaru adalah :{} ".format(warnaMobil))
                        print("Data tersimpan")
                        menuCreate()
                    elif (pilihan.upper()=='N'):
                        menuCreate()
            else :
                print("Data sudah ada") 
                menuCreate()
        elif (menu == 6):
            menuUtama()
        else:
            menuCreate()

def menuUpdate () :
        print("1. Update durasi sewa mobil \n2. Update type mobil Honda\n3. Update type mobil Toyota\n4. Update tahun mobil \n5. Update warna mobil\n6. Menu Utama")
        menu=int(input("Pilih menu yang diingikan [1-6]: "))
        if (menu ==1):
            print("Durasi yang ingin di update :{} ".format(durasiSewa))
            jenis=str(input('Pilih durasi yang ingin di update :'))
            if jenis in durasiSewa:
                    pilihan=input("Lanjut update ?(Y/N):")
                    ganti=str(input('Input durasi sewa terbaru : '))     
                    update=input("Update data(Y/N):")
                    if (update.upper() == 'Y'):    
                        if (pilihan.upper ()== 'Y'):
                            for i in range(len(durasiSewa)):
                                if(jenis == durasiSewa[i]):
                                 durasiSewa[i]=ganti
                                elif(jenis == durasiSewa[i]):
                                 durasiSewa[i]=ganti
                            print("Durasi sewa mobil terbaru adalah :{} ".format(durasiSewa))
                            print("Data terupdate")
                        elif (pilihan.upper()=='N'):
                         menuUpdate()                      
                    else :
                     menuUpdate()   
            else :
                print("Data yang anda cari tidak ada") 
                menuUpdate() 

        if (menu ==2):
            print("Jenis mobil Honda yang akan di update :{} ".format(jenisMobilHonda))
            jenis=str(input('Pilih type mobil yang ingin di update :'))
            if jenis in jenisMobilHonda:
                    pilihan=input("Lanjut update ?(Y/N):")
                    ganti=str(input('Input jenis mobil Honda terbaru : '))     
                    update=input("Update data(Y/N):")
                    if (update.upper() == 'Y'):    
                        if (pilihan.upper ()== 'Y'):
                            for i in range(len(jenisMobilHonda)):
                                if(jenis == jenisMobilHonda[i]):
                                 jenisMobilHonda[i]=ganti
                                elif(jenis == jenisMobilHonda[i]):
                                 jenisMobilHonda[i]=ganti
                            print("Jenis mobil Honda terbaru adalah :{} ".format(jenisMobilHonda))
                            print("Data terupdate")
                        elif (pilihan.upper()=='N'):
                         menuUpdate()                      
                    else :
                     menuUpdate()   
            else :
                print("Data yang anda cari tidak ada") 
                menuUpdate() 

        if (menu ==3):
            print("Jenis mobil Toyota yang akan di update :{} ".format(jenisMobilToyota))
            jenis=str(input('Pilih type mobil yang ingin di update :'))
            if jenis in jenisMobilToyota:
                    pilihan=input("Lanjut update ?(Y/N):")
                    ganti=str(input('Input jenis mobil Toyota terbaru : '))     
                    update=input("Update data(Y/N):")
                    if (update.upper() == 'Y'):    
                        if (pilihan.upper ()== 'Y'):
                            for i in range(len(jenisMobilToyota)):
                                if(jenis == jenisMobilToyota[i]):
                                 jenisMobilToyota[i]=ganti
                                elif(jenis == jenisMobilToyota[i]):
                                 jenisMobilToyota[i]=ganti
                            print("Jenis mobil Toyota terbaru adalah :{} ".format(jenisMobilToyota))
                            print("Data terupdate")
                        elif (pilihan.upper()=='N'):
                         menuUpdate()                      
                    else :
                     menuUpdate()   
            else :
                print("Data yang anda cari tidak ada") 
                menuUpdate() 

        if (menu ==4):
            print("Tahun mobil yang akan di update :{} ".format(tahunMobil))
            jenis=str(input('Pilih tahun mobil yang ingin di update :'))
            if jenis in tahunMobil:
                    pilihan=input("Lanjut update ?(Y/N):")
                    ganti=str(input('Input tahun mobil terbaru : '))     
                    update=input("Update data(Y/N):")
                    if (update.upper() == 'Y'):    
                        if (pilihan.upper ()== 'Y'):
                            for i in range(len(tahunMobil)):
                                if(jenis == tahunMobil[i]):
                                 tahunMobil[i]=ganti
                                elif(jenis == tahunMobil[i]):
                                 tahunMobil[i]=ganti
                            print("Tahun mobil terbaru adalah :{} ".format(tahunMobil))
                            print("Data terupdate")
                        elif (pilihan.upper()=='N'):
                         menuUpdate()                      
                    else :
                     menuUpdate()   
            else :
                print("Data yang anda cari tidak ada") 
                menuUpdate() 


        if (menu ==5):
            print("Warna mobil yang akan di update :{} ".format(warnaMobil))
            jenis=str(input('Pilih warna mobil yang ingin di update :'))
            if jenis in warnaMobil:
                    pilihan=input("Lanjut update ?(Y/N):")
                    ganti=str(input('Input warna mobil terbaru : '))     
                    update=input("Update data(Y/N):")
                    if (update.upper() == 'Y'):    
                        if (pilihan.upper ()== 'Y'):
                            for i in range(len(warnaMobil)):
                                if(jenis == warnaMobil[i]):
                                 warnaMobil[i]=ganti
                                elif(jenis == warnaMobil[i]):
                                 warnaMobil[i]=ganti
                            print("Warna mobil terbaru adalah :{} ".format(warnaMobil))
                            print("Data terupdate")
                        elif (pilihan.upper()=='N'):
                         menuUpdate()                      
                    else :
                     menuUpdate()   
            else :
                print("Data yang anda cari tidak ada") 
                menuUpdate() 
        elif (menu ==6):
             menuUtama()
        
        else:
            menuUpdate()

def menuDelete():
        print("1. Hapus durasi sewa mobil \n2. Hapus type mobil Honda\n3. Hapus type mobil Toyota\n4. Hapus tahun mobil \n5. Hapus warna mobil\n6. Menu Utama")
        menu=int(input("Pilih menu yang diingikan [1-6]: "))
        if (menu ==1):
            print("Durasi yang ingin di delete :{} ".format(durasiSewa))
            delete=input("Hapus data(Y/N):")
            if (delete.upper() == 'Y'):
                durasiSewa.clear()
                print("Data terupdate")
                menuDelete()
            else :
             menuDelete()

        elif (menu ==2):
            print("Type mobil yang ingin di delete :{} ".format(jenisMobilHonda))
            delete=input("Hapus data(Y/N):")
            if (delete.upper() == 'Y'):
                jenisMobilHonda.clear()
                print("Data terupdate")
                menuDelete()
            else :
             menuDelete()

        elif (menu ==3):
            print("Type mobil yang ingin di delete :{} ".format(jenisMobilToyota))
            delete=input("Hapus data(Y/N):")
            if (delete.upper() == 'Y'):
                jenisMobilToyota.clear()
                print("Data terupdate")
                menuDelete()
            else :
             menuDelete()

        elif (menu ==4):
            print("Tahun mobil yang ingin di delete :{} ".format(tahunMobil))
            delete=input("Hapus data(Y/N):")
            if (delete.upper() == 'Y'):
                tahunMobil.clear()
                print("Data terupdate")
                menuDelete()
            else :
             menuDelete()

        elif (menu ==5):
            print("Warna mobil yang ingin di delete :{} ".format(warnaMobil))
            delete=input("Hapus data(Y/N):")
            if (delete.upper() == 'Y'):
                warnaMobil.clear()
                print("Data terupdate")
                menuDelete()
            else :
             menuDelete()

        elif (menu ==6):
            menuUtama()
        else:
            menuDelete()

def menuExit():
    exit()


print ("++++++++Selamat datang di Rental Mobil Abadi Jaya++++++++")
menuUtama()

while True:
    pilih= int(input('Pilih nomor yang diinginkan [1-5]:' ))
    if pilih == 1:
        menuRead()
    elif pilih == 2:
        menuCreate()
    elif pilih == 3:
        menuUpdate()
    elif pilih == 4:
        menuDelete()
    elif pilih == 5:
        menuExit()
   
    



