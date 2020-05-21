Groesse = int(input("Wie groß bist du in cm? "))
Gewicht = int(input("Wie viel kg wiegst du? "))
Geschlechtsabfrage = input("Bitte gebe dein Geschlecht ein (w/m): ")
wr = 0.31223 - 0.006446 * Gewicht + 0.004466 * Groesse
mr = 0.31608 - 0.004821 * Gewicht + 0.004432 * Groesse
Geschlecht = {"w" : ["weiblich", wr], "m" : ["männlich", mr]}
while True:
    if Geschlechtsabfrage in Geschlecht:
        break
    print("Falsche Eingabe! Bitte nur w oder m eingeben!")
Alkohol_gewicht = 0.8
Bier_menge = int(input("Bitte die Biermenge in ml eingeben: "))
Trink_zeit = int(input("Bitte die Trinkzeit in vollen Stunden angeben: "))
Bier_alk = Bier_menge * 0.05
Alk = Bier_alk * Alkohol_gewicht
Promille_theo = Alk / (Gewicht * Geschlecht[Geschlechtsabfrage][1])
Promille_clean = Promille_theo - Promille_theo * 0.15
Promille = Promille_clean - Trink_zeit * 0.15
print("Hallo! Du bist", Geschlecht[Geschlechtsabfrage][0], ", bist", Groesse, "cm groß und wiegst", Gewicht, "kg")
while True:
    if Promille > 0.3:
        break
    print("Du solltest nicht mehr fahren!!!")
print("Du hast noch", Promille, "Promille im Blut")