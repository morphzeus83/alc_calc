Groesse = int(input("Wie groß bist du in cm? ")) # User input hight
Gewicht = int(input("Wie viel kg wiegst du? ")) # User input weight

# Factor of alcohol reduction per hour
wr = 0.31223 - 0.006446 * Gewicht + 0.004466 * Groesse
mr = 0.31608 - 0.004821 * Gewicht + 0.004432 * Groesse

Geschlecht = {"w" : ["weiblich", wr], "m" : ["männlich", mr]} # Dictionary what's "w" and "m"

# User input for gender
while True:
    Geschlechtsabfrage = input("Bitte gebe dein Geschlecht ein (w/m): ")
    if Geschlechtsabfrage in Geschlecht:
        break
    print("Falsche Eingabe! Bitte nur w oder m eingeben!")

# Definition weight of alcohol per ml
Alkohol_gewicht = 0.8

Bier_menge = int(input("Bitte die Biermenge in ml eingeben: ")) # User input amount of beer in ml
Trink_zeit = int(input("Bitte die Trinkzeit in vollen Stunden angeben: ")) # User input time amount of drinking

# Calculation of alcohol amount in ml
Bier_alk = Bier_menge * 0.05

# Calculation of consumed alcohol in grams
Alk = Bier_alk * Alkohol_gewicht

# Theoretical per mille value of consumed alcohol
Promille_theo = Alk / (Gewicht * Geschlecht[Geschlechtsabfrage][1])

# Cleaned per mille value of exhaust alcohol by 15%
Promille_clean = Promille_theo - Promille_theo * 0.15

# Real pro mille value of consumed alcohol during drinking time
Promille = Promille_clean - Trink_zeit * 0.15

print("Hallo! Du bist", Geschlecht[Geschlechtsabfrage][0], ", bist", Groesse, "cm groß und wiegst", Gewicht, "kg")

# Warning if you are allowed or not to drive a car
if Promille >= 0.3:
    print("Du solltest nicht mehr fahren!!!")
else:
    print("Du darfst noch fahren, solltest aber nichts mehr trinken!")
    
print("Du hast noch", Promille, "Promille im Blut")