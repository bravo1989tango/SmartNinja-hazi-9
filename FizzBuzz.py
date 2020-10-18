
szam = int(input("Kérek egy számot 1 és 100 között: "))

for i in range(szam):
    if (i+1) % 5 == 0 and (i+1) % 3 == 0:
        print("fizzbuzz")
    elif (i+1) % 3 == 0:
        print("fizz")
    elif (i+1) % 5 == 0:
        print("buzz")
    else:
        print(i + 1)
