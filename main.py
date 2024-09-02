Jesús Osvaldo Ramos Pérez A01713833
# se importa la librería random, para usar el método choice
import random
lista1="aeiou"
lista2="AEIOU"
lista3="1234567890"
lista4="-*+./_"
lista5=''
contraseña=''
longitud=int(input("Cuál es la longitud de caracteres que quieres en tu contraseña? : "))
mayusculas=(input("Quieres agregar mayusculas a tu contraseña?si/no: "))
#Los condicionales los utilice para delimitar lo que escoge o no el usuario
if mayusculas=='si':
    lista5=lista2
minusculas=(input("Quieres agregar minusculas a tu contraseña?si/no: "))
if minusculas=='si':
    lista5=lista5+lista1
numeros=(input("Quieres agregar numeros a tu contraseña?si/no: "))
if numeros=='si':
    lista5=lista5+lista3
simbolos=(input("Quieres agregar simbolos tu contraseña?si/no: "))
if simbolos=='si':
    lista5=lista5+lista4
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

print("la contraseña generada es: ",contraseña)



