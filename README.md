# Chamba-de-PCi
Soy Osvaldo y voy a hacer un generador de contraseñas.
Mi programa es una herramienta que sirve para ayudar a las personas a generar contraseñas aleatorias con las especificaciones que ellos quieran. Es útil para las personas que no saben elegir una contraseña, y más aparte una contraseña segura. 
Mi interés en este programa es porque yo tengo ese problema y más agregado a esto, a veces se me olvida la contraseña de cada cosa y utilizo todas las que he usado a lo largo de mi vida para ver cuál funciona.
El programa funciona a base de una librería random y variables con datos ya establecidos. Seguido de esto se le pide al usuario que responda a las preguntas de los tipos de datos que desea agregar a su contraseña (esto funciona a base de condicionales).
 Una vez el usuario haya respondido las preguntas se genera la contraseña a base de una función que recolecta datos aleatorios de las variables establecidas al inicio del programa.
Y finaliza imprimiendo la contraseña generada por el programa.

Situación problema
En la era digital actual, la seguridad de las cuentas en línea es una preocupación creciente. Los usuarios a menudo eligen contraseñas débiles o fácilmente adivinables. Como “1234”, “contraseña”, o su nombre, etc. Este comportamiento pone a los usuarios en riesgo de sufrir ataques de fuerza bruta. Como resultado de estas prácticas, las cuentas de los usuarios son vulnerables a accesos no autorizados, lo que puede llevar a la pérdida de datos personales, robo de identidad y otros problemas relacionados con la privacidad y seguridad.
##Entradas:
longitud (int)
mayusculas(string)
minusculas(string)
numeros(string)
simbolos(string)
##Salidas:
contraseña(string)
#1.Entrada:
1.1Pedir generar contraseña o salir.
1.2 Solicitar la longitud de la contraseña.
1.3 Preguntar si desean incluir letras mayúsculas.
1.4 Preguntar si desean incluir letras minúsculas.
1.5 Preguntar si desean incluir números.
1.6 Preguntar si desean incluir símbolos.
#2.Inicialización del programa:
2.1 Crear una variable vacía para almacenar los datos.
2.2 Crear una variable para almacenar la contraseña generada.
#3.Agregar los tipos de caracteres:
3.1 Si se permite letras mayúsculas, agregar letras mayúsculas a la lista de tipos  de caracteres válidos.
3.1.1 Se aumenta el puntaje de seguridad según sea el tipo de dato seleccionado.
3.2 Si se permite letras minúsculas, agregar letras minúsculas a la lista de tipos  de caracteres válidos.
3.2.1 Se aumenta el puntaje de seguridad según sea el tipo de dato seleccionado.
3.3 Si se permiten números, agregar números la lista de tipos  de caracteres válidos.
3.3.1 Se aumenta el puntaje de seguridad según sea el tipo de dato seleccionado.
3.4 Si se permiten símbolos, agregar símbolos a la lista de tipos  de caracteres válidos.
3.4.1 Se aumenta el puntaje de seguridad según sea el tipo de dato seleccionado.
#4. Generar la contraseña:
4.1 Seleccionar un carácter aleatorio de la lista de tipos caracteres válidos.
4.2 Añadir el carácter seleccionado a la lista de tipos de caracteres válidos de la contraseña.
#5.Mostrar la contraseña:
5.1 Convertir la variable de la contraseña a una cadena de texto.
5.2 Mostrar la contraseña generada al usuario.
5.3 Preguntar por generar una nueva contraseña o salir.


