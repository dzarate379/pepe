
lista = []
while True :
    try  :
        agregar-nombre-Estudiante= input("Nombre = ")
        break
    except :
        print ('solo letras')

lista.extend (agregar-nombre-Estudiante)
print(lista)
