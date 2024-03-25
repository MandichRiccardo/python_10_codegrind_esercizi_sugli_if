# esercizio 1
print("il numero è positivo") if int(input("inserisci un numero\n"))>=0 else print("il numero è negativo")
# esercizio 2
a = int(input("inserisci il secondo numero:\t"))
b = int(input("inserisci il primo numero:\t"))
if a > b:
    print("il primo numero è maggiore")
elif b > a:
    print("il secondo numero è maggiore")
else:
    print("i numeri sono uguali")
# esercizio 3
print("la stringa è vuota") if not str(input("inserisci una stringa:\t")) else print("la stringa non è vuota")
# esercizio 4
print("il numero è pari") if int(input("inserisci un numero:\t"))%2==0 else print("il numero è dispari")
# esercizio 5
print("la lettera è una vocale") if input("inserisci una lettera:\t") in "aeiou" else print("la lettera è una consonante")
# esercizio 6
print("il numero è compreso tra 1 e 10") if input("inserisci un numero:\t") else print("il numero non è compreso tra 1 e 10")
# esercizio 7
num = int(input("inserisci un numero intero:\t"))
if num > 10:
    condizione = "maggiore"
elif num < 10:
    condizione = "minore"
else:
    condizione = "uguale"
print("il numero è " + condizione + " a dieci")
# esercizio 8
char = input("inserisci un carattere:\t")
print("hai inserito una vocale") if char in "aeiou" else print("hai inserito una consonante") if char.isalpha() else print("non hai inserito una lettera")
# esercizio 9
latoA = int(input("inserisci la dimensione del primo lato"))
latoB = int(input("inserisci la dimensione del secondo lato"))
latoC = int(input("inserisci la dimensione del terzo lato"))
if latoA**2 + latoB**2 == latoC**2 or latoC**2 + latoB**2 == latoA**2 or latoA**2 + latoC**2 == latoB**2:
    print("è un triangolo rettangolo")
else:
    print("non è triangolo rettangolo")