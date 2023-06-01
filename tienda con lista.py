compra=[]
cuantos=[]
cant=0
ops=0
total=0
cont=0
while ops!=1:
    while True:
        totalproducto=0
        print("*"*30,"\n\tminimarket D'todito\n","*"*30)
        print("1.- leche $1000\n2.- galletas $1500\n3.- cocacola $2000\n4.- gomitas $1100\n5.- aceite $3000\n6.- Ver carrito")
        print("-"*30)
        try:
            selec=int(input("seleccione algun producto: "))
            if 1<= selec <=6:
                if selec==1:
                    cant=int(input("cuantos quiere: "))
                    totalproducto+=cant*1000
                    total+=totalproducto
                    cont+=1
                    compra.append(f"leche. ${totalproducto}")
                    cuantos.append(cant)
                elif selec==2:
                    cant=int(input("cuantos quiere: "))
                    totalproducto+=cant*1500
                    total+=totalproducto
                    cont+=1
                    compra.append(f"galletas. ${totalproducto}")
                    cuantos.append(cant)
                elif selec==3:
                    cant=int(input("cuantos quiere: "))
                    totalproducto+=cant*2000
                    total+=totalproducto
                    cont+=1
                    compra.append(f"cocacola. ${totalproducto}")
                    cuantos.append(cant)
                elif selec==4:
                    cant=int(input("cuantos quiere: "))
                    totalproducto+=cant*1100
                    total+=totalproducto
                    cont+=1
                    compra.append(f"gomitas. ${totalproducto}")
                    cuantos.append(cant)
                elif selec==5:
                    cant=int(input("cuantos quiere: "))
                    totalproducto+=cant*3000
                    total+=totalproducto
                    cont+=1
                    compra.append(f"aceite. ${totalproducto}")
                    cuantos.append(cant)
                else:
                    if total==0:
                        print("*"*30,"\n\tcarrito\n","*"*30,"\nNo tienes nada agregadoo!!\n\n\n")
                    else:
                        break
            else:
                print("solo del 1 al 5!!")
        except:
            print("solo numeros")
    while True:
        cont2=0
        print("*"*30,"\n\tcarrito\n","*"*30)
        for i in range(cont):
            print(cuantos[cont2],compra[cont2])
            cont2+=1
        print("-"*30,"\nque quiere hacer?\n1.- ver total a pagar.\n2.-volver al menu.\n\n\n")
        try:
            selec=int(input("seleccione una opcion: "))
            if 1<= selec <=2:
                if selec==1:
                    todo=0
                    for i in cuantos:
                        todo+=i
                    print("*"*30,"\n\tboleta\n","*"*30)
                    print(f"los productos a pagar son: {todo}\n\ntotal a pagar es: {total}\n\nMuchas gracias por tu compra!!\n","*"*30)
                    ops=1
                    break
                else:
                    break
            else:
                print("solo del 1 al 2!!")
        except:
            print("solo numeros")
