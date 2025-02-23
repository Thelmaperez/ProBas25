#Problema 28
#Simular una cuenta bancaria con depósitos y retiros


import math 
opciones=["1234", "9874", "0000"]
while True:
    print('''
        Bienvenido - Welcome\n"
        =========================="
        CAJERO AUTOMATICO UDELAS BANK"
        ==========================\n\n"
        Ingrese su PIN sin puntos ni guión\n\n\n"
    ''')
    opcion=input("Introducir PIN: ")
    if not (opcion in opciones):
        print("Este ping no es valido")
        input ("Porfavor pulse para continuar.")
        continue
    if opcion=="1234":
            try:
                print('''                      
                --------------------------"
                |*** Ingreso Correcto ***|"
                --------------------------\n"
                ''')
                print('''
                |*** SELECCIONE TIPO DE OPCION PARA RETIRAR ***|\n"
                [ 1 ] Cuenta Ahorro
                [ 2 ] Cuenta Corriente
                [ 3 ] Cuenta Visa"
                [ 4 ] Salir\n\n"
                ''')
                cuenta=input("Ingrese Opción: ")
                if cuenta == "1":
                    try:
                        print ("Cuenta Ahorro")
                        print ("Introduzca la cantidad en multiplos de 5, Retiro")
                        Retiro=float(input("Ingrese el monto que desee Retirar: -_"))
                        Saldo= 1000 - Retiro
                        print ("Retiro de Cuenta Ahorro por:" , round (Retiro,2 ))
                        print("Su Saldo Actual:",round (Saldo,2))
                        break
                    except:
                        print("Insuficiente Saldo en la cuenta")
                        input ("pulse para continuar.")
                        continue
                if cuenta == "2":
                    try:
                        print ("Cuenta Corriente")
                        print ("Introduzca la cantidad en multiplos de 5, Retiro")
                        Retiro=float(input("Ingrese el monto que desee Retirar: -_"))
                        Saldo= 1000 - Retiro
                        print ("Retiro de Cuenta Ahorro por:" , round (Retiro,2 ))
                        print("Su Saldo Actual:",round (Saldo,2))
                        break
                    except:
                        print("Insuficiente Saldo en la cuenta")
                        input ("pulse para continuar.")
                        continue
                  
                if cuenta == "3":
                    try:
                        print ("Cuenta Visa")
                        print ("Introduzca la cantidad en multiplos de 5, Retiro")
                        Retiro=float(input("Ingrese el monto que desee Retirar: -_"))
                        Saldo= 1000 - Retiro
                        print ("Retiro de Cuenta Ahorro por:" , round (Retiro,2 ))
                        print("Su Saldo Actual:",round (Saldo,2))
                        break
                    except:
                        print("Insuficiente Saldo en la cuenta")
                        input ("pulse para continuar.")
                        continue
                if cuenta == "4":
                    try:
                        print ('''
                Desea cancelar la transaccion?
                Digite numero, sin guiones o simbolos.
                        ''')
                        print ("1. Si?")
                        print ("2. No?")
                        salida=input("Ingrese Opción:")
                        if Salida=="2":
                            print ("Gracias por preferirnos")
                            input ("Pulse para continuar")
                    except:
                        input ("Pulse para continuar")
                        break
            except:
                print("La seleccion no es correcto pulse para continuar.")
                os.system("clear")
                break
        
print ("Fin del Programa")

