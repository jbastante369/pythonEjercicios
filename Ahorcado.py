from random import *

palabras = ["AGUACATE","PAJARO","BROCOLI","AVION","CONTINENTE","LOCOMOTORA","CARACOL","PULPO","MAGMA","GUADAÑA",
            "SERPIENTE","MIOPIA","ARAÑA","MAGDALENA","RAFLESIA","PYTHON","FUEGO","HIELO","DICCIONARIO","MARIONETA",
            "CEMENTERIO","TITANIO","ELECTROMAGNETISMO","HOSPITAL","ORACLE","FILOSOFIA","JAVA","HAMBRE","PESTE",
            "GUERRA","MUERTE"]

palabra_descubrir = palabras[randint(0,len(palabras)-1)]

def mostrar_palabra(palabra,letra,intento):
    resultado = ""
    recorer = 0
    for p in palabra:

        if (p == letra ):
            resultado = resultado + letra
        else:
            resultado = resultado + intento[recorer]
        recorer += 1

    return str(resultado)

def crear_intento(lenght):
    return "_"*lenght


vidas = 6
intento = crear_intento(len(palabra_descubrir))

letra = ' '
print(intento)
while vidas > 0 and palabra_descubrir != intento:
    print ("Vidas: "+ str(vidas))
    letra = input("Dime una letra: ").upper()
    resultado = mostrar_palabra(palabra_descubrir, letra, intento)
    if  letra not in palabra_descubrir:
        vidas -= 1
    intento = resultado
    print(intento)
    print(" ")
else:

    if vidas > 0:
        print("Felicidaddes la has acertado")
    else:
        print("Lo siento no has podido acertarla era "+ palabra_descubrir)

