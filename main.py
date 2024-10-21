#Jesús Osvaldo Ramos Pérez A01713833
# se importa la librería random, para usar el método choice
#Se hizo una matriz que contiene los tipos de datos para generar la contraseña
import random

datos = [
    list("aeiou"),
    list("AEIOU"),
    list("1234567890"),
    list("-*+./_")
]
seguridad = 0


def generar_contraseña(longitud, lista_tipos):
    """
    Genera una contraseña garantizando al menos un carácter de cada tipo seleccionado.
    """
    listaF = []
    
    # Garantizar al menos un carácter de cada tipo seleccionado
    for tipo in lista_tipos:
        listaF.append(random.choice(tipo))
    
    # Rellenar el resto de la contraseña al azar
    while len(listaF) < longitud:
        listaF.append(random.choice(random.choice(lista_tipos)))
    
    # Mezclar los caracteres para mayor aleatoriedad
    #shuffle es un método que organiza el orden de la lista
    #https://www.w3schools.com/python/ref_random_shuffle.asp
    random.shuffle(listaF)
    
    #join convierte los elementos de una lista en un solo string, siendo separados por un caracter, en este caso usamos un caracter vacio para tener la contraseña correctamente generada
    #https://www.w3schools.com/python/ref_string_join.asp
    return ''.join(listaF)


def evaluar_seguridad(seguridad):
    """
    Evalúa y muestra el nivel de seguridad de la contraseña.
    """
    if seguridad > 7:
        print("La contraseña es segura")
    elif 4 < seguridad <= 7:
        print("La contraseña es aceptable")
    else:
        print("La contraseña no es segura")

#Ciclo para generar contraseñas mientras el usuario lo requiera
while True:
    menu = int(input("1-Crear contraseña  2-Salir  "))
    
    if menu == 1:
        longitud = int(input("¿Cuál es la longitud de caracteres que quieres en tu contraseña? (Min. 4 caracteres) : "))
        #Ciclo para asegurar el minimo para generar la longitud de la contraseña
        while longitud<4 :
            longitud = int(input("¿Cuál es la longitud de caracteres que quieres en tu contraseña? (Min. 4 caracteres) : "))
            
            
        lista_tipos = []
        
        mayusculas = input("¿Quieres agregar mayúsculas a tu contraseña? (si/no): ")
        if mayusculas.lower() == 'si':
            lista_tipos.append(datos[1])
            seguridad += 2

        minusculas = input("¿Quieres agregar minúsculas a tu contraseña? (si/no): ")
        if minusculas.lower() == 'si':
            lista_tipos.append(datos[0])
            seguridad += 1

        numeros = input("¿Quieres agregar números a tu contraseña? (si/no): ")
        if numeros.lower() == 'si':
            lista_tipos.append(datos[2])
            seguridad += 3

        simbolos = input("¿Quieres agregar símbolos a tu contraseña? (si/no): ")
        if simbolos.lower() == 'si':
            lista_tipos.append(datos[3])
            seguridad += 4

        if lista_tipos:
            contraseña = generar_contraseña(longitud, lista_tipos)
            evaluar_seguridad(seguridad)
            
            print(f"La contraseña generada es: {contraseña} y tiene un número de caracteres de {len(contraseña)}")
        else:
            print("Debes seleccionar al menos un tipo de carácter para generar la contraseña.")
    
    else:
        break


    
