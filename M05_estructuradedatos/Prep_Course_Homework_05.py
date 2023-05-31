#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

ciudades = ["Lisboa", "Madrid", "París", "Berlín", "Roma", "Londres"]
print(ciudades)

# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(ciudades[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(ciudades[1:4])

# 4) Visualizar el tipo de dato de la lista

# In[12]:

type(ciudades)

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(ciudades[2:])

# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(ciudades[:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

ciudades.append("Madrid")
print(ciudades)
ciudades.append("Barcelona")
print(ciudades)
#No arroja error

# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

ciudades.insert(3, "Bruselas")
print(ciudades)

# In[21]:

# 9) Concatenar otra lista a la ya creada

# In[22]:

otras = ["Moscú", "Pekín"]
print (otras)
ciudades.extend(otras)
print(ciudades)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

#trae la primera ocurrencia
ciudades.count("Madrid")
print(ciudades.index("Madrid"))
i=0
while (i < len(ciudades)):
    print(ciudades[i])
    i+=1

# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

#Python arroja un error : is not in list

# 12) Eliminar un elemento de la lista

# In[25]:

#busco elementos repetidos
i=0
while (i < len(ciudades)):
    print(ciudades[i])
    n = ciudades.count(ciudades[i])
    if (n > 1):
        print ("hay ", n, " Borro el actual")
        ciudades.remove(ciudades[i])
    i+=1
print(ciudades)

# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

#Python arroja un error : not in list
ciudades.remove("La Haya")

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

ultimo = ciudades.pop()
print (ciudades)
print (ultimo)

# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(ciudades * 4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

enteros = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(enteros[10:16]) -> (11, 12, 13, 14, 15, 16)

# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

enteros.count(20) -> 1
enteros.count(30) -> 0

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

buscar = "Atenas"
i=0
existe = False
while (i < len(ciudades)):
    print(ciudades[i])
    if (ciudades[i] == buscar):
        print ("Elemento ", ciudades[i], " Existe")
        existe = True
        break
    i+=1
if (not existe):
    ciudades.append(buscar)
    print ("No existe, se agregó ", buscar)

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

# 21) Convertir la tupla en una lista

# In[52]:

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:


# 24) Imprimir las claves del diccionario

# In[59]:


# 25) Imprimir las ciudades a través de su clave

# In[61]:




