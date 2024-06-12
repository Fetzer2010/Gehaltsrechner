print("Herzlich Willkomen zu meinem Gehaltsrechner")

print(""
      "")

work = int(input("Gebe hier bitte ein wie viele Stunden du am Tag arbeitest: "))
tag_pro_monat = int(input("Gib jetzt ein wie viele Tage du pro Monat arbeitest: "))
stundenlohn = int(input("Bitte geben sie ihren Stundenlohn an: "))
tag = work * stundenlohn
monat = tag_pro_monat * tag
jahresgehalt = 12 * monat

print("Dein Tagesgehalt beträgt " + str(tag) + "€")
print("Du verdienst im Monat " + str(monat) + "€")
print("Dein Jahresgehalt beträgt " + str(jahresgehalt) + "€")

print("")

input("Drücken sie Enter zum beenden des Programmes")
