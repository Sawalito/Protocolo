prot = []
def protocolo():
    op=0
    print("---------------Menu---------------------")
    print("1.-Agregar instrucción")
    print("2.-Agregar subpaso")
    print("3.-Borrar paso")
    print("4.-Borrar subpaso")
    print("5.-Modificar paso")
    print("6.-Imprimir protocolo")
    print("7.-Salir")
    op=int(input("Introducir el numero de la opcion "))
    sp = []
    if op==1:
        ins = input("Introducir el paso ")
        sp.append(ins)
        prot.append(sp)
        sp=[]
        protocolo()
    if op==2:
        ins=input("Introducir el subpaso ")
        prot[-1].append(ins)
        protocolo()
    if op==3:
        pos=int(input("Introduce el paso que quieres borrar "))
        prot.pop(pos-1)
        protocolo()
    if op==4:
        posb=int(input("Introduce el paso que contiene al subpaso "))
        pos=int(input("Introduce el subpaso que quieres borrar "))
        prot[posb-1].pop(pos-1)
        protocolo()
    if op==5:
        pos=int(input("Introduce el paso que quieres modificar "))
        ins=input("Introduce el paso modificado ")
        prot[pos-1][0] = ins
        protocolo()
    if op==6:
        print("---------------------------------------------")
        for i in range(1,len(prot)+1):
            print(str(i)+".-"+prot[i-1][0])
            for j in range(1,len(prot[i-1])):
                print(str(i)+"."+str(j)+".-"+prot[i-1][j-1])
                print("---------------------------------------------")   
        print("---------------------------------------------")
        protocolo()
        

protocolo()
        



    
        

    
