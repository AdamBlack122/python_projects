#a művleletek 0=+, 1=-, 2=*, 3=/

from pip._vendor.distlib.compat import raw_input

a = float(raw_input("első szám"))
b = float(raw_input ("második szám"))
c = float(raw_input("művelet"))

if c == 0:
    print (a + b)
elif c == 1:
    print (a - b)
elif c == 2:
    print(a * b)
elif c == 3:
    print(a / b)
elif c == 23:
    print ("easter egg azért raktam bele mert a barátom egymás után szerezte ezeket a jegyeket :-)")

else: print ("MONDTAM HOGY CSAK A NÉGY MŰVELETET HASZNÁLHATOD")