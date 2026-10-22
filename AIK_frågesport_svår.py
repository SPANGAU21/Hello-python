
print("=== AIK QUIZ: SVÅR NIVÅ ===\n")

poang = 0

fragor = [
    {
        "fraga": "1. Vilket lag besegrade AIK i SM-finalen 1900?",
        "alternativ": [
            "1. Örgryte IS",
            "2. Djurgårdens IF",
            "3. IFK Göteborg"
        ],
        "svar": "1"
    },
    {
        "fraga": "2. Vilken AIK-spelare har gjort flest mål totalt för herrlaget?",
        "alternativ": [
            "1. Ivan Obolo",
            "2. Per Kaufeldt",
            "3. Henok Goitom"
        ],
        "svar": "2"
    },
    {
        "fraga": "3. Vilket år vann AIK sitt första SM-guld i fotboll?",
        "alternativ": [
            "1. 1898",
            "2. 1900",
            "3. 1911"
        ],
        "svar": "2"
    },
    {
        "fraga": "4. Vem var AIK:s tränare när laget vann Allsvenskan 1998?",
        "alternativ": [
            "1. Stuart Baxter",
            "2. Rikard Norling",
            "3. Andreas Alm"
        ],
        "svar": "1"
    },
    {
        "fraga": "5. Vilken arena spelade AIK sina hemmamatcher på fram till 2012?",
        "alternativ": [
            "1. Stockholms Stadion",
            "2. Råsunda Fotbollsstadion",
            "3. Söderstadion"
        ],
        "svar": "2"
    },
    {
        "fraga": "6. Vilket år vann AIK Svenska cupen och Allsvenskan?",
        "alternativ": [
            "1. 1998",
            "2. 2009",
            "3. 2018"
        ],
        "svar": "2"
    },
    {
        "fraga": "7. Hur många SM-guld i fotboll hade AIK enligt klubbens historik efter guldet 2018?",
        "alternativ": [
            "1. 10",
            "2. 12",
            "3. 14"
        ],
        "svar": "2"
    },
    {
        "fraga": "8. Vilken AIK-spelare gjorde fem mål i en Allsvensk match 1993?",
        "alternativ": [
            "1. Kim Bergstrand",
            "2. Krister Nordin",
            "3. Pascal Simpson"
        ],
        "svar": "1"
    },
    {
        "fraga": "9. Vilket år spelade AIK sin sista match på Råsunda?",
        "alternativ": [
            "1. 2009",
            "2. 2012",
            "3. 2015"
        ],
        "svar": "2"
    },
    {
        "fraga": "10. Vilken AIK-legend debuterade i A-laget och landslaget 1919?",
        "alternativ": [
            "1. Per Kaufeldt",
            "2. Putte Kock",
            "3. Gunnar Nordahl"
        ],
        "svar": "2"
    }
]

for fraga in fragor:
    print(fraga["fraga"])

    for alternativ in fraga["alternativ"]:
        print(alternativ)

    svar = input("Välj 1, 2 eller 3: ").strip()

    if svar == fraga["svar"]:
        print("Rätt! 🖤💛\n")
        poang += 1
    else:
        print("Fel!")
        print("Rätt svar:", fraga["svar"], "\n")

print("=== RESULTAT ===")
print("Du fick", poang, "av", len(fragor), "poäng.")


if poang == 10:
    print("Otroligt! Du är en riktig AIK-expert!")
elif poang >= 7:
    print("Starkt jobbat! Du kan mycket om AIK!")
elif poang >= 4:
    print("Bra försök! Fortsätt lära dig AIK:s historia.")
else:
    print("Du har mer AIK-historia att upptäcka!")
