Name = input("Wie heißt du?: ")
Geschlecht = ["w", "m"]
while True:
    input_var_1 = input("Bitte gib dein Geschlecht (w/m) ein: ")
    if input_var_1 in Geschlecht:
            if input_var_1 is "w":
                w = "eine Frau"
            elif input_var_1 is "m":
                m = "ein Mann"
            break
    else:
        print ("Bitte nur gültige Eingabe w oder m!")
    continue
Alter = input("Gib noch dein Alter ein: ")
Größe = input("Wie groß bist du (in cm)?: ")
Gewicht = input("Wie viel wiegst du (in kg)?: ")
print("Hallo " + Name + "! Du bist: ")
print("eine Frau") if input_var_1 is "w" else print("ein Mann") if input_var_1 is "m" else print("ok")
print("Du bist " + Alter + " Jahre alt, wiegst " + Gewicht + "kg und bist " + Größe + "cm groß!")