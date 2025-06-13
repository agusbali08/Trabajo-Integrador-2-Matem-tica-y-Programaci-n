#OPERACIONES CON DNIS
# Williams Exequiel Cantero: 41479713
# Agustin Baliño: 43719110
# Jose Juan Abad: 42403529

# Lista de DNIs (por ahora con uno ficticio)
dnis = ['42403529', '43719110', '41479713']

# Generamos los conjuntos de dígitos únicos
conjuntos = []
for dni in dnis:
    conjuntos.append(set(dni))

# Mostramos los conjuntos
for i, conjunto in enumerate(conjuntos):
    print(f"Conjunto {i+1}: {sorted(conjunto)}")

A = conjuntos[0]
B = conjuntos[1]
C = conjuntos[2]

# Unión
union_AB = A | B
union_AC = A | C
union_BC = B | C

# Intersección
interseccion_AB = A & B
interseccion_AC = A & C
interseccion_BC = B & C

# Diferencia
diferencia_AB = A - B
diferencia_AC = A - C
diferencia_BC = B - C

# Diferencia simétrica
difsim_AB = A ^ B
difsim_AC = A ^ C
difsim_BC = B ^ C

# Mostrar resultados
print("\nOperaciones entre A y B:")
print("Unión:", sorted(union_AB))
print("Intersección:", sorted(interseccion_AB))
print("Diferencia (A - B):", sorted(diferencia_AB))
print("Diferencia Simétrica:", sorted(difsim_AB))

print("\nOperaciones entre A y C:")
print("Unión:", sorted(union_AC))
print("Intersección:", sorted(interseccion_AC))
print("Diferencia (A - C):", sorted(diferencia_AC))
print("Diferencia Simétrica:", sorted(difsim_AC))

print("\nOperaciones entre B y C:")
print("Unión:", sorted(union_BC))
print("Intersección:", sorted(interseccion_BC))
print("Diferencia (B - C):", sorted(diferencia_BC))
print("Diferencia Simétrica:", sorted(difsim_BC))

#Frecuencia de dígitos en cada DNI

for i, dni in enumerate(dnis):
    print(f"\nDNI {i+1}: {dni}")
    for digito in '0123456789':
        frecuencia = dni.count(digito)
        if frecuencia > 0:
            print(f"Dígito {digito}: {frecuencia} vez/veces")

#Suma total de dígitos de cada DNI

for i, dni in enumerate(dnis):
    suma = sum(int(d) for d in dni)
    print(f"DNI {i+1}: suma total de dígitos = {suma}")

#Si algún conjunto tiene más de 6 elementos, mostrar "Diversidad numérica alta".

for i, conjunto in enumerate(conjuntos):
    if len(conjunto) > 6:
        print(f"Conjunto {i+1}: Diversidad numérica alta (tiene {len(conjunto)} elementos)")
    else:
        print(f"Conjunto {i+1}: Diversidad numérica baja (tiene {len(conjunto)} elementos)")

#Si un dígito aparece en todos los conjuntos, mostrar "Dígito compartido".

interseccion_total = conjuntos[0]
for conjunto in conjuntos[1:]:
    interseccion_total = interseccion_total & conjunto

if interseccion_total:
    print("Dígitos compartidos en todos los conjuntos:", sorted(interseccion_total))
else:
    print("No hay dígitos compartidos en todos los conjuntos")

#Si ningún conjunto tiene el número 0, entonces se considera un grupo sin ceros.·    

contiene_cero = False

for conjunto in conjuntos:
    if '0' in conjunto:
        contiene_cero = True

if contiene_cero:
    print("Hay al menos un conjunto con el dígito 0")
else:
    print("Grupo sin ceros")

#AÑOS DE NACIMIENTO:
# Williams Exequiel Cantero: 1998 
# Agustin Baliño: 2001
# Jose Juan Abad: 2000


def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return  True
    else:
        return False

#PROGRAMA PRINCIPAL 
print("Operaciones con años de nacimiento")
print("")
cantidad_de_integrantes = int(input("Ingrese la cantidad de integrantes del grupo: "))

#Pedimos años de nacimiento
años_de_nacimiento = []
for i in range(cantidad_de_integrantes):
    año = int(input(f"Ingresa el año de nacimiento del integrante {i+1}: "))
    if año in años_de_nacimiento:
        print("Ese año ya esta en la lista. Ingresa uno ficticio")
        año = int(input())
    años_de_nacimiento.append(año)

#Contar cuantos nacieron en año par e impar
cont_par = 0
cont_impar= 0
for año in años_de_nacimiento:
    if año % 2 == 0:
        cont_par += 1
    else: 
        cont_impar += 1    

print(f"{cont_par} nacieron en año par")
print(f"{cont_impar} nacieron en año impar")

#Verificar si el grupo es generacion z
generacionZ = True
for año in años_de_nacimiento:
    if año < 2000:
        generacionZ = False
        break

if generacionZ:
    print("Grupo Z")

#Ver si alguno nacio en año biciesto
especial = False 
for año in años_de_nacimiento:
    if es_bisiesto(año):
        especial = True
        break

if especial:
    print("Tenemos un año especial")

#Edades actuales
año_actual = 2025
edades =[]
for año in años_de_nacimiento:
    edades.append(año_actual - año)
print (edades)

#Producto Cartesiano de años de nacimiento y edades.
producto_cartesiano = []
for año in años_de_nacimiento:
    for edad in edades:
        producto_cartesiano.append((año, edad))
print(producto_cartesiano)