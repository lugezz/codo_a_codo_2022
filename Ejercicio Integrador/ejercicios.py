
# 1. Escribir una función que calcule el máximo común divisor entre dos números.

def get_divisores(numero):
    resp = []
    if numero == 1:
        resp = [1]

    for i in range(2, numero + 1):
        if numero % i == 0:
            resp.append(i)
            resp += get_divisores(int(numero / i))
            break

    return resp


def orden_resultados(list_resultados):
    counts = dict()
    for i in sorted(list_resultados):
        counts[i] = counts.get(i, 0) + 1

    return counts


def maximo_comun_divisor(num1, num2):
    divisor = 1
    veces = 1

    if min(num1, num2) < 1:
        print('Ingrese 2 numeros positivos')
        return -1

    divisores1 = orden_resultados(get_divisores(num1))
    divisores2 = orden_resultados(get_divisores(num2))

    for i in divisores1:
        if i in divisores2:
            divisor = i
            veces = min(divisores1[i], divisores2[i])

    return divisor ** veces


try:
    numero1a = int(input("Ingrese el número 1: "))
    numero2a = int(input("Ingrese el número 2: "))
    respuesta = maximo_comun_divisor(numero1a, numero2a)
    if respuesta > 0:
        print(f'El Máximo Común Divisor entre {numero1a} y {numero2a} es {respuesta} ')

except Exception:
    print("Ingrese números correctos")


# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
print("*" * 100)


def minimo_comun_multipo(num1, num2):
    respuesta = 1

    if min(num1, num2) < 1:
        print('Ingrese 2 numeros positivos')
        return -1

    divisores1 = orden_resultados(get_divisores(num1))
    divisores2 = orden_resultados(get_divisores(num2))
    maximo_divisor = max(list(divisores1)[-1], list(divisores2)[-1])

    for i in range(1, maximo_divisor + 1):
        respuesta *= (i ** max(divisores1.get(i, 0), divisores2.get(i, 0)))

    return respuesta


try:
    numero1b = int(input("Ingrese el número 1: "))
    numero2b = int(input("Ingrese el número 2: "))
    respuesta2 = minimo_comun_multipo(numero1b, numero2b)
    if respuesta2 > -10:
        print(f'El Mínimo Común Múltipo entre {numero1b} y {numero2b} es {respuesta2} ')

except Exception:
    print("Ingrese números correctos")


# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).


# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.


# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.


# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.


# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.


# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.
