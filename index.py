from sympy import symbols, Eq, sin, cos, pi, solve

def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")

def resolver_sistema(mA, mB, angulo, mu, g=9.81):
    # Convertir ángulo a radianes para las funciones trigonométricas
    angulo_rad = angulo * pi / 180

    # Variables simbólicas
    a, T = symbols('a T')

    # Fuerzas
    F_gA_parallel = mA * g * sin(angulo_rad)
    F_gA_perpendicular = mA * g * cos(angulo_rad)
    F_fric = mu * F_gA_perpendicular
    F_gB = mB * g

    # Ecuaciones
    eq1 = Eq(mA * a, F_gA_parallel - T - F_fric)
    eq2 = Eq(mB * a, T - F_gB)

    # Resolver el sistema de ecuaciones
    solution = solve((eq1, eq2), (a, T))
    aceleracion = solution[a].evalf()
    tension = solution[T].evalf()

    return aceleracion, tension

def main():
    print("Cálculo de la aceleración y tensión en un sistema con poleas y cuerdas")

    # Pedir variables al usuario
    
    mA = pedir_numero("Ingresa la masa mA (en kg): ")
    mB = pedir_numero("Ingresa la masa mB (en kg): ")
    angulo = pedir_numero("Ingresa el ángulo del plano inclinado (en grados): ")
    mu = pedir_numero("Ingresa el coeficiente de fricción mu: ") 
    
    
    
    '''mA = 5
    mB = 3
    angulo = 30
    mu = 0.2 '''

    try:
        aceleracion, tension = resolver_sistema(mA, mB, angulo, mu)
        print(f"La aceleración del sistema es {aceleracion:.2f} m/s^2")
        print(f"La tensión en el hilo es {tension:.2f} N")
    except Exception as e:
        print(f"Error al resolver el sistema: {e}")


main()
