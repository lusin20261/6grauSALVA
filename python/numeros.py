print("===========BIENBENIDO A MI CALCULADORA===========")
import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def potencia(base, exponente):
    return base ** exponente

def radicacion(numero, raiz=2):
    if numero < 0 and raiz % 2 == 0:
        return "Error: No se puede extraer raíz par de número negativo"
    return numero ** (1 / raiz)

def calculadora():
    print("Seleccione operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Radicación")
    
    opcion = input("Opción: ")
    num1 = float(input("Primer número: "))
    
    if opcion == '5':
        num2 = float(input("Exponente: "))
        print(f"Resultado: {potencia(num1, num2)}")
    elif opcion == '6':
        num2 = float(input("Índice de la raíz: "))
        print(f"Resultado: {radicacion(num1, num2)}")
    else:
        num2 = float(input("Segundo número: "))
        if opcion == '1': print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == '2': print(f"Resultado: {restar(num1, num2)}")
        elif opcion == '3': print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == '4': print(f"Resultado: {dividir(num1, num2)}")
        else: print("Opción no válida")

if __name__ == "__main__":
    calculadora()