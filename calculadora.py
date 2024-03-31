#CALCULADORA BÁSICA EN PYTHON

while True:
    print(" ________________________________ ")
    print("|                                |")
    print("|       CALCULADORA BÁSICA       |")
    print("|________________________________|")

    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        num1 = float(input("Ingresa el primer numero a sumar: "))
        num2 = float(input("Ingresa el segundo numero a sumar: "))
        resultado = num1 + num2
        print("EL RESULTADO DE LA SUMA ES: ", resultado)
      

    elif opcion == "2":
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        print("EL RESULTADO DE LA RESTA ES: ", num1 - num2)
       

    elif opcion == "3":
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
      
        print("EL RESULTADO DE LA MULTIPLICACIÓN ES: ", num1 * num2)

    elif opcion == "4":
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        
        print("EL RESULTADO DE LA DIVISIÓN ES: ", num1 / num2)

    elif opcion == "5":
        print("Adios, vuelva pronto.")
        break
    else:
        print("opcion no valida")
        print("Intente de nuevo")
