def hitung(angka_depan, angka_belakang, operasi):
    hasil = ""
    if operasi == "*":
        hasil = str(angka_belakang*angka_depan)
    elif operasi == "/":
        hasil = str(angka_belakang/angka_depan)
    elif operasi == "+":
        hasil = str(angka_belakang+angka_depan)
    else:
        hasil = str(angka_belakang-angka_depan)
    return hasil

def cari_angka_depan(ekspresi, i):
    angka_depan = 0
    untuk_depan = len(ekspresi)
    while untuk_depan > i:
        try:
            angka_depan = float(ekspresi[i+1:untuk_depan])
        except:
            untuk_depan -= 1
        else:
            break
    return angka_depan, untuk_depan

def cari_angka_belakang(ekspresi, i):
    angka_belakang = 0
    untuk_belakang = 0
    while untuk_belakang < i:
        try:
            angka_belakang = float(ekspresi[untuk_belakang:i])
        except:
            untuk_belakang += 1
        else:
            break
    return angka_belakang, untuk_belakang

def selesaikan_kalibagi(ekspresi, i, operasi, hasil, kalibagi):
    angka_depan, untuk_depan = cari_angka_depan(ekspresi, i)
    angka_belakang, untuk_belakang = cari_angka_belakang(ekspresi, i)
    hasil = hitung(angka_depan, angka_belakang, operasi)
    
    while kalibagi:
        try:
            if ekspresi[untuk_depan] == "*" or ekspresi[untuk_depan] == "/":
                i = untuk_depan
                angka_depan, untuk_depan = cari_angka_depan(ekspresi, i)
                hasil = hitung(angka_depan, float(hasil), ekspresi[i])
            else:
                kalibagi = False
        except IndexError:
            break
    return untuk_depan, untuk_belakang, hasil

def selesaikan_tambahkurang(ekspresi, i, operasi, hasil, tambahkurang):
    angka_depan, untuk_depan = cari_angka_depan(ekspresi, i)
    angka_belakang, untuk_belakang = cari_angka_belakang(ekspresi, i)
    hasil = hitung(angka_depan, angka_belakang, operasi)
    
    while tambahkurang:
        try:
            if ekspresi[untuk_depan] == "+" or ekspresi[untuk_depan] == "-":
                i = untuk_depan
                angka_depan, untuk_depan = cari_angka_depan(ekspresi, i)
                hasil = hitung(angka_depan, float(hasil), ekspresi[i])
            else:
                tambahkurang = False
        except IndexError:
            break
    return untuk_depan, hasil

def memproses_ekspresi():
    hurufkarakter = "qwertyuiopasdfghjklzxcvbnm@#$_&:;!?,"
    print("------------------------------")
    print("**INPUT**")
    while True:
        try:
            angka = input("Masukkan Angka: ")
            angka = float(angka)
            ekspresilist = input("Buat Beberapa Ekspresi Aritmatika: ")
            for i in ekspresilist:
                if i in hurufkarakter:
                    raise ValueError
        except:
            print("Error: Inputan Tidak Valid, Mohon Masukkan Angka, Bukan Huruf Atau Karakter")
        else:
            ekspresilist = ekspresilist.split()
            for i in range (len(ekspresilist)):
                ekspresilist[i] = ekspresilist[i].replace("(", "").replace(")", "").replace("--", "+").replace("+-", "-")
            return angka, ekspresilist
    print("------------------------------")

def main():
    ketemu = False
    hasiloutput = ""
    hasilarr = []
    hasilarreks = []
    angka, ekspresilist = memproses_ekspresi()
    
    for ekspresi in ekspresilist:
        temp = ekspresi
        operasi_kalibagi = {}
        operasi_kalibagilen = {}
        operasi_kalibagiarr = []
        hasil = ""
        kalibagi = False
        tambahkurang = False
        
        i = 0
        while i < len(ekspresi):
            if ekspresi[i] == "*" or ekspresi[i] == "/":
                kalibagi = True
                i, i_belakang, hasil = selesaikan_kalibagi(ekspresi, i, ekspresi[i], hasil, kalibagi)
                operasi_kalibagi[ekspresi[i_belakang:i]] = hasil
            else:
                i += 1
                
        for i in operasi_kalibagi.keys():
            operasi_kalibagiarr.append(len(i))
            operasi_kalibagilen[i] = len(i)
        operasi_kalibagiarr.sort(reverse=True)
        for i in range(len(operasi_kalibagiarr)):
            for j in operasi_kalibagilen:
                if operasi_kalibagilen[j] == operasi_kalibagiarr[i]:
                    operasi_kalibagiarr[i] = j
                    operasi_kalibagilen.pop(j)
                    break
        for i in operasi_kalibagiarr:
            for j in operasi_kalibagi:
                if i == j:
                    if operasi_kalibagi[j][0] != "-":
                        ekspresi = ekspresi.replace(i, "+" + operasi_kalibagi[j])
                        if ekspresi[0] == "+":
                            ekspresi = ekspresi[1:]
                        ekspresi = ekspresi.replace("*+", "*").replace("/+", "/").replace("-+", "-").replace("++", "+").replace("--", "+").replace("+-", "-")
                    else:
                        ekspresi = ekspresi.replace(i, operasi_kalibagi[j])
                    break
        
        i = 0
        while i < len(ekspresi):
            if ekspresi[i] == "+" or ekspresi[i] == "-":
                if ekspresi[i] == "-" and i == 0:
                    i += 1
                else:
                    tambahkurang = True
                    i, hasil = selesaikan_tambahkurang(ekspresi, i, ekspresi[i], hasil, tambahkurang)
            else:
                i += 1
        if float(angka) == float(hasil):
            ketemu = True
            for indeks in range(len(ekspresilist)):
                if ekspresilist[indeks] == temp:
                    hasilarr.append("Indeks " + str(indeks))
                    hasilarreks.append(temp)
    if ketemu:
        for i in hasilarr:
             if len(hasilarr) == 1:
                 hasiloutput = i
             elif len(hasilarr) == 2:
                 if i == hasilarr[len(hasilarr)-1]:
                     hasiloutput += i
                 else:
                     hasiloutput += i + " Dan "
             else:
                 if i == hasilarr[len(hasilarr)-1]:
                     hasiloutput += " Dan " + i
                 elif i == hasilarr[len(hasilarr)-2]:
                     hasiloutput += i + " "
                 else:
                     hasiloutput += i + ", "
        print("------------------------------")
        print("**OUTPUT**")
        print(hasiloutput)
        print(hasilarreks)
        print("------------------------------")
    else:
        print("------------------------------")
        print("Tidak Ketemu")
        print("------------------------------")

if __name__ == "__main__":
    program = True
    while program:
        main()
        while True:
            try:
                loop = input("Ulangi?(y/t): ")
                if loop != "y" and loop != "t":
                    raise ValueError
            except ValueError:
                print("Error: Input Tidak Valid, Pilih y/t.")
            else:
                if loop == "t":
                    print("Terima Kasih Menggunakan Program Ini")
                    program = False
                break