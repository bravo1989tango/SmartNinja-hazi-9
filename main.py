import random

nehezseg = input("\nKérem válasszon nehézségi szintet (könnyű, közepes, nehéz): ")
eletek_szama = 0

if nehezseg == "könnyű":
    eletek_szama = 20
    szam = random.randint(1, 5)
elif nehezseg == "közepes":
    eletek_szama = 10
    szam = random.randint(1, 10)
elif nehezseg == "nehéz":
    eletek_szama = 5
    szam = random.randint(1, 20)
else:
    print("Nem értem.")

for i in range(eletek_szama):
    tipp = int(input("Kérem tippeljen: "))
    if tipp == szam:
        print("Eltaláltad! Valóban " + str(szam) + " a keresett szám!")
        break
    else:
        print("Nem sikerült! Még " + str(eletek_szama-(i+1)) + " életed maradt!")
