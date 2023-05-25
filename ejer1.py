'''
Ingrese por teclado dos números enteros 
positivos, súmelos y entregue su resultado.
'''
num1=int(input("Ingrese N°1: "))
num2=int(input("Ingrese N°2: "))
if num1>0 and num2>0:
    resultado=num1+num2
    print(f"{num1} + {num2} = {resultado}")
else:
    print("Los números debes ser positivos")
