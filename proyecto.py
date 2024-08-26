'''
Jesús Osvaldo Ramos Pérez A01713833
1.Entrada:
1.1 Solicitar la longitud de la contraseña.
1.2 Preguntar si desean incluir letras mayúsculas.
1.3 Preguntar si desean incluir letras minúsculas.
1.4 Preguntar si desean incluir números.
1.5 Preguntar si desean incluir símbolos.

2.Inicialización del programa:
2.1 Crear una variable vacía para almacenar los datos.
2.2 Crear una variable para almacenar la contraseña generada.

3.Agregar los tipos de caracteres:
3.1 Si se permite letras mayúsculas, agregar letras mayúsculas a la variable de caracteres válidos.
3.2 Si se permite letras minúsculas, agregar letras minúsculas a la variable de caracteres válidos.
3.3 Si se permiten números, agregar números a la lista de caracteres válidos.
3.4 Si se permiten símbolos, agregar símbolos a la lista de caracteres válidos.

4.Generar la contraseña:
4.1 Seleccionar un carácter aleatorio de la variable de caracteres válidos.
4.2 Añadir el carácter seleccionado a la variable de la contraseña.

5.Mostrar la contraseña:
5.1 Convertir la variable de la contraseña a una cadena de texto.
5.2 Mostrar la contraseña generada al usuario.
'''
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
for i in range (longitud):
    contraseña+=random.choice(lista5)

print("la contraseña generada es: ",contraseña)


