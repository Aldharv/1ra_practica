''' Tipos de datos en Python

int -- se utiliza para numeros enteros y cuando se van hacer operaciones matematicas como suma, resta, multiplicacion, division
float -- se utiliza cuando se quiere trabajar con numeros con punto decimal
str -- se utiliza cuando se quiere almacenar cadena de caracteres '''

x = 5      # Ejemplo de una variable tipo entero
y = 3.5    # Ejemplo de una variable tipo flotante
z = 'Hola' # Ejemplo de una variable tipo string

# El metodo casteo permite cambiar el tipo de una variable
w = str(x)
print(w)

# Condicionales en Python
# If es un condicional que solo ejecuta la parte del codigo si se cumple su funcion

n = 18
if n >= 18:                 # en esta parte el codigo verifica si se cumple la condicion
    print("Mayor de edad")  # si la condicion se cumple, esta linea se ejecutara, de lo contrario saltara a la siguiente linea

# Elif es un condicional el cual primero verifica que las anteriores condiciones no se hayan cumplido, despues verifica su condicion

r = 'Mexico'
if r == 'Canada':            # en esta parte el codigo verifica si se cumple la condicion
    print("Pais incorrecto") # solo se ejecutara si se cumple la condicion anterior
elif r == "Mexico":          # si la condicion anterior no se cumple, verifica su condicion
    print('Bienvenido')      # solo se ejecutara si no se cumplio la primera condicion y se cumplio la segunda condicion

# Else condicional el cual solo se ejecutara si ninguna de las condciones anteriores se han cumplido o se cumplieron

c = 7
if c <= 5:
    print('Insuficiente')
elif c == 6:
    print('Reprobado')
elif c == 7:
    print('Aprobado')
else:
    print('Formato incorrecto')  # Si ninguna de todas las condiciones anteriores se cumplio, por ultimo se ejecutara el else 
