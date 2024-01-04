# 04/01/2024 02:39 Notte
# Primo programma in pyton
# Il tipo delle variabili non va messo
theworld_is_flat = True
# A quanto pare le parentesi graffe non esistono
if theworld_is_flat:
    print("Be careful not to fall off!")

# Matematica
num1 = 20
num2 = 30
if theworld_is_flat:
    print(num1 + num2)


# Funzioni

# Funzione che saluta una persona
def saluta_persona(nome, cognome, eta):
    print(f"Ciao {nome} {cognome}! Benvenuto. Hai {eta} anni.")

#Funzione per la somma tra due numeri
def somma(a,b):
    return a+b


# Chiamate Funzioni

saluta_persona("Luigi", "Ariano", 18)
print(somma(num1,num2))


# Creazione di una classe
class Persona:
    def __init__(self,nome,cognome,eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta
        saluta_persona(nome,cognome,eta)

    # Metodi per la classe persona
    def Benvenuto(self):
        print(f"Benvenuto all'interno della classe {self.nome}")


# istanze della classe persona
persona1=Persona("Marco","Rossi",30)

print("Nome: ", persona1.nome)
print("Cognome: ",persona1.cognome)
print("Eta:", persona1.eta)
persona1.Benvenuto()
