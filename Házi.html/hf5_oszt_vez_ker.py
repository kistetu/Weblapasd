# Számok beolvasása és eltárolása egy listában
szamok = []
while True:
    szam = input("Adjon meg egy számot (vagy 'q' a kilépéshez): ")
    if szam == 'q':
        break
    szamok.append(float(szam))

# 2 tizedesjegyig kerekítés és nagyságrend meghatározása
kerekitett_szamok = [round(szam, 2) for szam in szamok]
nagysagrendek = [f"10^{len(str(int(szam))))}" for szam in szamok]

# 1. feladat: Számok kiíratása
print("1. feladat: Beolvasott számok:")
for szam in kerekitett_szamok:
    print(szam)

# 2. feladat: Legnagyobb szám
legnagyobb = max(kerekitett_szamok)
print("2. feladat: A legnagyobb szám:", legnagyobb)

# 3. feladat: Legkisebb szám
legkisebb = min(kerekitett_szamok)
print("3. feladat: A legkisebb szám:", legkisebb)

# 4. feladat: Számok összege
osszeg = sum(kerekitett_szamok)
print("4. feladat: A számok összege:", osszeg)

# 5. feladat: Számok átlaga
atlaga = sum(kerekitett_szamok) / len(kerekitett_szamok)
print("5. feladat: A számok átlaga:", atlaga)

# 6. feladat: Pozitív számok száma
pozitiv_szamok = [szam for szam in kerekitett_szamok if szam > 0]
pozitiv_szamok_szama = len(pozitiv_szamok)
print("6. feladat: A pozitív számok száma:", pozitiv_szamok_szama)

# 7. feladat: Negatív számok száma
negativ_szamok = [szam for szam in kerekitett_szamok if szam < 0]
negativ_szamok_szama = len(negativ_szamok)
print("7. feladat: A negatív számok száma:", negativ_szamok_szama)

# 8. feladat: Nagyságrendek kiíratása
print("8. feladat: Számok nagyságrendje:")
for szam, nagysagrend in zip(kerekitett_szamok, nagysagrendek):
    print(f"{szam} - {nagysagrend}")