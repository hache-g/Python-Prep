#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

a = 30
if a>0:
  print (a)
elif a<0:
  print (a)


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a = 30
b = 14
if type(a)==type(b):
  print ("son de igual tipo")
else:
  print ("son de distinto tipo")

  
# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1,21):
  if i%2==0:
    print (i, " es par")
  else:
    print (i, " es impar")


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(6):
  print (i**3)


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

i=10
for i in range (1,i+1):
  print (i)

  
# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

varorigen = 49 #variable inicial a factorear
i = varorigen
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #primeros 25 números primos
r = [] #resultado del factoreo
newv = 1 #acumulado de factoreo
if isinstance(i, int) and i>0:
  print (i)
  for j in primos:
    print ("j= ", j)
    while i%j==0:
        i=i//j
        print ("i= ", i)
        r.append(j)
        print ("j= ", j)
        newv*=j
        print ("newv= ", newv)
    if newv>=varorigen:
       break
print(r)


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

s = 3
i = 1
while i<s:
    print (i, "W" + str(i))
    for j in range(1, 6):
        print (j, "Loop")
    i+=1


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

varorigen = 21 #variable inicial a factorear (caso factoreo)
i = varorigen
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #primeros 25 números primos
r = [] #resultado del factoreo
newv = 1 #acumulado de factoreo
if isinstance(i, int) and i>0:
  print (i)
  for j in primos:
    print ("j= ", j)
    while i%j==0:
        i=i//j
        print ("i= ", i)
        r.append(j)
        print ("j= ", j)
        newv*=j
        print ("newv= ", newv)
    if newv>=varorigen:
       break
print(r)

nombres = ['Hector', 'Manuel', 'Gonzalez']
for i in nombres:
  j = 0
  while j < 3:
    print(i, end = ' ')
    j += 1
  print('')
  

# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] #números primos < 30
for i in primos:
    print (i)


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

#Imprimir los números primos menores a 30
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #primeros 25 números primos
for i in primos:
    if i<30:
        print (i)
    else:
        break


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:




# In[57]:




# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# In[58]:





# In[59]:




# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

i = 99
while i<301:
    i += 1
    if i%12 == 0:
        print (i)
    else:
        continue


# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:




# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

i = 99
while i<301:
    i += 1
    if i%6 == 0:
        print (i)
        break
    else:
        continue

