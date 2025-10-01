# 1. Binnen bebouwde kom: 50 km/u (tenzij anders aangegeven).
# 2. Buiten bebouwde kom: 70 km/u (Vlaanderen)
# 3. Autosnelweg: 120 km/u.

# Flitsers houden een kleine marge: meestal 6 km/u bij snelheden ≤100 km/u 
# of 6% bij snelheden >100 km/u.
# Rijd je 57 km/u in een zone 50 → effectief 51 km/u na aftrek → boete.
# Rijd je 136 km/u op de snelweg → na aftrek 128 km/u → boete.

# Boetes (indicatief 2025)
# Lichte overtreding (tot 10–20 km/u te snel): 
# onmiddellijke inning via overschrijving, bv. €53 tot €174.
# Zwaardere overtreding (meer dan 20 km/u te snel): 
# hogere boetes, vaak vanaf €174 en oplopend tot meer dan €400.
# Meer dan 40 km/u te snel: 
# dagvaarding voor de politierechtbank → zware geldboete, rijverbod mogelijk.

# O: welke zone? 
# I: 1 
# O: welke snelheid? 
# I: 120 
# O: dagvaarding voor de politierechtban

# data dat ik nodig heb
zones = [50, 70, 120]
zone = int(input("welke zone"))
geflitste_snelheid = int(input("welke snelheid"))

# berekening van maximum snelheid
maximum_snelheid = 0
snelheid_zone= zones[zone - 1] # 50
if (snelheid_zone <= 100):
    maximum_snelheid = snelheid_zone + 6
else:
    maximum_snelheid = snelheid_zone * 1.06

# checken of ik boete heb of niet 
if (geflitste_snelheid > maximum_snelheid):
    hoeveel_te_snel = geflitste_snelheid - snelheid_zone

    if hoeveel_te_snel <= 20:
        print("lichte overtreding")
    elif hoeveel_te_snel < 40:
        print("zware overtreding")
    else:
        print("dagvaarding")
else:
    print("geen boete")
