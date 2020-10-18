print("\nÜdvözlöm a kilóméter-mérföld konvertáló programban!")
km = 0
nemigen = ""

while True:
    try:
        km = float(input("Adja meg a konvertálni kivánt kilómétert: "))
        print("A távolság mérföldben: " + str(km * 0.621371192))
        nemigen = input("Szeretne még konvertálni? ")
        if nemigen == "igen" or "i" or "yes":
            continue
        else:
            print("Rendben, viszontlátásra!")
            break
    except ValueError:
        print("Kérem csak számokat és pontot használjon!\n")