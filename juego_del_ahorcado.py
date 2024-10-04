### VIDEO DESDE 6.00 hs #####
import random

def obtener_palabra_secreta() -> str: # de esta forma seguramos que siempre devuelva string
    palabras = ['python','java','javascript','angular','django','tensorflow','react','typescript','git','flask']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''
    
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += '_'
    return adivinado
    
def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False
    
    print('¡Bienvenido al juego del ahorcado!')
    print(f"Tenés {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), 'La longitud de la pabra secreta es: ', len(palabra_secreta) )
    
    while not juego_terminado and intentos > 0:
        adivinanza = input('Introduce una letra: ').lower()
        
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print('Introduzca una letra válida(solo escroibir una letra)')
        elif adivinanza in letras_adivinadas:
            print('Ya intentaste esa letra, prueba con otra')
        else:
            letras_adivinadas.append(adivinanza)
            
            if adivinanza in palabra_secreta:
                print(f"Muy bien has acertado, la letra '{adivinanza}' está en la palabra buscada")
            else:
                intentos -= 1
                print(f"Lo siento mucho la letra '{adivinanza}' no esta presente en la palabra")
                print(f'Te quedan {intentos} intentos')
        
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)
        
        if '_' not in progreso_actual:
            palabra_secreta = palabra_secreta.capitalize()
            print(f"¡¡Felicitaciones has ganado, la palabra secretsa es: '{palabra_secreta}'!!")
                
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Lo siento mucho se te terminaron los intentos, la palabra era: '{palabra_secreta}'")
        

juego_ahorcado()