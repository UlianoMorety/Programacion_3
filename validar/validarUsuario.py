##Modulo de validacion de usuario
def validar(nombre):

    if nombre[0].isupper() == False:
        print("La primera letra del nombre debe ser mayuscula.")

    if nombre.isalpha() == False:
        print("El nombre de usuario solo debe contener letras.")

    if nombre[0].isupper() == True and nombre.isupper() == True:
        return True
def valUsuario(nombre, lista):
        i = 0
        while i < len(lista):
            if lista[i] == nombre:
                print("el nombre que ha ingresado es un nombre prohibido")
                break
            i += 1
        print("el usuario es valido")

def agregar(nombre, lista):
    
    file = open("listaNombre.txt", '+a')
    file.write("\n"+ nombre)
    print("nombre en la lista prohibida")
    lista.append(nombre)
    for i in lista:
        linea = i.rstrip("\n")
        print(linea)
    file.close()    

    

if __name__=="__main__":

    lista=[]
    print("inicio")

    try:
        archivo = open("listaNombre.txt",'r')
        print("lectura de archivo")
    except:
        archivo = open("listaNombre.txt", "w")
        
    for l in archivo:
    
        linea = l.rstrip("\n")
        lista.append(linea)
        print(linea)

    archivo.close()
    opc = 0
    while opc != 3:
        print("Sistema de validacion de usuarios")
        print("\nIngrese una opcion")
        print("1- comprobar nombre")
        print("2- agregar nombre a la lista")
        print("3- salir")

        opc = input("Igrese una opcion: ")

        if opc == '1':

            nombre = input("ingrese un nombre para la evaluacion: ")
            if validar(nombre) == True:
                valUsuario(nombre, lista)

        elif opc == '2':

            nombre = input("ingrese el nombre que desea agregar a la lista: ")
            if validar(nombre) == True:
                agregar(nombre, lista)
        elif opc =="3":
            print("Hasta pronto")

        else:
            print("la opcion no en una opcion correcta")
