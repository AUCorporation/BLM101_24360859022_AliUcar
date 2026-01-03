# Bu fonksiyonlar ile mantık kapılarını tanımladım.
def ve(A, B):
    return A & B


def veya(A, B):
    return A | B


def xor(A, B):
    return A ^ B


def değil(A):
    if (A == 1):
        return 0
    else:
        return 1

# Bilgilerim,program hakkında kısa bilgi ve yol ayrımı.
print("Ali Uçar 24360859022 BLM101 proje3")
print("Bu program 2 veya 3 değişkenli mantık kapılarını çözebilir(A x B veya A x (B x C)) \nve bunların doğruluk tablosunu çıkarabilir.")
print("1.Mantık kapısı simulatörü.\n2.Mantık kapısı doğruluk tablosu.")
path = int(input("Lütfen istediğiniz özelliğin numarasını(1/2) giriniz:"))
# Burada if,elif le iki kısmı ayırdım.Kullanıcı girdiği sayıya göre ilerleyecek.Hatalı girişte ise en son else de hata mesajı alacak.
if (path == 1):
    print("Mantık kapısı simulatörüne hoşgeldiniz!")
    degree = int(input("Lütfen mantık kapısının değişken sayısını giriniz(1,2,3):"))
    # Burada da girilen değiken sayısına göre ilerlenecek.
    if (degree == 1):
        kapı1 = input("1.not\nLütfen kullanacağınız kapının adını girin(yazıyla ve küçük harf kullanın):")
        if (kapı1 == "not"):
            A = int(input("Lütfen değilini alacağınız rakamı girin:"))
            if (A == 1 or A == 0):
                print(değil(A))
            else:
                print("Lütfen programı tekrar başlatın ve var olan rakamlardan(1/0) birini girin.")
        else:
            print("Lütfen programı tekrar başlatın ve var olan kapılardan birini girin.")
    elif (degree == 2):
        kapı1 = input("1.and \n2.or \n3.xor\nLütfen kullanacağınız kapının adını girin(yazıyla ve küçük harf kullanın):")
        A = int(input("A "+kapı1+" B için A yı girin:"))
        B = int(input("A "+kapı1+" B için B yi girin:"))
        if ((A == 1 or A == 0) and (B == 1 or B == 0)):
            if (kapı1 == "and"):
                print(ve(A, B))
            elif (kapı1 == "or"):
                print(veya(A, B))
            elif (kapı1 == "xor"):
                print(xor(A, B))
            else:
                print("Lütfen programı tekrar başlatın ve var olan kapılardan birini girin.")
        else:
            print("Lütfen programı tekrar başlatın ve var olan rakamlardan(1/0) birini girin.")
    elif (degree == 3):
        kapı1 = input("1.and \n2.or \n3.xor\nLütfen Ax(BxC) için parantez içindeki kapının adını girin(yazıyla ve küçük harf kullanın):")
        kapı2 = input("Lütfen Ax(BxC) için parantez dışındaki kapının adını girin(yazıyla ve küçük harf kullanın):")
        A = int(input("A "+kapı2+"(B "+kapı1+" C) için A yi girin:"))
        B = int(input("A "+kapı2+"(B "+kapı1+" C) için B yi girin:"))
        C = int(input("A "+kapı2+"(B "+kapı1+" C) için C yi girin:"))
        if ((C == 1 or C == 0) and (B == 1 or B == 0)):
            if (kapı1 == "and"):
                B = ve(B, C)
            elif (kapı1 == "or"):
                B = veya(B, C)
            elif (kapı1 == "xor"):
                B = xor(B, C)
            else:
                print("Lütfen programı tekrar başlatın ve var olan kapılardan birini girin.")
                #Kodun bazı yerlerinde hata mesajından sonra ayrıca python hata mesajı çıktığından karışıklığı önlemek için bazı hata mesajlarındanından sonra direkt programın sonlanması için exit koydum.
                exit()
        else:
            print("Lütfen programı tekrar başlatın ve var olan rakamlardan(1/0) birini girin.")
            exit()
        if ((A == 1 or A == 0) and (B == 1 or B == 0)):
            if (kapı2 == "and"):
                print(ve(A, B))
            elif (kapı2 == "or"):
                print(veya(A, B))
            elif (kapı2 == "xor"):
                print(xor(A, B))
            else:
                print("Lütfen programı tekrar başlatın ve var olan kapılardan birini girin.")
        else:
            print("Lütfen programı tekrar başlatın ve var olan rakamlardan(1/0) birini girin.")
    else:
        print("Derece 1,2 veya 3 girilebilir.\nLütfen tekrar deneyin.")

elif (path == 2):
    print("Mantık kapısı doğruluk tablosuna hoşgeldiniz!")
    degree = int(input("Lütfen mantık kapısının değişken sayısını giriniz(1,2,3):"))
# Burada da yine girilen değiken sayısına göre ilerlenecek.
    if (degree == 1):
        # 1. dereceden doğruluk tablosunda kullanıcıdan kapıyı alıp direkt yazdırdım.
        kapı1 = input("1.not\nLütfen kullanacağınız kapının adını girin(yazıyla ve küçük harf kullanın):")
        if (kapı1 == "not"):
            for A in range(0, 2):
                print(kapı1, A, "=", değil(A))
        else:
            print("Lütfen programı tekrar başlatın ve var olan kapılardan birini girin.")
    elif (degree == 2):
        # 2.derecedenlerin doğruluk tablosunda aynı şekilde kapıları alıp 2 iç içe for ile yazdırdım.
        kapı1 = input("1.and \n2.or \n3.xor\nLütfen kullanacağınız kapının adını girin(yazıyla ve küçük harf kullanın):")
        if (kapı1 == "and"):
            for A in range(0, 2):
                for B in range(0, 2):
                    print(A, " ", kapı1, " ", B, "=", ve(A, B))
        elif (kapı1 == "or"):
            for A in range(0, 2):
                for B in range(0, 2):
                    print(A, " ", kapı1, " ", B, "=", veya(A, B))
        elif (kapı1 == "xor"):
            for A in range(0, 2):
                for B in range(0, 2):
                    print(A, " ", kapı1, " ", B, "=", xor(A, B))
        else:
            print("Lütfen programı tekrar başlatın ve var olan kapılardan birini girin.")
            exit()
    elif (degree == 3):
        # 3. derecedenlerin tablosunu yaparken yine kapıları aldım , 3 iç içe for kurdum ve anlaşılır olsun diye iç_değer ve dış_değer tanımladım.
        kapı1 = input("1.and \n2.or \n3.xor\nLütfen Ax(BxC) için parantez içindeki kapının adını girin(yazıyla ve küçük harf kullanın):")
        kapı2 = input("Lütfen Ax(BxC) için parantez dışındaki kapının adını girin(yazıyla ve küçük harf kullanın):")
        for A in range(0, 2):
            for B in range(0, 2):
                for C in range(0, 2):
                    if (kapı1 == "and"):
                        iç_değer = ve(B, C)
                    elif (kapı1 == "or"):
                        iç_değer = veya(B, C)
                    elif (kapı1 == "xor"):
                        iç_değer = xor(B, C)
                    else:
                        print("Lütfen programı tekrar başlatın ve var olan kapılardan birini girin.")
                        exit()
                    if (kapı2 == "and"):
                        dış_değer = ve(A, iç_değer)
                    elif (kapı2 == "or"):
                        dış_değer = veya(A, iç_değer)
                    elif (kapı2 == "xor"):
                        dış_değer = xor(A, iç_değer)
                    else:
                        print("Lütfen programı tekrar başlatın ve var olan kapılardan birini girin.")
                        exit()
                    print(A, kapı2, "(", B, kapı1, C, ") =", dış_değer)
    else:
        print("Derece 1,2 veya 3 girilebilir.\nLütfen tekrar deneyin.")

else:
    print("Tanımlı olmayan numara girişi!\nLütfen programı yeniden başlatın ve tanımlı olan(1,2)bir numara girin.")
