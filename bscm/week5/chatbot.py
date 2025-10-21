import random

# Alle data dat ik nodig heb 
kanyeWords = ["kanye", "west"]
tempWords = ["koud", "weer", "temperatuur", "temp", "warm"]
posWords = [
    "goed", "positief", "leuk", "nice", "slay",
    "top", "super", "geweldig", "fantastisch", "cool",
    "heerlijk", "chill", "blij", "tevreden", "happy",
    "excellent", "briljant", "sterk", "mooi", "gezellig"
]
negWords = [
    "slecht", "oei", "bad",
    "vervelend", "stom", "rot", "triest", "droevig",
    "negatief", "vreselijk", "jammer", "zwaar", "kut",
    "teleurstellend", "boos", "ellendig", "onhandig",
    "waardeloos", "meh", "pijnlijk"
]

positiveSentences = [
    "W bro.",
    "Echt fire 🔥",
    "Slay fr.",
    "Hard af.",
    "Lekker bezig.",
    "Top vibe.",
    "Gas geven.",
    "Bro, dat is clean.",
    "Nice one.",
    "Dat is wild.",
    "Sowieso W.",
    "Je hebt ge-cooked.",
    "Alles on point.",
    "Goated gedrag.",
    "W move.",
    "Helemaal top.",
    "Sick gedaan.",
    "Dat was peak.",
    "Big win bro.",
    "Real one."
]

negativeSentences = [
    "L bro.",
    "Dat was echt mid.",
    "Rip 💀",
    "Cringe moment.",
    "Down bad.",
    "Flop move.",
    "Niet it.",
    "Bro… pijn.",
    "Slechte vibe.",
    "Dat is trash.",
    "Boenk mis.",
    "Skibidi L.",
    "Zwaar meh.",
    "Bro, lost.",
    "Geen W hier.",
    "Teleurstelling fr.",
    "Weak af.",
    "Kut dag man.",
    "Oef, dat doet pijn.",
    "Zero riz."
]

neutralSentences = [
    "Tja bro.",
    "Oké dan.",
    "Kan zijn.",
    "Facts.",
    "Chill.",
    "Mjah.",
    "True dat.",
    "Zeg maar.",
    "We’ll see.",
    "Aight.",
    "Gewoon zo.",
    "Snap ik.",
    "Fair point.",
    "Whatever.",
    "Idk man.",
    "Rustig aan.",
    "Cool ig.",
    "Same tbh.",
    "Gaat wel.",
    "Is wat het is."
]


commando = input()

def wordInPhrase(words, phrase):
    if any(word.lower() in phrase.lower() for word in words):
        return True
    else:
        return False

def categorisePhrase(phrase):
    if wordInPhrase(kanyeWords, phrase):
        return "kanye"
    elif wordInPhrase(tempWords, phrase):
        return "temp"
    elif wordInPhrase(posWords, phrase):
        return "positief"
    elif wordInPhrase(negWords, phrase):
        return "negatief"
    
    return "neutral"

def randomPhrase(phrases): 
    return random.choice(phrases)

# positief, negatief, kanye, temp, neutraal
while commando != "stop":
    # Iets antwoorden 
    category = categorisePhrase(commando)

    if category == "kanye":
        print("rachid: ik haal een kanye quote op")
    elif category == "temp":
        print("rachid: ik haal een temperatuur op")
    elif category == "positief":
        print(randomPhrase(positiveSentences))
    elif category == "negatief":
        print(randomPhrase(negativeSentences))
    else:
        print(randomPhrase(neutralSentences))

    # Opnieuw vragen 
    commando = input()

print("rachid: Thx byekes")