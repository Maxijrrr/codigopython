import os
os.system('cls')
def solicitar_numeros():
    while True:
        try:
            a=int(input("Ingrese el primero número: "))
            break
        except ValueError:
            print("Error, debe ingresar un número")

    while True:
        try:
            b=int(input("Ingrese el primero número: "))
            break
        except ValueError:
            print("Error, debe ingresar un número")
    return a,b
def sumar(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def dividir(a,b):
    try:
        dividir=round(a/b)
        return dividir
            
        
    except ZeroDivisionError:
        print("La división por cero no está definida")
        
def menu():
    while True:
        try:
            print("----- Calculadora -----")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            op=int(input("Ingrese opción: "))
            if op == 1:
                a,b=solicitar_numeros()
                print(f"La suma es: {sumar(a,b)}")
            
            elif op == 2:
                a,b=solicitar_numeros()
                print(f"La resta es: {resta(a,b)} ")

            elif op == 3:
                a,b=solicitar_numeros()
                print(f"La multiplicación es: {multiplicacion(a,b)}")


            elif op == 4:
                a,b=solicitar_numeros()
                if dividir(a,b) != None:
                   print(f"La división de los números es: {dividir(a,b)}")
                
                


            elif op == 5:
                print("Adiós")
                break



        except ValueError:
            print("Error, debe ingresar un número entero")
menu()