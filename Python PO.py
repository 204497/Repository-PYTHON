import random

# Lijsten
VijfLetterWoorden = ["appel", "fiets", "broek", "tafel"]
ZesLetterWoorden = ["school", "banaan", "alinea", "parfum"]
ZevenLetterWoorden = ["machine", "gewicht", "halfzus", "jackpot"]

MaxPogingen = 6

# Begin
print("Welkom bij Lingo!!")
print("\n")

# Spelernaam
naamspeler = input("Wat is de naam van uw speler? ")
print("\n")
while naamspeler == "":
    print("Uw spelersnaam is niet opgeslagen, probeer het opnieuw.")
    naamspeler = input("Wat is de naam van uw speler? ")

Spelregels = input("Wilt u de spelregels weten? (Ja/Nee) ").strip().lower()
#ChatGPT 11-2-2026 / 13-2-2026

while not (Spelregels.startswith("ja") or Spelregels.startswith("nee")):
    Spelregels = input("Typ ja of nee: ").strip().lower()

if Spelregels.startswith("ja"):
    print("\n")
    print("Het doel van het spel is om een vijfletter-, zesletter- of een zevenletterwoord te raden door middel van andere woorden. U heeft 6 pogingen om dit te doen, als uw een letter goed raad, kleurt het hokje wit, als de letter in het woord zit maar niet op de juiste plek dan kleurt het hokje grijs en als de letter niet goed is blijft het hokje zwart/leeg.")
    print("\n")
else:
    print("Succes!")
    print("\n")

# Woordlengte kiezen
LengteWoord = input("Wilt u een vijfletterwoord, zesletterwoord of zevenletterwoord proberen te raden?")
print("\n")

while LengteWoord not in ("5", "vijf", "vijfletterwoord", "6", "zes", "zesletterwoord", "7", "zeven", "zevenletterwoord"):
    # ChatGPT 11-2-2026
    LengteWoord.strip().lower() == input("Ongeldige keuze. Kies: vijfletterwoord, zesletterwoord of zevenletterwoord.")

# Bevestiging
Confirmatie = input("Weet u dit zeker? (Ja/Nee)")
while Confirmatie.strip().lower() != "ja":
    if Confirmatie.strip().lower() == "nee":
        LengteWoord = input("Kies opnieuw: vijfletterwoord, zesletterwoord of zevenletterwoord: ")
    Confirmatie.strip().lower() == input("Weet u dit zeker? (Ja/Nee)")

print("Oke. We gaan beginnen!")

# Woord
if LengteWoord.lower().startswith(("vijf", "5")):
    geheim_woord = random.choice(VijfLetterWoorden)
    ALetter = len(geheim_woord)
    # ChatGPT 11-2-2026
elif LengteWoord.lower().startswith(("zes", "6")):
    geheim_woord = random.choice(ZesLetterWoorden)
    ALetter = len(geheim_woord)

else:
    geheim_woord = random.choice(ZevenLetterWoorden)
    ALetter = len(geheim_woord)

print("Uw woord is gekozen.")

# Spel
pogingen = MaxPogingen
geraden = False

while pogingen > 0 and not geraden:

    raden = input("Probeert u eens: ").lower()

# Lengte controleren
    if len(raden) != ALetter:
        print("Uw woord moet", ALetter, "letters hebben.")
        continue

# Feedback
    feedback = ""
    for i in range(ALetter):
        if raden[i] == geheim_woord[i]:
            feedback += "🟩"
        elif raden[i] in geheim_woord:
            feedback += "🟨"
        else:
            feedback += "⬜"

    print("Resultaat:", feedback)
# Raden
    if raden == geheim_woord:
        geraden = True
        print("Geweldig,", naamspeler, "! U heeft het woord geraden!")
    else:
        pogingen -= 1
        print("U heeft nog", pogingen, "pogingen over.")

if not geraden:
    print("Helaas,", naamspeler, "u heeft verloren.")
    print("Het woord was:", geheim_woord)


