import sys


# 8
for i in range(1, 4):
    print(i)

# 9
print(", ".join(str(i) for i in range(1, 10)))

# 10
print(", ".join(str(i) for i in range(1, 10001)))

# 11
print(", ".join(str(i) for i in range(5, 11)))

# 12
print(", ".join(str(i) for i in range(5, 16)))

# 13
print(", ".join(str(i) for i in range(5, 15001, 5)))

# 14
print(", ".join(["hola"] * 200))

# 15
print(", ".join(str(i**2) for i in range(1, 31)))

# 16
resultado = 1
for i in range(1, 21):
    resultado *= i
print(resultado)

# 17
suma_cuadrados = sum(i**2 for i in range(1, 101))
print(suma_cuadrados)


n = int(input("Ingrese un número: "))
suma_100 = sum(range(n + 1, n + 101))
print("Suma de los 100 números siguientes:", suma_100)

#euros a dolares
euros = float(input("Ingrese cantidad en euros: "))
tasa_cambio = 1.1  
dolares = euros * tasa_cambio
print("Cantidad en dólares:", dolares)

#rectangulo
altura = float(input("Ingrese la altura del rectángulo: "))
anchura = float(input("Ingrese la anchura del rectángulo: "))
area = altura * anchura
print("Área del rectángulo:", area)

#mayor y menor
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
if a > b:
    print(f"Mayor: {a}, Menor: {b}")
elif b > a:
    print(f"Mayor: {b}, Menor: {a}")
else:
    print("Ambos números son iguales")

#menores impares
num = int(input("Ingrese un número entero: "))
for i in range(1, num, 2):
    print(i)

#euclides mcd
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print("Máximo común divisor:", mcd(num1, num2))

#cuadratica
import math
a = float(input("Ingrese coeficiente a: "))
b = float(input("Ingrese coeficiente b: "))
c = float(input("Ingrese coeficiente c: "))
discriminante = b**2 - 4*a*c
if discriminante < 0:
    print("La ecuación no tiene soluciones reales")
elif discriminante == 0:
    x = -b / (2*a)
    print("Solución única:", x)
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("Soluciones:", x1, "y", x2)

# 25
sys.setrecursionlimit(3000)  

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def ackermann(m, n):
    if m < 0 or n < 0:
        raise ValueError("Los valores de Ackermann deben ser no negativos.")
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

try:
    n = int(input("Ingrese un número para calcular factorial: "))
    print("Factorial:", factorial(n))

    m = int(input("Ingrese m para Ackermann: "))
    n = int(input("Ingrese n para Ackermann: "))
    print("Ackermann:", ackermann(m, n))

except ValueError as e:
    print("Error:", e)
except RecursionError:
    print("Error: La recursión es demasiado profunda. Prueba con valores más pequeños.")

#26
nums = [int(input("Ingrese un número entero positivo: ")) for _ in range(3)]
print("Menor:", min(nums), "Mayor:", max(nums))

#27
while True:
    f = float(input("Ingrese temperatura en Fahrenheit (999 para salir): "))
    if f == 999:
        break
    c = (5/9) * (f - 32)
    print("Temperatura en Celsius:", c)

#29 menu diccionario
opciones = {1: "Opción 1", 2: "Opción 2", 3: "Opción 3"}
seleccion = int(input("Ingrese una opción (1-3): "))
print(opciones.get(seleccion, "Opción no válida"))

# 29
import sys
print("Ingrese datos, presione Ctrl+D (Linux/Mac) o Ctrl+Z (Windows) para terminar:")
for linea in sys.stdin:
    print("Ingresado:", linea.strip())

#primos con bucles anidados
for num in range(2, 101):
    es_primo = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    if es_primo:
        print(num)
