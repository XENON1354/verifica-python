#importazione librerie
import re
import random

scelta = input("Scegli pwd semplice o complessa: ").lower()

#definizione delle regole per password semplice e complessa
easyRule = r"[a-zA-Z0-9]"
hardRule = r"."

#creazione della sacca principale di carateri da cui pescare i caratteri
sacco = "".join(chr(i) for i in range(32, 127))

#creazione dei pattern di estrazione
easyPool = re.findall(easyRule, sacco)
hardPool = re.findall(hardRule, sacco)

x = True
#creazione della password in base alla scelta dell'utente
while x == True:

    if scelta == "semplice":
        password = "".join(random.choice(easyPool) for i in range(8))
        print(password)
        print("Arrivederci")
        x = False
    elif scelta == "complessa":
        password = "".join(random.choice(hardPool) for i in range(20))
        print(password)
        print("Arrivederci")
        x = False
    else:
        print("Scelta non valida riprova")