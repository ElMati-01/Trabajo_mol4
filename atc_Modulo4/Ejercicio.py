# Tuplas:

######### Ejemplo 1

# numeros= ("Uno","Dos","Tres","Cuatro","Cinco",)
# print(numeros[1])
# print(numeros[4])

######### Ejemplo 2
# my_tuple = (5,10,33,300,)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print("_____________")
# print(my_tuple[:-2])

# print("\nTodos los numeros de la lista:")

# for repeat in my_tuple:
#    print(repeat)

#### Ejemplo 3

# sandwich=("Atún", "Queso", "Jamón",)

# print(len(sandwich))
# print("Atún" in sandwich)

################# Diccionarios
# Ejercicio 1

# animales = {"cat": "gato", "perro": "dog", "caballo": "horse"}
# palabras = ['gato', 'león', 'caballo']

# for word in palabras:
#     if word in animales:
#         print(word, "->", animales[word])
#     else:
#         print(word, "no está en el diccionario")

# Ejercico 2
 
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# for key in dictionary.keys(): #extraer del diccionario todas las keys (clave) que tenemos en este, para hacer cosas tales como imprimirlas
#     print(key, "->", dictionary[key])

# Ejercicio 3

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# for valor in dictionary.items(): #extraer del diccionario todas los items (valor) que tenemos en este, para hacer cosas tales como imprimirlas
#     print(valor, "->", dictionary[valor])

#
### excepciones

# #zerDivisorError

# def division(num1,num2):
#     try:
#         resultado = num1/num2
#         print(resultado)
#     except ZeroDivisionError:
#         print("no se puede dividir por cero")
    
# division(89,0)

# print("\n")

# #indexError

# lista = [1, 2, 3]
# try:
#     elemento = lista[8]
# except IndexError:
#     print("Error: El índice está fuera del rango de la lista.")
  
# print("\n")


# #TypeError

# try:
#     resultado = "10" + 5
# except TypeError:
#     print("Error: No se puede concatenar una cadena de texto con un número.")

# print("\n")

# #ValueError
# try:
#     numero = int("abc")
# except ValueError:
#     print("Error: No se puede convertir 'abc' a un entero.")
