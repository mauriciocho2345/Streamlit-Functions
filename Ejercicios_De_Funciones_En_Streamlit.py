import streamlit as st

st.title("Hola, Bienvenido a mi Aplicación 😁")
st.header("Tablero Interactivo")

# Crear pestañas para los ejercicios
tabs = st.tabs(["Inicio",
       "Ejercicio 1: Saludar",
        "Ejercicio 2: Suma de dos números",
        "Ejercicio 3: Área de un triángulo",
        "Ejercicio 4: Calculadora de descuento",
        "Ejercicio 5: Suma de una lista de números",
        "Ejercicio 6: Funciones con valores predeterminados",
        "Ejercicio 7: Números pares e impares",
        "Ejercicio 8: Multiplicación con *args",
        "Ejercicio 9: Información de una persona con **kwargs",
        "Ejercicio 10: Calculadora flexible",
        "Acerca De:"])



with tabs[0]:
    st.header("Que tal mucho gusto espero te encuentres muy bien el dia de hoy 😃¿Que te parece si comenzamos a probar los ejercicios?")
    st.header("Para continuar por favor deslice hacia la derecha 👉")
    
 #Ejercicio 1: saludo simple   
with tabs[1]:
    st.header("Te envio un cordial saludo")
    
    def saludo(nombre):
        return f"Hola, {nombre}! 👋"
    
    nombre_input = st.text_input("Puedes Ingresar tu nombre porfis:")
    if nombre_input:
        st.write(saludo(nombre_input))

# Ejercicio 2: Suma de dos números
with tabs[2]:
    st.header("Suma de dos Números")
    
    def sumar(a, b):
        return a + b
    
    num1 = st.number_input("Hola Ingresa el primer número:")
    num2 = st.number_input("Ahora Ingresa el segundo número:")
    if st.button("Calcular Suma"):
        resultado = sumar(num1, num2)
        st.write(f"El resultado de la suma es: {resultado}")

# Ejercicio 3: Cálculo de Área de un Triángulo
with tabs[3]:
    st.header("Cálculo de Área de un Triángulo")
    
    def calcular_area_triangulo(b, a):
        return (b * a) / 2
    
    st.header("Ojo: ambos valores deben ser mayores a cero 👈👀")
    b = st.number_input("Primero Ingresa el valor de la base del triángulo:")
    a = st.number_input("Ahora Ingresa el valor de la altura del triángulo:")
    if st.button("Calcular Área"):
        area = calcular_area_triangulo(b, a)
        st.write(f"El área del triángulo es: {area}")

# Ejercicio 4: Calculadora de Descuento
with tabs[4]:
    st.header("Calculadora de Descuento")
    
    def productos(producto="producto", cantidad=0, precio=0.0, descuento=0.0, impuesto=0.0):
        total = cantidad * precio
        total_descuento = total - (total * (descuento / 100))
        total_impuesto = total_descuento + (total_descuento * (impuesto / 100))
        return (f"{cantidad} {producto}(s) cuestan {total:.2f} pesos. "
                f"Descuento aplicado: {descuento}%. Precio después del descuento: {total_descuento:.2f} pesos. "
                f"Impuesto aplicado: {impuesto}%. Precio final: {total_impuesto:.2f} pesos.")

    st.header("Información del Producto")
    producto_input = st.text_input("Primero Ingresa el nombre del producto:", "producto")
    cantidad_input = st.number_input("Ahora Ingresa la cantidad del producto:", min_value=0, value=0)
    precio_input = st.number_input("Luego Ingresa el precio por unidad:", min_value=0.0, value=0.0, format="%.2f")
    descuento_input = st.number_input("Despues Ingresa el porcentaje de descuento:", min_value=0.0, max_value=100.0, value=0.0, format="%.2f")
    impuesto_input = st.number_input("Finalmente Ingresa el porcentaje de impuesto (opcional):", min_value=0.0, value=0.0, format="%.2f")

    if st.button("Calcular"):
        resultado = productos(producto_input, cantidad_input, precio_input, descuento_input, impuesto_input)
        st.write(resultado)

#Ejercicio 5

def sumar_lista(numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma
with tabs[5]:
    st.header("Suma de una lista de Números")

    number_input = st.text_area("Ingresa los números separados por comas:")

    if st.button("Calcular suma"):
        try:
            num = []
            temp = ""
            
            for char in number_input:
                if char == ',':
                    if temp:  
                        num.append(float(temp.strip()))
                        temp = ""
                else:
                    temp += char  
            
            if temp:
                num.append(float(temp.strip()))
            
            resultado = sumar_lista(num)

            st.write(f"La suma de los números es: {resultado}")
        
        except ValueError:
            st.error("Por favor, asegúrate de que la entrada sea correcta y contenga solo números.")

#Ejercicio 6: 

def producto(nombre, cantidad=1, precio_por_unidad=10):
    total = cantidad * precio_por_unidad
    return f"El total a pagar por {cantidad} unidad de {nombre} es: {total}."

with tabs[6]:  
    st.header("Calculadora de Precio de Productos")

    nombre_producto = st.text_input("Nombre del producto:")
    cantidad = st.number_input("Cantidad por defecto 1:", min_value=1, value=1)
    precio_por_unidad = st.number_input("Precio por unidad $10:", min_value=0.0, value=10.0)

    if st.button("Calcular Precio"):
        
        resultado = producto(nombre_producto, cantidad, precio_por_unidad)
        st.write(resultado)

#Ejercicio 7:


# Función para separar números pares e impares
def numeros_pares_e_impares(lista_numeros):
    pares = []
    impares = []
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares

with tabs[7]:  
    st.header("Separar Números Pares e Impares")

    number_input = st.text_input("Ingresa los números separados por comas:")

    if st.button("Calcular Numeros"):
        try:
            
            lista_numeros = []
            
            numero_temporal = ""

            for char in number_input:
                if char in "0123456789":  
                    numero_temporal += char
                elif char in [',', ' ', '\n']:  
                    if numero_temporal:
                        lista_numeros.append(int(numero_temporal))
                        numero_temporal = ""  

            if numero_temporal:
                lista_numeros.append(int(numero_temporal))

            pares, impares = numeros_pares_e_impares(lista_numeros)

            st.write(f"Números pares: {pares}")
            st.write(f"Números impares: {impares}")
        
        except ValueError:
            st.error("Por favor, asegúrate de ingresar solo números válidos.")

#Ejercicio 8:

def multiplicar_todos(*args):
    if not args:  # Si no se pasan argumentos, devolver 1
        return 1
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

with tabs[8]: 
    st.header("Multiplicación de Números (multiplicar todos los valores)")

    number_input = st.text_input("Ingresa los valores separados por comas:")

    if st.button("Calcular Multiplicación"):
        try:

            lista_numeros = []
            numero_temporal = ""

            # Iterar sobre los caracteres ingresados
            for char in number_input:
                if char in "0123456789.":  
                    numero_temporal += char
                elif char in [',', ' ', '\n']:  
                    if numero_temporal:  
                        lista_numeros.append(float(numero_temporal))
                        numero_temporal = ""  

            if numero_temporal:
                lista_numeros.append(float(numero_temporal))

            resultado = multiplicar_todos(*lista_numeros)
            st.write(f"El resultado de la multiplicación es: {resultado}")

        except ValueError:
            st.error("Por favor, asegúrate de ingresar solo números válidos.")

#Ejercicio 9:

def informacion_personal(**kwargs):
    for clave, valor in kwargs.items():
        st.write(f"{clave}: {valor}")

with tabs[9]:  
    st.header("Información Personal")

    Nombre = st.text_input("Nombre:")
    Genero = st.text_input("Genero.")
    Edad = st.number_input("Edad:", min_value=0, value=0)
    EstadoCivil = st.text_input("Estado Civil:")
    Nacionalidad = st.text_input("Nacionalidad:")
    Direccion = st.text_input("Dirección:")
    Profesion = st.text_input("Profesión:")
    Telefono = st.text_input("Telefono:")

    if st.button("Mostrar Información Personal"):
    
        informacion_personal(Nombre=Nombre, Genero=Genero, Edad=Edad, EstadoCivil=EstadoCivil, Nacionalidad=Nacionalidad, Direccion=Direccion, Profesion=Profesion, Telefono=Telefono )
    

#Ejercicio 10:

def calculadora_flexible(num1, num2, operacion="suma"):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicación":
        return num1 * num2
    elif operacion == "división":
        if num2 != 0:  # Evitar la división por cero
            return num1 / num2
        else:
            return "Error: División por cero."
    else:
        return "Operación no válida."

with tabs[10]:  
    st.header("Calculadora Flexible")

    num1 = st.number_input("Ingresa el primer número:", value=0)
    num2 = st.number_input("Ingresa el segundo número:", value=0)
    operacion = st.selectbox("Selecciona la operación:", ["suma", "resta", "multiplicación", "división"])

    if st.button("Calcular Operacion"):
        resultado = calculadora_flexible(num1, num2, operacion)
        st.write(f"El resultado de la {operacion} es: {resultado}")

#Acerca de:

with tabs[11]:

 if st.button("Mostrar Acerca de"):
    st.header("Esa es una aplicacion que fue desarrollada mediante streamlit, la herramienta que permite facilitar la creacion de aplicaciones web de manera interactiva y sencilla en este caso utilizando el lenguaje de programacion python")

    st.header("El objetivo de esta app es ofrecer a los usuarios el realizar calculos sencillos que a su ves se obtiene la informacion de forma rapida y eficiente gracias a su interfaz, todos los usuarios pueden ingresar los datos que deseen y recibir sus resultados sin coontratiempos")

    st.header("Gracias por Utilizar esta app Espero te sea util 😉❤️")