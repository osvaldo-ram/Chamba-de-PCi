#Jesús Osvaldo Ramos Pérez A01713833
# se importa la librería random, para usar el método choice
import random
lista1=list("aeiou")
lista2=list("AEIOU")
lista3=list("1234567890")
lista4=list("-*+./_")
lista5=[]
seguridad=0
longitud=int(input("Cuál es la longitud de caracteres que quieres en tu contraseña? : "))
mayusculas=(input("Quieres agregar mayusculas a tu contraseña?si/no: "))
#Los condicionales los utilice para delimitar lo que escoge o no el usuario
if mayusculas=='si':
    lista5.extend(lista2)
    seguridad+=2
minusculas=(input("Quieres agregar minusculas a tu contraseña?si/no: "))
if minusculas=='si':
    lista5.extend(lista1)
    seguridad+=1
numeros=(input("Quieres agregar numeros a tu contraseña?si/no: "))
if numeros=='si':
    lista5.extend(lista3)
    seguridad+=3
simbolos=(input("Quieres agregar simbolos tu contraseña?si/no: "))
if simbolos=='si':
    lista5.extend(lista4)
    seguridad+=4
'''
El for lo utilice para generar la contraseña basada en la longitud de lo que pidió el usuario.
Se usó el método choice para escoger los caracteres que tendrá la contraseña
'''
def generar_contraseña (long,lista):
    listaF=''    
    for i in range (long):
        listaF+=random.choice(lista)
    return listaF

contraseña=generar_contraseña(longitud,lista5)
if seguridad>7:
    print("La contraseña es segura")
if seguridad>4 and seguridad<7:
    print("La contraseña es aceptable")
if seguridad<4:
    print("La contraseña no es segura")
    
print("la contraseña generada es: ",contraseña, " y tiene un numero de caracteres de ",len(contraseña))



