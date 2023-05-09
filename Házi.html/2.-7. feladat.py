# 1. sor
sor_1 = [3, 8, 2, 5, 9, 1, 7, 4, 6, 10, 12, 15, 11, 13, 14]

# 2. feladat
legkisebb_15 = sorted(sor_1)[:15]
osszeg = sum(legkisebb_15)
print("2. feladat eredménye:", osszeg)

# 2. sor
sor_2 = [20, 18, 15, 10, 5, 22, 24, 19, 17, 8, 12, 14, 21, 25, 16]

# 3. feladat
kisebb_24 = [szam for szam in sor_2 if szam < 24]
atlag = sum(kisebb_24) / len(kisebb_24)
print("3. feladat eredménye:", atlag)

# 3. sor
sor_3 = [9, 6, 12, 3, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]

# 4. feladat
harmassal_oszthato = [szam for szam in sor_3 if szam % 3 == 0]
maximum = max(harmassal_oszthato)
print("4. feladat eredménye:", maximum)

# 4. sor
sor_4 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]

# 5. feladat
negyzetek_osszege = sum([szam ** 2 for szam in sor_4[:17]])
print("5. feladat eredménye:", negyzetek_osszege)

# 5. sor
sor_5 = [25, 28, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# 6. feladat
nagyobb_24 = [szam for szam in sor_5 if szam > 24]
szorzat_nagysagrendje = 1
for szam in nagyobb_24:
    szorzat_nagysagrendje *= szam
nagysagrend = len(str(szorzat_nagysagrendje))
print("6. feladat eredménye:", nagysagrend)

# Összes szám
osszes_szam = sor_1 + sor_2 + sor_3 + sor_4 + sor_5

# 7. feladat
legnagyobb_10_minimuma = sorted(osszes_szam)[-10]
print("7. feladat eredménye:", legnagyobb_10_minimuma)
