import matplotlib.pyplot as plt
import numpy as np

def draw_right_triangle():
    # Definir los puntos del triángulo
    A = (0, 0)
    B = (4, 0)
    C = (0, 3)
    
    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    
    # Dibujar los lados del triángulo
    triangle_x = [A[0], B[0], C[0], A[0]]
    triangle_y = [A[1], B[1], C[1], A[1]]
    ax.plot(triangle_x, triangle_y, 'b-', linewidth=2, label='Triángulo')
    
    # Dibujar los puntos
    ax.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red', label='Vértices')
    
    # Etiquetas de los puntos
    ax.text(A[0] - 0.3, A[1] - 0.2, 'A', fontsize=12, color='black')
    ax.text(B[0] + 0.1, B[1] - 0.2, 'B', fontsize=12, color='black')
    ax.text(C[0] - 0.3, C[1] + 0.1, 'C', fontsize=12, color='black')
    
    # Dibujar la circunferencia circunscrita
    center_x, center_y = (B[0] / 2, C[1] / 2)
    radius = np.sqrt((center_x - A[0])**2 + (center_y - A[1])**2)
    circle = plt.Circle((center_x, center_y), radius, color='g', fill=False, linestyle='dashed', label='Circunferencia circunscrita')
    ax.add_patch(circle)
    
    # Ajustar límites y mostrar
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 4)
    ax.set_aspect('equal')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.title("Triángulo Rectángulo con Circunferencia Circunscrita")
    plt.show()

# Llamar a la función
if __name__ == "__main__":
    draw_right_triangle()
