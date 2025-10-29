from operaciones import *
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print('El numero ingresado no es valido')

def main():
    continuar = "s"

    while continuar == "s":
        print("\n--- Calculadora ---")
        a = pedir_numero("Introduzca el primer numero: ")
        b = pedir_numero("Introduzca el segundo numero: ")

        print("\n¿Qué operación deseas realizar?")
        print("1: Suma")
        print("2: Resta")
        print("3: Multiplicacion")
        print("4: Division")

        opcion = input("Elige (1-4): ")
        if opcion == "1":
            resultado = suma(a, b)
        elif opcion == "2":
            resultado = resta(a, b)
        elif opcion == "3":
            resultado = multiplicacion(a, b)
        elif opcion == "4":
            resultado = division(a, b)
        else:
            print("Opción no válida")
            continue

        print(f"Resultado: {resultado}")

        continuar = input("\¿Desea realizar otra operación? (s/n): ")

    print("\nPrograma finalizado")

if __name__ == '__main__':
    main()