while True :
    try  :
        salario= int(input("salario = "))
        break
    except :
        print ('digite numero')
empleador=0.30
trabajador=0.10
total = int((salario*trabajador)+(salario*empleador))
print("total seria", total)