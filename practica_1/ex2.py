#Importamos libreria sys para leer strings
import sys

#Definimos la función para crear cadena de números
def CrearCadena(numero):
    cadena=[]
    for i in range (1,numero+1):
        cadena.append(i)
    return cadena

def Primos(cadena):
    primos=[]
    for i in range (1,len(cadena)+1):
        a=es_primo(i)
        if a==True:
            if i!=1:
                primos.append(i)
    return primos

def es_primo(i):
    for n in range(2, i):
        if i % n == 0:
            return False
    return True
        
# Guardamos en una variable la posición 1 en la consola.
    # Para operaciones logicas lo guardamos como int
numero=int(sys.argv[1])

# Se manda a llamar la función que creara la matriz de números
    #y guardamos en una variable el resultado
cadena=CrearCadena(numero)

#Imprimimos mcadena de número generada
print (cadena)

# Se manda a llamar la función que analizara que númros son primos
    #y guardamos en una variable el resultado
primos=Primos(cadena)

#Imprimimos los numeros primos
print ("Los números primos son: ")
print(primos)