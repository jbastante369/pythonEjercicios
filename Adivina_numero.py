from random import *
numero = randint(1, 101)
intentos = 8
intentos_tomados = 0
prueba = 0
nombre = input("Dame tu nombre: ")
while intentos > 0 and prueba != numero:
    print("Intentos: "+ str(intentos))
    prueba = int(input("Adivina el numero del 1 al 100: "))
    if prueba != numero:
        intentos -= 1
        intentos_tomados += 1
    if prueba > numero:
        print("El numero es menor")
    if prueba < numero:
        print("El numero es mayor")
    if prueba == numero:
        print(" ")
        print(nombre + " acertartes has tardado " + str(intentos_tomados) + " intentos")
    print(" ")
else:
    print("Se ha acabado el programa")