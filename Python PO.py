print("Welkom bij Lingo!!")

naamspeler = input("Wat is de naam van uw speler? ")
while naamspeler == "":
    print("Uw spelersnaam is niet opgeslagen, probeer het opnieuw.")
    naamspeler = input("Wat is de naam van uw speler? ")

print("Uw spelersnaam is opgeslagen")

# woordlengte kiezen
LengteWoord = input(
    "Wilt u een vijfletter, zesletter of zevenletterwoord proberen te raden? ")

while LengteWoord not in ("vijfletter", "zesletter", "zevenletterwoord"):
    LengteWoord = input(
        "Ongeldige keuze. Kies: vijfletter, zesletter of zevenletterwoord: ")

# bevestiging
Confirmatie = input("Weet u dit zeker? (Ja/Nee) ")

while Confirmatie != "Ja":
    if Confirmatie == "Nee":
        LengteWoord = input(
            "Kies opnieuw: vijfletter, zesletter of zevenletterwoord: ")
    Confirmatie = input("Weet u dit zeker? (Ja/Nee) ")

print("Oke. We gaan beginnen!")
