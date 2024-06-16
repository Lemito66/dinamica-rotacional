import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
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

def plot_system(m1, m2, theta, direction):
    fig, ax = plt.subplots(1, 2, figsize=(14, 7))
    theta_rad = np.radians(theta)
    L = 1  # longitud arbitraria para dibujar

    # Primer gráfico: Sistema con fuerzas
    ax[0].plot([0, L * np.cos(theta_rad)], [0, L * np.sin(theta_rad)], 'k', label='Plano inclinado')
    ax[0].plot([L * np.cos(theta_rad), L * np.cos(theta_rad)], [L * np.sin(theta_rad), -0.5], 'k--')

    # Dibujo de las masas como círculos con colores diferentes
    ax[0].plot(L * np.cos(theta_rad) / 2, L * np.sin(theta_rad) / 2, 'go', label='m1 (verde)')
    ax[0].plot(L * np.cos(theta_rad), -0.5, 'mo', label='m2 (magenta)')
    ax[0].plot([L * np.cos(theta_rad), L * np.cos(theta_rad)], [L * np.sin(theta_rad), -0.5], 'k')

    # Ángulo ingresado como texto en el triángulo
    ax[0].text(0.2, 0, f'{theta}°', fontsize=12, ha='right', va='bottom')

    # Dibujo de fuerzas en m1
    # Tensión (T)
    ax[0].arrow(L * np.cos(theta_rad) / 2, L * np.sin(theta_rad) / 2, 0.2 * np.cos(theta_rad),
                0.2 * np.sin(theta_rad), head_width=0.05, head_length=0.1, fc='m', ec='m')
    ax[0].text(L * np.cos(theta_rad) / 2 + 0.2 * np.cos(theta_rad),
               L * np.sin(theta_rad) / 2 + 0.2 * np.sin(theta_rad), 'T', fontsize=12, color='m')

    # Normal (N)
    ax[0].arrow(L * np.cos(theta_rad) / 2, L * np.sin(theta_rad) / 2, -0.2 * np.sin(theta_rad),
                0.2 * np.cos(theta_rad), head_width=0.05, head_length=0.1, fc='b', ec='b')
    ax[0].text(L * np.cos(theta_rad) / 2 - 0.2 * np.sin(theta_rad),
               L * np.sin(theta_rad) / 2 + 0.2 * np.cos(theta_rad), 'N', fontsize=12, color='b')

    # Componente de peso perpendicular al plano (Wy)
    ax[0].arrow(L * np.cos(theta_rad) / 2, L * np.sin(theta_rad) / 2, 0.2 * np.sin(theta_rad),
                -0.2 * np.cos(theta_rad), head_width=0.05, head_length=0.1, fc='orange', ec='orange')
    ax[0].text(L * np.cos(theta_rad) / 2 + 0.2 * np.sin(theta_rad),
               L * np.sin(theta_rad) / 2 - 0.2 * np.cos(theta_rad) - 0.1, 'Wy', fontsize=12, color='orange')

    # Peso (W1)
    ax[0].arrow(L * np.cos(theta_rad) / 2, L * np.sin(theta_rad) / 2, 0, -0.2, head_width=0.05, head_length=0.1,
                fc='g', ec='g')
    ax[0].text(L * np.cos(theta_rad) / 2, L * np.sin(theta_rad) / 2 - 0.2, 'W1', fontsize=12, color='g')

    # Componente de peso paralela al plano (Wx)
    ax[0].arrow(L * np.cos(theta_rad) / 2, L * np.sin(theta_rad) / 2, -0.2 * np.cos(theta_rad),
                -0.2 * np.sin(theta_rad), head_width=0.05, head_length=0.1, fc='purple', ec='purple')
    ax[0].text(L * np.cos(theta_rad) / 2 - 0.2 * np.cos(theta_rad),
               L * np.sin(theta_rad) / 2 - 0.2 * np.sin(theta_rad), 'Wx', fontsize=12, color='purple')

    # Componente de fuerza de fricción (frk)
    if direction == 'derecha':
        ax[0].arrow(L * np.cos(theta_rad) / 2, L * np.sin(theta_rad) / 2, -0.2 * np.cos(theta_rad),
                    -0.2 * np.sin(theta_rad), head_width=0.05, head_length=0.1, fc='brown', ec='brown')
        ax[0].text(L * np.cos(theta_rad) / 2 - 0.2 * np.cos(theta_rad),
                   L * np.sin(theta_rad) / 2 - 0.3 * np.sin(theta_rad), 'frk', fontsize=12, color='brown')
    else:
        ax[0].arrow(L * np.cos(theta_rad) / 2, L * np.sin(theta_rad) / 2, 0.2 * np.cos(theta_rad),
                    0.2 * np.sin(theta_rad), head_width=0.05, head_length=0.1, fc='brown', ec='brown')
        ax[0].text(L * np.cos(theta_rad) / 2 + 0.2 * np.cos(theta_rad),
                   L * np.sin(theta_rad) / 2 + 0.2 * np.sin(theta_rad), 'frk', fontsize=12, color='brown')

    # Dibujo de fuerzas en m2
    ax[0].arrow(L * np.cos(theta_rad), -0.5, 0, -0.2, head_width=0.05, head_length=0.1, fc='g', ec='g')
    ax[0].text(L * np.cos(theta_rad), -0.7, 'W2', fontsize=12, color='g')

    # Tensión (T) en m2 (hacia arriba)
    arrow_length = 0.2  # longitud arbitraria para la flecha de tensión
    ax[0].arrow(L * np.cos(theta_rad), -0.5, 0, arrow_length, head_width=0.05, head_length=0.1, fc='m', ec='m')
    ax[0].text(L * np.cos(theta_rad), -0.4, 'T', fontsize=12, color='m', ha='center')

    # Añadir los ejes X e Y
    ax[0].axhline(0, color='grey', lw=1)
    ax[0].axvline(0, color='grey', lw=1)

    ax[0].set_aspect('equal')
    ax[0].set_xlim(-0.1, L * np.cos(theta_rad) + 0.3)
    ax[0].set_ylim(-0.8, L * np.sin(theta_rad) + 0.3)
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[0].set_title('Sistema con fuerzas')
    ax[0].legend()
    ax[0].grid()

    # Segundo gráfico: Sistema con masas y polea
    ax[1].plot([0, L * np.cos(theta_rad)], [0, L * np.sin(theta_rad)], 'k', label='Plano inclinado')
    ax[1].plot([L * np.cos(theta_rad), L * np.cos(theta_rad)], [L * np.sin(theta_rad), -0.5], 'k--')

    # Dibujo de la polea como un círculo
    polea = patches.Circle((L * np.cos(theta_rad), L * np.sin(theta_rad)), 0.05, edgecolor='black', facecolor='none')
    ax[1].add_patch(polea)

    # Dibujo de las masas como cuadrados con colores diferentes
    masa1 = patches.Rectangle(
        (L * np.cos(theta_rad) / 2 - 0.05, L * np.sin(theta_rad) / 2 - 0.05),
        0.1, 0.1, angle=theta, edgecolor='green', facecolor='none', label='m1 (verde)'
    )
    masa2 = patches.Rectangle(
        (L * np.cos(theta_rad) - 0.05, -0.55), 0.1, 0.1, edgecolor='magenta', facecolor='none', label='m2 (magenta)'
    )
    ax[1].add_patch(masa1)
    ax[1].add_patch(masa2)

    # Dibujo de la cuerda que sostiene m2 más corta
    ax[1].plot([L * np.cos(theta_rad), L * np.cos(theta_rad)], [L * np.sin(theta_rad), -0.45], 'k')

    # Ángulo ingresado como texto en el triángulo
    ax[1].text(0.2, 0, f'{theta}°', fontsize=12, ha='right', va='bottom')

    # Añadir los ejes X e Y
    ax[1].axhline(0, color='grey', lw=1)
    ax[1].axvline(0, color='grey', lw=1)

    ax[1].set_aspect('equal')
    ax[1].set_xlim(-0.1, L * np.cos(theta_rad) + 0.3)
    ax[1].set_ylim(-0.8, L * np.sin(theta_rad) + 0.3)
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('y')
    ax[1].set_title('Sistema con polea')
    ax[1].legend()
    ax[1].grid()

    plt.tight_layout()
    plt.show()

def main():
    print("Cálculo de la aceleración y tensión en un sistema con poleas y cuerdas")

    # Pedir variables al usuario
    m1 = pedir_numero("Ingresa la masa m1 (en kg): ")
    m2 = pedir_numero("Ingresa la masa m2 (en kg): ")
    theta = pedir_numero("Ingresa el ángulo del plano inclinado (en grados): ")
    mu = pedir_numero("Ingresa el coeficiente de fricción mu: ")

    try:
        aceleracion, tension = resolver_sistema(m1, m2, theta, mu)
        print(f"La aceleración del sistema es {aceleracion:.2f} m/s^2")
        print(f"La tensión en el hilo es {tension:.2f} N")

        direction = 'derecha' if aceleracion > 0 else 'izquierda'

        # Dibujar el sistema
        plot_system(m1, m2, theta, direction)

    except Exception as e:
        print(f"Error al resolver el sistema: {e}")

    input("Presiona Enter para salir...")

main()
