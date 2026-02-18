import random

# Lijsten
VijfLetterWoorden = ["appel", "fiets", "broek", "tafel"]
ZesLetterWoorden = ["school", "banaan", "alinea", "parfum"]
ZevenLetterWoorden = ["machine", "gewicht", "halfzus", "jackpot"]

MaxPogingen = 6

# Begin
print("Welkom bij Lingo!!\n")

# Spelernaam
naamspeler = input("Wat is de naam van uw speler? ").strip()
while not naamspeler:
    print("Uw spelersnaam is niet opgeslagen, probeer het opnieuw.")
    naamspeler = input("Wat is de naam van uw speler? ").strip()

print(f"Uw spelersnaam is opgeslagen: {naamspeler}\n")

# Spelregels
Spelregels = input("Wilt u de spelregels weten? (Ja/Nee) ").strip().lower()
while not (Spelregels.startswith("ja") or Spelregels.startswith("nee")):
    Spelregels = input("Typ ja of nee: ").strip().lower()

if Spelregels.startswith("ja"):
    print("\nHet doel van het spel is om een vijfletter-, zesletter- of zevenletterwoord te raden door middel van andere woorden.")
    print("U heeft 6 pogingen om dit te doen.")
    print("Als u een letter goed raadt, kleurt het hokje groen 🟩,")
    print("als de letter in het woord zit maar niet op de juiste plek dan kleurt het hokje geel 🟨,")
    print("en als de letter niet goed is blijft het hokje wit ⬜.\n")
else:
    print("Succes!\n")

# Woordlengte kiezen
LengteWoord = input("Wilt u een vijfletterwoord, zesletterwoord of zevenletterwoord proberen te raden? (5/vijf, 6/zes, 7/zeven) ").strip().lower()

# Blijft vragen tot geldige invoer
while LengteWoord not in ("5", "vijf", "vijfletterwoord",
                          "6", "zes", "zesletterwoord",
                          "7", "zeven", "zevenletterwoord"):
    LengteWoord = input("Ongeldige keuze. Kies 5/vijf, 6/zes of 7/zeven: ").strip().lower()

# Bevestiging
Confirmatie = input("Weet u dit zeker? (Ja/Nee) ").strip().lower()
while Confirmatie != "ja":
    if Confirmatie == "nee":
        LengteWoord = input("Kies opnieuw: vijfletterwoord, zesletterwoord of zevenletterwoord: ").strip().lower()
        while LengteWoord not in ("5", "vijf", "vijfletterwoord",
                                  "6", "zes", "zesletterwoord",
                                  "7", "zeven", "zevenletterwoord"):
            LengteWoord = input("Ongeldige keuze. Kies 5/vijf, 6/zes of 7/zeven: ").strip().lower()
    Confirmatie = input("Weet u dit zeker? (Ja/Nee) ").strip().lower()

print("\nOke. We gaan beginnen!\n")

# Woord kiezen
if LengteWoord in ("5", "vijf", "vijfletterwoord"):
    geheim_woord = random.choice(VijfLetterWoorden)
elif LengteWoord in ("6", "zes", "zesletterwoord"):
    geheim_woord = random.choice(ZesLetterWoorden)
else:
    geheim_woord = random.choice(ZevenLetterWoorden)

ALetter = len(geheim_woord)
print("Uw woord is gekozen.\n")

# Spel
pogingen = MaxPogingen
geraden = False

while pogingen > 0 and not geraden:
    raden = input("Probeert u eens: ").strip().lower()

    # Lengte controleren
    if len(raden) != ALetter:
        print(f"Uw woord moet {ALetter} letters hebben.\n")
        continue

    geheim_list = list(geheim_woord)
    feedback = ["⬜"] * ALetter

    for i in range(ALetter):
        if raden[i] == geheim_woord[i]:
            feedback[i] = "🟩"
            geheim_list[i] = None

    for i in range(ALetter):
        if feedback[i] == "⬜" and raden[i] in geheim_list:
            feedback[i] = "🟨"
            index = geheim_list.index(raden[i])
            geheim_list[index] = None

    print("Resultaat:", "".join(feedback), "\n")

    # Controleren of het woord geraden is
    if raden == geheim_woord:
        geraden = True
        print(f"Geweldig, {naamspeler}! U heeft het woord geraden!")
    else:
        pogingen -= 1
        print(f"U heeft nog {pogingen} pogingen over.\n")

if not geraden:
    print(f"Helaas, {naamspeler}, u heeft verloren.")
    print("Het woord was:", geheim_woord)

