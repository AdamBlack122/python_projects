email_cim = ("nagyadamaladar@gmail.com")

bemenet = input("mi a e-mail cím ?")

hiba = (0)

while bemenet != email_cim:
	hiba += 1
	if hiba == 3:
		print ("Hibás email_cim, rendszer lezárva!")
		break
	print ("Hibás email_cim, probáld újra!")
	bemenet = input("mi a e-mail cím ?")
if bemenet == email_cim:
	print ("ird be a jelszót is!")

jelszo = ("adamnagy")

bemenet = input("mi a jelszó ?")

hiba_2 = (0)

while bemenet != jelszo:
	hiba += 1
	if hiba_2 == 3:
		print ("Hibás jelszó, rendszer lezárva!")
		break
	print ("Hibás jelszó, probáld újra!")
	bemenet = input("mi a jelszó ?")
if bemenet == jelszo:
	print ("Hozzáférés megadva!")
