import random

# Lijsten
VijfLetterWoorden = [
    "acces", "acryl", "addax", "affix", "aftyp", "ampex", "axels", "babys", "baggy", "batch",
    "bobby", "buggy", "buddy", "buxus", "bitch", "blijf", "bodys", "bogey", "bytes", "check",
    "chick", "click", "cocci", "curry", "cycli", "dizzy", "derby", "dummy", "dicht", "dwaze",
    "epoxy", "enzym", "ethyl", "exact", "essay", "extra", "happy", "hobby", "husky", "hyper",
    "hypes", "hypet", "hysop", "guppy", "gipsy", "gyros", "grijp", "geluw", "glijd", "gulpt",
    "vinyl", "vieux", "vacht", "vecht", "vijlt", "vipje", "vlezе", "wacht", "wijze", "winch",
    "wrijf", "wazig", "wezel", "whist", "wigje", "xerox", "xeres", "xenon", "yucca", "yanks",
    "yards", "zloty", "zwijg", "zwijm", "zicht", "zucht", "zwalp", "zwamp", "zacht", "zocht",
    "acryl", "baggy", "cysts", "folky", "lycra", "pique", "quilt", "rugby", "squaw", "jazzy",
    "proxy", "query", "fylum", "lobby", "sexys", "waxje", "campy", "crazy", "crypt", "chijl",
    "chimp", "dacht", "dandy", "derny", "detox", "docht", "dwars", "epiek"
]

ZesLetterWoorden =  [
    "acquit","afwijk","afzwak","afzwem","afzwoom","accept","afkick","afwijs","abject","achtje",
    "afbijt","afbouw","affect","byebye","bobbys","buggys","bakmix","boycot","brique","bypass",
    "bluesy","boxjes","buddys","byssus","backup","catchy","cyclus","chique","cowboy","cheque",
    "clique","cyborg","cynici","calque","cervix","claque","climax","crypte","cypers","chicks",
    "currys","dinghy","dummys","duplex","derbys","dollys","deejay","dichts","duwbak","dandys",
    "dernys","dichte","dijkje","dikbil","dikzak","doffig","exquis","exchef","epifyt","equipe",
    "excuus","exprof","embryo","epoche","elixir","episch","exacte","expats","expert","gymjuf",
    "glycol","guppys","gympje","gipsys","gympie","gefaxt","gemixt","glossy","groggy","groovy",
    "grungy","hobbys","hobbyt","hockey","hybris","huskys","hiphop","hydras","hymens","hymnes",
    "ijsbox","influx","idylle","impact","inwijk","inzwem","inzwom","ijsbal","ijsbok","ijzelt",
    "jockey","juicht","jersey","jezelf","jaszak","jippie","jochie","juffer","juffie","jujube",
    "klysma","kwikwi","klucht","kwijlt","kippig","kirsch","kitsch","klacht","krucht","kwezel"
]

ZevenLetterWoorden  = [
    "Acquits", "Acrogym", "Afschuw", "Afzicht", "Afblijf", "Afwacht", "Afwrijf", "Afzocht",
    "Aquavit", "Aquifer", "Accubak", "Affiche", "Affixen", "Afhecht", "Aflicht", "Afschaf",
    "Babybox", "Babypop", "Boxcalf", "Babybus", "Bijwijf", "Babybad", "Babybed", "Babybos",
    "Babyvet", "Bezwijk", "Bezwijm", "Babyaap", "Cycloop", "Cynisch", "Chiquer", "Cowboys",
    "Cyclaam", "Callboy", "Chatbox", "Cheques", "Citybag", "Cliques", "Complex", "Cyborgs",
    "Cycline", "Cynicus", "Calques", "Calypso", "Duoquiz", "Dactyli", "Display", "Damclub",
    "Dijkweg", "Djilbab", "Doortyp", "Duchtig", "Duwwerk", "Daghulp", "Deejays", "Dialyse",
    "Exquise", "Equinox", "Excerpt", "Exclave", "Exvrouw", "Epifyse", "Equipes", "Exprofs",
    "Ecstasy", "Embryos", "Employe", "Epoques", "Excuses", "Exempel", "Gehypet", "Grizzly",
    "Gympjes", "Gelobby", "Gymzaal", "Gifwijk", "Glycine", "Gympies", "Gewicht", "Gezicht",
    "Gezucht", "Gifpijl", "Glypten", "Gameboy", "Gateway", "Gechipt", "Hickory", "Hockeyt",
    "Hyacint", "Hybride", "Hijzelf", "Halfweg", "Ijsclub", "Idylles", "Incheck", "Infobox",
    "Inzicht", "Ijswijn", "Jacquet", "Jacuzzi", "Jockeys", "Jukebox", "Jurylid", "Jachtig"
]

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
    print("Als u een letter goed raadt, kleurt het hokje wit 🟩,")
    print("als de letter in het woord zit maar niet op de juiste plek dan kleurt het hokje grijs 🟨,")
    print("en als de letter niet goed is blijft het hokje zwart ⬜.\n")
else:
    print("Succes!\n")

# Woordlengte kiezen
LengteWoord = input("Wilt u een vijfletterwoord, zesletterwoord of zevenletterwoord proberen te raden? (5/vijf, 6/zes, 7/zeven) ").strip().lower()

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

    if raden == geheim_woord:
        geraden = True
        print(f"Geweldig, {naamspeler}! U heeft het woord geraden!")
    else:
        pogingen -= 1
        print(f"U heeft nog {pogingen} pogingen over.\n")

if not geraden:
    print(f"Helaas, {naamspeler}, u heeft verloren.")
    print("Het woord was:", geheim_woord)

LevelConfirmatie = input("Wilt uw een moeilijkere level spelen? ")

while LevelConfirmatie.lower().startswith("ja"):
    LengteWoord = input("Wilt u een vijfletterwoord, zesletterwoord of zevenletterwoord proberen te raden? (5/vijf, 6/zes, 7/zeven) ").strip().lower()

    while LengteWoord not in ("5", "vijf", "vijfletterwoord",
                              "6", "zes", "zesletterwoord",
                              "7", "zeven", "zevenletterwoord"):
        LengteWoord = input("Ongeldige keuze. Kies 5/vijf, 6/zes of 7/zeven: ").strip().lower()

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

    if LengteWoord in ("5", "vijf", "vijfletterwoord"):
        geheim_woord = random.choice(VijfLetterWoorden)
    elif LengteWoord in ("6", "zes", "zesletterwoord"):
        geheim_woord = random.choice(ZesLetterWoorden)
    else:
        geheim_woord = random.choice(ZevenLetterWoorden)

    ALetter = len(geheim_woord)
    print("Uw woord is gekozen.\n")

    
    pogingen = MaxPogingen
    geraden = False

    while pogingen > 0 and not geraden:
        raden = input("Probeert u eens: ").strip().lower()

        
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

        print("Resultaat:", " ".join(feedback), "\n")
        
        if raden == geheim_woord:
            geraden = True
            print(f"Geweldig, {naamspeler}! U heeft het woord geraden!")
        else:
            pogingen -= 1
            print(f"U heeft nog {pogingen} pogingen over.\n")

    if not geraden:
        print(f"Helaas, {naamspeler}, u heeft verloren.")
        print("Het woord was:", geheim_woord)

    LevelConfirmatie = input("Wilt u nog een level spelen? ")
    
if LevelConfirmatie.lower().startswith("nee"):
    print("\n")
    print("Einde spel, dankuwel voor het spelen.")
    
# Einde
    

