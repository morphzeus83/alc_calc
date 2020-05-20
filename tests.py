Name = input("Wie heißt du? ")
Alter = int(input("Wie alt bist du? "))
while True:
        Geschlechtsabfrage = input("Bitte gebe dein Geschlecht ein (w/m): ")
        Geschlecht = {"w" : "weiblich", "m" : "männlich"}
        if Geschlechtsabfrage in Geschlecht:
                break
        print("Falsche Eingabe! Bitte nur w oder m eingeben!")
Groesse = int(input("Wie groß bist du in cm? "))
Gewicht = int(input("Wie viel kg wiegst du? "))
print("Hallo ", Name, "Du bist", Geschlecht[Geschlechtsabfrage], "bist", Alter, "Jahre alt, bei einer Körpergröße von ", Groesse, "cm und wiegst", Gewicht, "kg!")