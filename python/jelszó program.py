#az adatok/változókg
jelszo = "kecskebéka0000"

bemenet = (input("Mi a jelszó? "))

hiba = 0

while bemenet != jelszo:
    hiba += 1
    if hiba == 3:
        print ("Hibás jelszó, Hozzáférés megtagadva, rendszer lezárva!")
        break
    print ("Hibás jelszó,probáld újra")
    bemenet = (input("Mi a jelszó? "))


if bemenet == jelszo:
    print ("Hozzáférés megadva")
