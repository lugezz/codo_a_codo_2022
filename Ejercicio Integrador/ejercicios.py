
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

print("*" * 100)


# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números

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

print("*" * 100)

# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

texto = "Es un teatro de temporada o de stagione que renueva su programación anualmente, no un teatro de repertorio. Asimismo es un teatro de producción propia, que cuenta con talleres  especializados para realizar todos los elementos necesarios para la escenificación de un  espectáculo de ópera o ballet."

texto_lista = texto.split()
texto_diccionario = orden_resultados(texto_lista)

print("Ejercicio 3", texto_diccionario)
print("*" * 100)

# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.


def get_mas_repetido(mi_diccionario):
    resultado = ("", 0)
    for k, v in mi_diccionario.items():
        if v > resultado[1]:
            resultado = (k, v)

    return resultado


print("Ejercicio 4", get_mas_repetido(texto_diccionario))
print("*" * 100)

# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.

es_entero = False


def get_int(numero):
    global es_entero
    respuesta = 0
    try:
        respuesta = int(numero)
        es_entero = True

    except ValueError:
        print("Ingreso incorrecto, intente nuevamente")

    return respuesta


while not es_entero:
    ingreso = input('Ingrese un número: ')
    valor = get_int(ingreso)


print("Ejercicio 5: Ingresaste el valor", valor)
print("*" * 100)

# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.


class Persona:

    def __init__(self, nombre="", edad=0, DNI=""):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def DNI(self):
        return self.__DNI

    def validar_nombre(self):
        # Máximo largo 100 caracteres
        if len(self.__nombre) > 100:
            print('Nombre Incorrecto!')
            self.__nombre = ""

    def validar_edad(self):
        if self.__edad < 0:
            print('Edad Incorrecta!')
            self.__edad = 0

    def validar_DNI(self):
        # Debe tener 7 a 9 caracteres
        if len(self.__DNI) < 7 or len(self.__DNI) > 9:
            print('DNI Incorrecto!')
            if len(self.__DNI) < 7:
                self.__DNI = f'{"0" * (8 - len(self.__DNI))}{self.__DNI}'
            else:
                self.__DNI = self.__DNI[:8]

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        self.validar_nombre()

    @edad.setter
    def edad(self, edad):
        self.__edad = edad
        self.validar_edad()

    @DNI.setter
    def DNI(self, DNI):
        self.__DNI = DNI
        self.validar_DNI()

    def mostrar(self):
        return f'Mi nombre es {self.nombre}, DNI: {self.DNI} y tengo {self.edad} años'

    def es_mayor_de_edad(self):
        return self.edad >= 18


personilla = Persona("Juan", 22, "3232")
print("Ejercicio 6:")
print(personilla.mostrar())
print("*" * 100)

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


class Cuenta():

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    def mostrar(self):
        print(f'Titular: {self.titular.mostrar()} | Su cantidad es {self.cantidad}')

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad


cuentilla = Cuenta(personilla, 100)
cuentilla.ingresar(400)
cuentilla.retirar(10)
print("Ejercicio 7:")
cuentilla.mostrar()
print("*" * 100)

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


class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def mostrar(self):
        print(f'Cuenta Joven: Su cantidad es {self.cantidad} - Su bonificación es {self.bonificacion}%')

    def es_valido_titular(self):
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25

    def retirar(self, cantidad):
        if not self.es_valido_titular():
            mensaje = "estás viejito" if self.titular.edad >= 25 else "sos un niño"
            print(f'No puedes retirar, {mensaje}')

        else:
            super().retirar(cantidad)


cuentilla_joven = CuentaJoven(personilla, bonificacion=20)
cuentilla_joven.ingresar(1300)
cuentilla_joven.retirar(128)

print("Ejercicio 8:")
cuentilla_joven.mostrar()
