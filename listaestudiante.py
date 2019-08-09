
lista=[]
while True:
    agregar=input()
    if agregar=="1": 
        estudiante=input("name")
        lista.append(estudiante)
    elif agregar=="2":
        print(lista)
        opcion=int(input("otra"))
        lista.pop=(opcion)
    elif agregar=="3": 
        break
print(lista)
