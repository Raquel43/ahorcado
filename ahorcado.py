import random

def ahorcado():
    nombre=input("Diga su nombre: ")
    print(f"{nombre}.Comienza el juego del ahorcado!!!")
    print("Los espacios se corresponden a cada letra de la palabra")
    listaPalabras=["gato","perro","foca","elefante","caballo","pajaro"]
    espacios=[]
    listaSecreta=[]
    listaIncorrectas=[]
    intentos=int()
    secreta=random.choice(listaPalabras)
    listaSecreta=list(secreta)
    
    for i in range(len(secreta)):
        espacios.append("_")
    print(espacios)
    while listaSecreta!=espacios:
        letra=input("Diga una letra: ")
        while letra.isalpha()==False or len(letra)>1:
            letra=input("Incorrecto, introduzca una letra: ")
    
        if letra in listaSecreta:
        
            for i in listaSecreta:
                
                indices=[x for x, e in enumerate(listaSecreta) if e==letra]
                
                for e in indices:
                    for a in espacios:
                        espacios[e]=letra
        else:
            pinta_ahorcado(intentos)
            listaIncorrectas.append(letra)
            intentos+=1
            if intentos == 6:
                print(f"Lo siento {nombre}, ha perdido! La palabra era: {secreta}")
                print(f"La lista de letras erroneas introducidas es: {listaIncorrectas}")
        print(espacios)

    if listaSecreta == espacios:
            print(f"{nombre}, has ganado el juego!! Has cometido {intentos} errores")
            print(f"La lista de letras erroneas introducidas es: {listaIncorrectas}")







def pinta_ahorcado(num_intents = 0):
    print ("______")
    print ("|        |")
        
    if num_intents == 0:
        print ("|")
        print ("|")
        print ("|")
    else:
        if num_intents == 1:
            print ("|        O")
            print ("|")
            print ("|")
        else:
            if num_intents == 2:
                print ("|        O")
                print ("|         |")
                print ("|")
            else:
                if num_intents == 3:
                    print ("|        O")
                    print ("|       /|")
                    print ("|")
                else:
                    if num_intents == 4:
                        print ("|        O")
                        print ("|       /|\ ")
                        print ("|")
                    else:
                        if num_intents == 5:
                            print ("|        O")
                            print ("|       /|\ ")
                            print ("|       / ")
                        else:
                            if num_intents == 6:
                                print ("|        O")
                                print ("|       /|\ ")
                                print ("|       / \ ")
    print ("|")
    print ("|___")

ahorcado()