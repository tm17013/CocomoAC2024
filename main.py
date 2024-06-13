def bienvenida():
    print("************************************************************")
    print("*             Calculadora de COCOMO                        *")
    print("*       Analisis de Costos Informaticos 2024               *")
    print("*    Creado por: Kenia Tepas y  Victoria Castro            *")
    print("************************************************************\n")

#calculo de KLDC por medio de PFA
def obtener_kldc_por_puntos_funcion():
    puntos_funcion = float(input("Ingrese los puntos de función (PF) de su proyecto: "))
    ldc_por_pf = float(input("Ingrese las líneas de código (LDC) por cada punto de función (PF): "))
    ldc = puntos_funcion * ldc_por_pf
    kldc = ldc / 1000
    print(f"La cantidad de KLDC es: {kldc:.4f}")
    return kldc

#conversion de LDC por KLDC
def obtener_kldc_por_ldc():
    ldc = float(input("Ingrese la cantidad de líneas de código (LDC) de su proyecto: "))
    kldc = ldc / 1000
    print(f"La cantidad de KLDC es: {kldc:.4f}")
    return kldc

#calculo de E en modelo basico
def calcular_esfuerzo_basico(kldc, modo):
    if modo == 'Organico':
        esfuerzo = 2.4 * (kldc ** 1.05)
    elif modo == 'Semi-acoplado':
        esfuerzo = 3.0 * (kldc ** 1.12)
    elif modo == 'Acoplado':
        esfuerzo = 3.6 * (kldc ** 1.20)
    else:
        esfuerzo = None
    return esfuerzo

#calculo de tiempo en meses segun el modo, modelo basico
def calcular_tdev(esfuerzo, modo):
    if modo == 'Organico':
        tdev = 2.5 * (esfuerzo ** 0.38)
    elif modo == 'Semi-acoplado':
        tdev = 2.5 * (esfuerzo ** 0.35)
    elif modo == 'Acoplado':
        tdev = 2.5 * (esfuerzo ** 0.32)
    else:
        tdev = None
    return tdev

#calculo de personas 
def calcular_numero_personas(esfuerzo, tdev):
    return esfuerzo / tdev

#calculo del costo 
def calcular_costo(numero_personas, tdev):
    salario = float(input("Ingrese el salario por persona para calcular costo del proyecto (mensual): $"))
    costo = numero_personas * salario * tdev
    return costo

#seleccionar modo
def seleccionar_tipo_proyecto():
    print("\nSeleccione el tipo de proyecto:")
    print("1. Orgánico")
    print("2. Semi-acoplado")
    print("3. Acoplado (Empotrado)")
    tipo = input("Ingrese su elección: ")
    if tipo == '1':
        return 'Organico'
    elif tipo == '2':
        return 'Semi-acoplado'
    elif tipo == '3':
        return 'Acoplado'
    else:
        print("Opción no válida.")
        return seleccionar_tipo_proyecto()

#calculo de EAF en el modelo Intermedio
def obtener_eaf():
    print("Ingrese los multiplicadores de esfuerzo:")
    rely = float(input("RELY (fiabilidad requerida del software): "))
    data = float(input("DATA (tamaño de la base de datos): "))
    cplx = float(input("CPLX (complejidad del producto): "))
    time = float(input("TIME (constricciones temporales): "))
    stor = float(input("STOR (restricciones de almacenamiento): "))
    virt = float(input("VIRT (volatilidad de la máquina virtual): "))
    turn = float(input("TURN (tiempo de respuesta): "))
    acap = float(input("ACAP (capacidad del analista): "))
    aexp = float(input("AEXP (experiencia del analista): "))
    pcap = float(input("PCAP (capacidad del programador): "))
    vexp = float(input("VEXP (experiencia en la máquina virtual): "))
    lexp = float(input("LEXP (experiencia en el lenguaje): "))
    modp = float(input("MODP (uso de herramientas de software modernas): "))
    tool = float(input("TOOL (uso de herramientas de software): "))
    sced = float(input("SCED (restricción de planificación): "))
    
    eaf = rely * data * cplx * time * stor * virt * turn * acap * aexp * pcap * vexp * lexp * modp * tool * sced
    print(f"El Factor de Ajuste del Esfuerzo (EAF) es: {eaf}")
    return eaf 

#calculo de E en el modelo Intermedio
def calcular_esfuerzo_intermedio(kldc, eaf, modo):
    if modo == 'Organico':
        esfuerzo_nominal = 3.2 * (kldc ** 1.05)
        esfuerzo_ajustado = esfuerzo_nominal * eaf
    elif modo == 'Semi-acoplado':
        esfuerzo_nominal = 3.0 * (kldc ** 1.12)
        esfuerzo_ajustado = esfuerzo_nominal * eaf
    elif modo == 'Acoplado':
        esfuerzo_nominal = 2.8 * (kldc ** 1.20)
        esfuerzo_ajustado = esfuerzo_nominal * eaf
    else:
        esfuerzo_ajustado = None
    return esfuerzo_ajustado

#COCOMO2 MODELO1
def calcular_puntos_objeto():
    pantallas = int(input("\n¿Cuántas pantallas tiene tu proyecto? "))
    reportes = int(input("¿Cuántos reportes tiene tu proyecto? "))
    componentes_3gl = input("¿Los componentes de software son 3GL? (si/no): ")

    if componentes_3gl.lower() == "no":
        print("Lo siento, el software no es apto para el cálculo de COCOMO II.")
        return None
    componentes = 1 if componentes_3gl.lower() == "si" else 0
    peso_componentes = 10 if componentes_3gl.lower() == "si" else 0

    peso_pantallas = 1 if pantallas <= 5 else (2 if pantallas <= 8 else 3)
    peso_reportes = 2 if reportes <= 5 else (5 if reportes <= 8 else 8)

    puntos_objeto = pantallas * peso_pantallas + reportes * peso_reportes + componentes* peso_componentes
    print("\nPuntos Objeto (PO):", puntos_objeto)
    return puntos_objeto

def calcular_nuevos_puntos_objeto(puntos_objeto):
    while True:
        reuso = input("\n¿Conoces el % de reuso? (si/no): ").lower()
        
        if reuso == "no":
            puntos_reutilizables = int(input("¿Cuántos de los puntos objeto (PO) son componentes que pueden reutilizarse de proyectos anteriores? "))
            porcentaje_reuso = (puntos_reutilizables / puntos_objeto) * 100
            break
        elif reuso == "si":
            porcentaje_reuso = float(input("Ingrese el % de reuso (número entero sin %): "))
            break
        else:
            print("Opción inválida. Por favor, seleccione 'si' o 'no'.")

    nuevos_puntos_objeto = puntos_objeto * (100 - porcentaje_reuso) / 100
    print("\nNuevos Puntos Objeto (NOP):", nuevos_puntos_objeto)
    return nuevos_puntos_objeto

def esfuerzo_modelo1(nuevos_puntos_objeto, productividad_promedio=None):
    if productividad_promedio:
        prod = productividad_promedio
    else:
        experiencia = input("¿Cuál es la experiencia y capacidad de los desarrolladores? (muy bajo, bajo, normal, alto, muy alto): ")
        if experiencia.lower() == "muy bajo":
            prod = 4
        elif experiencia.lower() == "bajo":
            prod = 7
        elif experiencia.lower() == "normal":
            prod = 13
        elif experiencia.lower() == "alto":
            prod = 25
        elif experiencia.lower() == "muy alto":
            prod = 50
        else:
            print("Experiencia no reconocida. Se usara valor de experiencia normal.")
            prod = 13  #experiencia normal
    
    esfuerzo = nuevos_puntos_objeto / prod
    print("\nEsfuerzo (PM):", esfuerzo)

#FIN COCOMO2 MODELO1

#COCOMO2-MODELO2

#factor exponencial de escala
def exponente_b():
    print("\nIngrese los 5 factores de escala para B (valores entre 1.00 y 5.00):")
    prec = float(input("1-Precedentes (PREC): "))
    flex = float(input("2-Desarrollo (FLEX): "))
    resl = float(input("3-Arquitectura y resolución de riesgo (RESL): "))
    team = float(input("4-Cohesión de equipo (TEAM): "))
    pmat = float(input("5-Madurez del proceso (PMAT): "))
    
    suma_factores = prec + flex + resl + team + pmat
    b = 1.01 + 0.01 * suma_factores
    print(f"\nEl valor de B es: {b:.4f}")

    if b < 1.0:
        print("El proyecto exhibe economía de escala.")
    elif b == 1.0:
        print("Las economías y desconomías de escala están en equilibrio.")
    else:
        print("El proyecto muestra deseconomía de escala.")
    
    return b

#calculo de esfuerzo nominal- PM nominal
def esfuerzo_nominal_diseno_temprano(kldc, b):
    esfuerzo_nominal = 2.94 * (kldc ** b)
    print(f"\nEsfuerzo nominal (PM_nominal): {esfuerzo_nominal:.4f} personas-mes")
    return esfuerzo_nominal

#calculo de factores de costo
def eaf_diseno_temprano():
    print("\nIngrese los 7 multiplicadores de esfuerzo (EMi):")
    rucx = float(input("1-RCPX (complejidad del producto): "))
    ruse = float(input("2-RUSE (reutilización del software): "))
    pdif = float(input("3-PDIF (dificultad de la plataforma): "))
    pers = float(input("4-PERS (capacidad del personal): "))
    prex = float(input("5-PREX (experiencia del personal): "))
    fcil = float(input("6-FCIL (facilidad de la plataforma): "))
    sced = float(input("7-SCED (restricciones de planificación): "))
    
    eaf = rucx * ruse * pdif * pers * prex * fcil * sced
    print(f"\nEl Factor de Costo o Multiplicador de esfuerzo (EM) es: {eaf}")
    return eaf

#calculo de PM estimado
def esfuerzo_estimado_diseno_temprano(esfuerzo_nominal, eaf):
    esfuerzo_estimado = esfuerzo_nominal * eaf
    print(f"Esfuerzo estimado (PM_estimado): {esfuerzo_estimado:.2f} personas-mes")
    return esfuerzo_estimado

def cocomo_2_diseno_temprano():
    kldc = float(input("\nIngrese la cantidad de KLDC de su proyecto: "))
    b = exponente_b()
    esfuerzo_nominal = esfuerzo_nominal_diseno_temprano(kldc, b)
    eaf = eaf_diseno_temprano()
    print("\nRESULTADO PM ESTIMADO:")
    esfuerzo_estimado = esfuerzo_estimado_diseno_temprano(esfuerzo_nominal, eaf)
    print("\nCALCULO DE TDEV, N° PERSONAS y COSTO de proyecto: ")
    #calculo de tdev, personas y costo dependiendo del usuario
    while True:
        calcular_detalles = input("¿Desea calcular el TDEV, número de personas y costo del proyecto? (si/no): ").lower()
        
        if calcular_detalles == 'si':
            tipo_proyecto = seleccionar_tipo_proyecto()
            tdev = calcular_tdev(esfuerzo_estimado, tipo_proyecto)
            numero_personas = calcular_numero_personas(esfuerzo_estimado, tdev)
            costo = calcular_costo(numero_personas, tdev)
            
            if esfuerzo_estimado and tdev and numero_personas and costo:
                print("\nRESULTADOS:")
                print(f"El esfuerzo estimado (PM) es: {esfuerzo_estimado:.2f} persona-meses")
                print(f"El tiempo de desarrollo estimado (TDEV) es: {tdev:.2f} meses")
                print(f"El número de personas necesarias es: {numero_personas:.2f}")
                print(f"El costo total estimado es: $ {costo:.2f}")
            else:
                print("Hubo un error en el cálculo.")
                
            break
        elif calcular_detalles == 'no':
            print("No se calculará TDEV, N° PERSONAS y COSTO de proyecto.")
            break
        else:
            print("Opción no válida. Por favor, seleccione 'si' o 'no'.")
#FIN MODELO2

#COCOMO2-MODELO 3 ¨Post - Arquitecture¨
def get_input(prompt, min_val=0.00, max_val=5.00):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Por favor, ingresa un valor entre {min_val} y {max_val}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def cocomo_post_architecture():
    # Constantes de COCOMO II Post-Arquitectura
    A = 2.94
    B = 0.91
    # Tamaño del software en KSLOC
    size = float(input("Ingrese el tamaño del software en KSLOC: "))
    
    # Factores de escala (ingresados por el usuario)
    SF = {}
    sf_labels = ['PREC', 'FLEX', 'RESL', 'TEAM', 'PMAT']
    print("\nIngrese los factores de escala SF:\n")
    for label in sf_labels:
        SF[label] = get_input(f"Ingrese el valor para {label} (0.00 a 5.00): ")

    # Factores de escala sumados
    scale_factors_w = sum(SF.values())

    # Multiplicadores de esfuerzo
    print("\nIngrese los multiplicadores de esfuerzo EM:\n")
    EM = {}
    em_labels = [
        'RELY', 'DATA', 'CPLX', 'RUSE', 'DOCU', 
        'TIME', 'STOR', 'PVOL', 'ACAP', 'PCAP', 
        'APEX', 'PLEX', 'LTEX', 'TOOL', 'SITE', 
        'SCED', 'PMAT'
    ]

    for label in em_labels:
        EM[label] = get_input(f"Ingrese el valor para {label} (0.01 a 5.00): ", min_val=0.01, max_val=5.00)

    # Calcular E
    E = B + 0.01 * scale_factors_w

    # Calcular el producto de los multiplicadores de esfuerzo
    product_em = 1
    for value in EM.values():
        product_em *= value

    # Calcular el esfuerzo (PM)
    PM = A * (size ** E) * product_em

    # Mostrar resultados
    print("\nResultados:")
    print(f"Constante A: {A}")
    print(f"Constante B: {B}")
    print(f"Factores de escala sumados: {scale_factors_w}")
    print(f"Factor de escala E: {E:.4f}")
    print(f"Producto de los multiplicadores de esfuerzo: {product_em:.4f}")
    print(f"Esfuerzo estimado (PM): {PM:.2f} Persona-Meses")

#FIN MODELO3

def cocomo_81():
    print("\nHas seleccionado COCOMO 81.")
    sabe_puntos_funcion = input("¿Sabe los puntos de función de su proyecto? (s/n): ").lower()
    
    if sabe_puntos_funcion == 's':
        kldc = obtener_kldc_por_puntos_funcion()
    elif sabe_puntos_funcion == 'n':
        kldc = obtener_kldc_por_ldc()
    else:
        print("Opción no válida.")
        return cocomo_81()

#recomendacion del modelo a utilizar segun kldc
    if kldc <= 50:
        print("\nRecomendación: Se sugiere calcular esfuerzo por el modelo básico.")
    elif 50 < kldc < 300:
        print("\nRecomendación: Se sugiere calcular esfuerzo por el modelo intermedio.")
    else:
        print("\nRecomendación: Se sugiere calcular esfuerzo por el modelo restringido (avanzado).")

    modelo = input("\n¿Desea calcular el esfuerzo en el Modelo Básico o Modelo Intermedio? (b/i): ").lower()
    
    if modelo == 'b':
        tipo_proyecto = seleccionar_tipo_proyecto()
        esfuerzo = calcular_esfuerzo_basico(kldc, tipo_proyecto)
        tdev = calcular_tdev(esfuerzo, tipo_proyecto)
        numero_personas = calcular_numero_personas(esfuerzo, tdev)
        costo = calcular_costo(numero_personas, tdev)
    elif modelo == 'i':
        tipo_proyecto = seleccionar_tipo_proyecto()
        eaf = obtener_eaf()
        esfuerzo = calcular_esfuerzo_intermedio(kldc, eaf, tipo_proyecto)
        tdev = calcular_tdev(esfuerzo, tipo_proyecto)
        numero_personas = calcular_numero_personas(esfuerzo, tdev)
        costo = calcular_costo(numero_personas, tdev)
    else:
        print("Opción no válida.")
        return cocomo_81()
    
    if esfuerzo and tdev and numero_personas and costo:
        print("\nRESULTADOS:")
        print(f"El esfuerzo estimado (PM) es: {esfuerzo:.2f} persona-meses")
        print(f"El tiempo de desarrollo estimado (TDEV) es: {tdev:.2f} meses")
        print(f"El número de personas necesarias es: {numero_personas:.2f}")
        print(f"El costo total estimado es: $ {costo:.2f}")
    else:
        print("Hubo un error en el cálculo.")

def cocomo_2():
    print("Has seleccionado COCOMO II.")
    #código para COCOMO 2
    #elegir modelo de cocomo 2
    print("¿Qué modelo de cálculo de esfuerzo desea utilizar?")
    print("1-Modelo de Composición de Aplicación. \n2-Modelo Diseño Temprano. \n3-Modelo de Post-Arquitectura")
    modelo = input("Elige un modelo (1,2 o 3): ")
    
    #modelo de composicion de aplicacion
    if modelo == "1":
        print("\nModelo de Composición de Aplicación seleccionado.")
        puntos_objeto = calcular_puntos_objeto()
        if puntos_objeto:
            nuevos_puntos_objeto = calcular_nuevos_puntos_objeto(puntos_objeto)
            productividad_promedio = input("¿Conoces el valor de productividad promedio? (si/no): ")
            if productividad_promedio.lower() == "si":
                productividad = float(input("Ingrese el valor de productividad promedio: "))
                esfuerzo_modelo1(nuevos_puntos_objeto, productividad)
            else:
                esfuerzo_modelo1(nuevos_puntos_objeto)

    #modelo diseño temprano           
    elif modelo == "2":
        print("\nModelo Diseño Temprano seleccionado.")
        cocomo_2_diseno_temprano()

    #modelo post-arqui    
    elif modelo == "3":
        print("\nModelo de Post-Arquitectura seleccionado.\n")
       #Llamada a la funcion de Post-Arquitectura
        cocomo_post_architecture()
    else:
        print("Selección no válida.")

def menu():
    bienvenida()
    while True:
        print("\nSelecciona una opción:")
        print("1. COCOMO 81")
        print("2. COCOMO II")
        print("3. Salir")
        
        opcion = input("\nIngrese su elección: ")
        
        if opcion == '1':
            cocomo_81()
        elif opcion == '2':
            cocomo_2()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor seleccione una opción válida (1, 2 o 3).")

if __name__ == "__main__":
    menu()
