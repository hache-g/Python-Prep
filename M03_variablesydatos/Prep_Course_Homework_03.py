#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

a = 24
print (a)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(a))


# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre = "Hector Gonzalez"


# 5) Crear una variable que contenga un número complejo

# In[3]:

complejo = 5 + 7j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print (type(complejo))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:

pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

var1 = 'True' #String content "True"
var2 = True   #Boolean value True


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

# In[5]:

print (type(var1))
print (type(var2))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

x = 7 + 3.8


# 11) Realizar una operación de suma de números complejos

# In[2]:

c1 = 16 + 5j
c2 = 5 + 2j
print (c1 + c2)


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

pi = 3.1416
c3 = 12 + 3j
print (pi + c3)


# 13) Realizar una operación de multiplicación

# In[5]:

5 * 8


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print (2 ** 8)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

d = 27 / 4
print (d)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

print (27 // 4)


# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

print (27 % 4)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

4 * 6 + 3


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

print ("mi nombre es " + nombre)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

2 == "2" #Evaluación FALSO por ser una variable Numérica y otra String


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

2 == int("2") #Evaluación TRUE convirtiendo la variable String a Numérica


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

#Por tener coma "," en lugar de punto
a = float('3.8') #Conversión correcta


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

# In[15]:

x = 3
x -= 1 #Valor final de la variable x es = 2


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1 << 2  = 4
#El operador "<<" (left shift) realiza un desplazamiento a la izquierda bit a bit.
#Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha.
#1 = en binario 0000 0001
#2 = en binario 0000 0010
#Se desplaza 1 (0000 0001) 2 bits (0000 0010) a la izquierda, quedando => 0000 0100, equivalente al valor 4


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

#No se pueden sumar una variable Numérica y un String


# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

2 + int('2')

