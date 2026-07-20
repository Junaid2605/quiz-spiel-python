import random
datei = open("Quizfragen.txt", "r")
fragen = datei.readlines()
datei.close()

# print(fragen)



print("Willkommen zum Quiz!")
punkte = 0

quiz = {}

for zeile in fragen:
    frage, antwort = zeile.strip().split(";")
    quiz[frage] = antwort
    
repeat len(quiz):

    frage = random.choice(list(quiz.keys()))
    antwort = input(frage + " ")
    
    richtigeAntwort = quiz[frage]
    
    if antwort.upper() == richtigeAntwort.upper():
        print("Richtig! 🎉")
        punkte += 1
        
    else:
        print("Falsch!")
        print("Die richtige Antwort war:", richtigeAntwort)
        
del quiz[frage]
        
print("----------------")
print("Quiz beendet!")
print("Du hast", punkte, "von 3 Fragen richtig beantwortet.")

if punkte == len(fragen):
    print("Perfekt! Alle Fragen richtig! 🏆")

elif punkte >= len(fragen) / 2:
    print("Gut gemacht! 👍")

else:
    print("Da ist noch Luft nach oben. Übe weiter! 💪")