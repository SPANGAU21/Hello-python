
print("=== AIK-QUIZ ===")
print("Testa dina kunskaper om AIK!\n")

poang = 0

fragor = [
    {
        "fraga": "1. Vilket år grundades AIK?",
        "alternativ": ["1. 1891", "2. 1901", "3. 1910"],
        "svar": "1"
    },
    {
        "fraga": "2. Vad står AIK för?",
        "alternativ": [
            "1. Allmänna Idrottsklubben",
            "2. Allsvenska Idrottsklubben",
            "3. Atletiska Idrottsklubben"
        ],
        "svar": "1"
    },
    {
        "fraga": "3. Vilken stad kommer AIK från?",
        "alternativ": ["1. Göteborg", "2. Stockholm", "3. Malmö"],
        "svar": "2"
    },
    {
        "fraga": "4. Vad kallas AIK:s fotbollslag ofta?",
        "alternativ": ["1. Gnaget", "2. Blåvitt", "3. Bajen"],
        "svar": "1"
    },
    {
        "fraga": "5. Vilka färger förknippas med AIK?",
        "alternativ": [
            "1. Grönt och vitt",
            "2. Blått och rött",
            "3. Svart och gult"
        ],
        "svar": "3"
    },
    {
        "fraga": "6. På vilken arena spelar AIK:s herrlag vanligtvis sina hemmamatcher i fotboll?",
        "alternativ": [
            "1. Strawberry Arena",
            "2. Gamla Ullevi",
            "3. Eleda Stadion"
        ],
        "svar": "1"
    },
    {
        "fraga": "7. Vad heter AIK:s stora rival från södra Stockholm?",
        "alternativ": ["1. Malmö FF", "2. Hammarby IF", "3. IFK Göteborg"],
        "svar": "2"
    },
    {
        "fraga": "8. Vilken sport spelar AIK i Allsvenskan?",
        "alternativ": ["1. Fotboll", "2. Handboll", "3. Rugby"],
        "svar": "1"
    },
    {
        "fraga": "9. Vilket smeknamn används för AIK:s supportrar?",
        "alternativ": [
            "1. Änglarna",
            "2. Gnagare",
            "3. Kamraterna"
        ],
        "svar": "2"
    },
    {
        "fraga": "10. Vilket år vann AIK herrarnas Allsvenska i fotboll senast?",
        "alternativ": ["1. 2009", "2. 2018", "3. 2020"],
        "svar": "2"
    }
]

for fraga in fragor:
    print(fraga["fraga"])

    for alternativ in fraga["alternativ"]:
        print(alternativ)

    svar = input("Ditt svar (1, 2 eller 3): ")

    if svar == fraga["svar"]:
        print("Rätt svar!\n")
        poang += 1
    else:
        print("Fel svar!")
        print("Rätt svar är alternativ",
              fraga["svar"], "\n")

print("=== QUIZEN ÄR KLAR ===")
print("Du fick", poang, "av", len(fragor), "poäng.")

if poang == 10:
    print("Fantastiskt! Du är ett riktigt AIK-proffs!")
elif poang >= 7:
    print("Bra jobbat! Du kan mycket om AIK!")
elif poang >= 4:
    print("Helt okej! Du kan en del om AIK.")
else:
    print("Dags att lära dig mer om AIK!")
