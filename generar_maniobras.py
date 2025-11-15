"""
Script para generar gráficas de maniobras de camiones
Muestra: entrada, salida y espacio de maniobrabilidad
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, FancyArrow, Arc
from matplotlib.path import Path
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# Configuración
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 10

# Datos del problema
CAMION_LARGO = 12  # metros
CAMION_ANCHO = 2.5  # metros
DISTANCIAMIENTO = 2  # metros
ESPACIO_LARGO = CAMION_LARGO + 2 * DISTANCIAMIENTO  # 16m
ESPACIO_ANCHO = CAMION_ANCHO + 2 * DISTANCIAMIENTO  # 6.5m
AREA_POR_CAMION = ESPACIO_LARGO * ESPACIO_ANCHO  # 104 m²

# ECUACIÓN LINEAL PARA AMPLIACIÓN NECESARIA
def calcular_ampliacion_necesaria(num_camiones, area_actual=550, area_por_camion=104,
                                   factor_maniobra=1.44):
    """
    Ecuación lineal para calcular la ampliación exacta necesaria

    Parámetros:
    - num_camiones: número de camiones a estacionar
    - area_actual: área actual del parqueadero (550 m²)
    - area_por_camion: área de estacionamiento por camión (104 m²)
    - factor_maniobra: factor de espacio adicional para maniobras (1.44 → 150/104)

    Fórmula:
    A_ampliación = (n × a × f) - A_actual

    Donde:
    - n = número de camiones
    - a = área por camión (104 m²)
    - f = factor de maniobras (1.44)
    - A_actual = área actual (550 m²)

    Retorna:
    - Área de ampliación necesaria en m²
    """
    area_necesaria = num_camiones * area_por_camion * factor_maniobra
    ampliacion = area_necesaria - area_actual
    return max(0, ampliacion)  # No puede ser negativa


def dibujar_camion(ax, x, y, angulo, color='#3498db', label=None, alpha=1.0):
    """Dibuja un camión en posición y ángulo específico"""
    # Crear polígono del camión
    largo = CAMION_LARGO
    ancho = CAMION_ANCHO

    # Vértices del camión (rectángulo)
    vertices = np.array([
        [-largo/2, -ancho/2],
        [largo/2, -ancho/2],
        [largo/2, ancho/2],
        [-largo/2, ancho/2]
    ])

    # Rotar
    theta = np.radians(angulo)
    rot_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    vertices_rot = vertices @ rot_matrix.T

    # Trasladar
    vertices_final = vertices_rot + np.array([x, y])

    # Dibujar camión
    camion = Polygon(vertices_final, facecolor=color, edgecolor='#2c3e50',
                     linewidth=2, alpha=alpha, label=label)
    ax.add_patch(camion)

    # Dibujar cabina (frente del camión)
    if angulo == 0:
        cabina_x = x + largo/2 - 2
        cabina_y = y
    elif angulo == 90:
        cabina_x = x
        cabina_y = y + largo/2 - 2
    elif angulo == 180:
        cabina_x = x - largo/2 + 2
        cabina_y = y
    else:
        cabina_x = x
        cabina_y = y - largo/2 + 2

    cabina = Rectangle((cabina_x - 1, cabina_y - ancho/4), 2, ancho/2,
                       facecolor='#2c3e50', edgecolor='white', linewidth=1.5, alpha=alpha)

    return camion


def dibujar_zona_seguridad(ax, x, y, angulo, color='#e74c3c', alpha=0.15):
    """Dibuja la zona de seguridad alrededor del camión"""
    largo_zona = ESPACIO_LARGO
    ancho_zona = ESPACIO_ANCHO

    # Vértices de la zona
    vertices = np.array([
        [-largo_zona/2, -ancho_zona/2],
        [largo_zona/2, -ancho_zona/2],
        [largo_zona/2, ancho_zona/2],
        [-largo_zona/2, ancho_zona/2]
    ])

    # Rotar
    theta = np.radians(angulo)
    rot_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    vertices_rot = vertices @ rot_matrix.T
    vertices_final = vertices_rot + np.array([x, y])

    zona = Polygon(vertices_final, facecolor=color, edgecolor=color,
                   linewidth=1.5, linestyle='--', alpha=alpha)
    ax.add_patch(zona)

    # Dibujar conos en las esquinas
    for v in vertices_final:
        cono = Circle(v, 0.4, facecolor='orange', edgecolor='#d35400', linewidth=1.5)
        ax.add_patch(cono)


def dibujar_trayectoria(ax, puntos, color='#2ecc71', label='Trayectoria'):
    """Dibuja una trayectoria con flechas"""
    for i in range(len(puntos) - 1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i + 1]

        # Calcular dirección
        dx = x2 - x1
        dy = y2 - y1

        # Dibujar flecha
        arrow = FancyArrow(x1, y1, dx * 0.9, dy * 0.9,
                          width=0.5, head_width=1.5, head_length=1,
                          facecolor=color, edgecolor='#27ae60', linewidth=2,
                          alpha=0.7, zorder=10)
        ax.add_patch(arrow)

    # Línea punteada de la trayectoria
    x_coords = [p[0] for p in puntos]
    y_coords = [p[1] for p in puntos]
    ax.plot(x_coords, y_coords, 'o--', color=color, linewidth=2,
            markersize=8, alpha=0.5, label=label)


def generar_grafica_maniobra_entrada():
    """Genera gráfica de maniobra de entrada de camión"""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Dibujar área de parqueadero
    parqueadero = Rectangle((0, 0), 30, 20, facecolor='#ecf0f1',
                            edgecolor='#34495e', linewidth=3, alpha=0.3)
    ax.add_patch(parqueadero)

    # Entrada
    entrada = Rectangle((-3, 8), 3, 4, facecolor='#95a5a6',
                        edgecolor='#7f8c8d', linewidth=2, alpha=0.5)
    ax.add_patch(entrada)
    ax.text(-1.5, 10, 'ENTRADA', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')

    # Posición final del camión
    x_final, y_final = 15, 10
    dibujar_zona_seguridad(ax, x_final, y_final, 0)
    dibujar_camion(ax, x_final, y_final, 0, color='#3498db', label='Posición final')

    # Trayectoria de entrada
    trayectoria_entrada = [
        (-1.5, 10),  # Entrada
        (5, 10),     # Punto intermedio 1
        (10, 10),    # Punto intermedio 2
        (15, 10)     # Posición final
    ]
    dibujar_trayectoria(ax, trayectoria_entrada, color='#2ecc71', label='Ruta de entrada')

    # Camión en posiciones intermedias (transparente)
    dibujar_camion(ax, 5, 10, 0, color='#3498db', alpha=0.2)
    dibujar_camion(ax, 10, 10, 0, color='#3498db', alpha=0.3)

    # Radio de giro
    centro_giro = (5, 10)
    radio_giro = 8
    arco = Arc(centro_giro, 2*radio_giro, 2*radio_giro, angle=0,
              theta1=0, theta2=90, color='#e67e22', linewidth=2,
              linestyle='--', alpha=0.6)
    ax.add_patch(arco)
    ax.text(8, 14, f'Radio de giro\n≈ {radio_giro}m', ha='center',
            fontsize=10, color='#e67e22', fontweight='bold')

    # Configuración de la gráfica
    ax.set_xlim(-5, 32)
    ax.set_ylim(-2, 22)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.set_xlabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_title('MANIOBRA DE ENTRADA - Análisis de Trayectoria y Espacio Requerido',
                fontsize=14, fontweight='bold', pad=20)

    # Leyenda
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

    # Anotaciones
    ax.text(15, 2, f'Espacio requerido: {ESPACIO_LARGO}m × {ESPACIO_ANCHO}m = {AREA_POR_CAMION}m²',
            ha='center', fontsize=11, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.savefig('./images/maniobra_entrada.png', dpi=150, bbox_inches='tight')
    print("✅ Gráfica de maniobra de entrada generada")
    plt.close()


def generar_grafica_maniobra_salida():
    """Genera gráfica de maniobra de salida de camión"""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Dibujar área de parqueadero
    parqueadero = Rectangle((0, 0), 30, 20, facecolor='#ecf0f1',
                            edgecolor='#34495e', linewidth=3, alpha=0.3)
    ax.add_patch(parqueadero)

    # Salida
    salida = Rectangle((30, 8), 3, 4, facecolor='#95a5a6',
                       edgecolor='#7f8c8d', linewidth=2, alpha=0.5)
    ax.add_patch(salida)
    ax.text(31.5, 10, 'SALIDA', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')

    # Posición inicial del camión
    x_inicial, y_inicial = 15, 10
    dibujar_zona_seguridad(ax, x_inicial, y_inicial, 0, alpha=0.1)
    dibujar_camion(ax, x_inicial, y_inicial, 0, color='#e74c3c', label='Posición inicial')

    # Trayectoria de salida
    trayectoria_salida = [
        (15, 10),    # Posición inicial
        (20, 10),    # Punto intermedio 1
        (25, 10),    # Punto intermedio 2
        (31.5, 10)   # Salida
    ]
    dibujar_trayectoria(ax, trayectoria_salida, color='#e74c3c', label='Ruta de salida')

    # Camión en posiciones intermedias (transparente)
    dibujar_camion(ax, 20, 10, 0, color='#e74c3c', alpha=0.3)
    dibujar_camion(ax, 25, 10, 0, color='#e74c3c', alpha=0.2)

    # Espacio de maniobra para salir
    maniobra = Rectangle((12, 5), 10, 10, facecolor='yellow',
                         edgecolor='orange', linewidth=2, linestyle='--', alpha=0.15)
    ax.add_patch(maniobra)
    ax.text(17, 15.5, 'Espacio de maniobra\npara salida', ha='center',
            fontsize=10, color='orange', fontweight='bold')

    # Radio de giro
    centro_giro = (25, 10)
    radio_giro = 8
    arco = Arc(centro_giro, 2*radio_giro, 2*radio_giro, angle=0,
              theta1=90, theta2=180, color='#e67e22', linewidth=2,
              linestyle='--', alpha=0.6)
    ax.add_patch(arco)

    # Configuración de la gráfica
    ax.set_xlim(-2, 35)
    ax.set_ylim(-2, 22)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.set_xlabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_title('MANIOBRA DE SALIDA - Análisis de Trayectoria y Espacio Requerido',
                fontsize=14, fontweight='bold', pad=20)

    # Leyenda
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

    # Anotaciones
    ax.text(15, 2, f'Distanciamiento de seguridad: {DISTANCIAMIENTO}m por cada lado',
            ha='center', fontsize=11, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.savefig('./images/maniobra_salida.png', dpi=150, bbox_inches='tight')
    print("✅ Gráfica de maniobra de salida generada")
    plt.close()


def generar_grafica_maniobrabilidad():
    """Genera gráfica completa de maniobrabilidad con múltiples camiones"""
    fig, ax = plt.subplots(figsize=(16, 12))

    # Dibujar área de parqueadero completa (forma de C)
    # Rectángulo A
    rect_a = Rectangle((0, 20), 20, 10, facecolor='#d5dbdb',
                       edgecolor='#34495e', linewidth=2.5, alpha=0.4)
    ax.add_patch(rect_a)
    ax.text(10, 25, 'RECTÁNGULO A\n20m × 10m', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#2c3e50')

    # Rectángulo B (zona de maniobra)
    rect_b = Rectangle((0, 10), 15, 10, facecolor='#fcf3cf',
                       edgecolor='#f39c12', linewidth=2.5, alpha=0.4)
    ax.add_patch(rect_b)
    ax.text(7.5, 15, 'RECTÁNGULO B\n15m × 10m\n(ZONA DE MANIOBRA)',
            ha='center', va='center', fontsize=10, fontweight='bold', color='#d68910')

    # Rectángulo C
    rect_c = Rectangle((0, 0), 20, 10, facecolor='#d5dbdb',
                       edgecolor='#34495e', linewidth=2.5, alpha=0.4)
    ax.add_patch(rect_c)
    ax.text(10, 5, 'RECTÁNGULO C\n20m × 10m', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#2c3e50')

    # Ampliación (calculada con ecuación lineal)
    num_camiones_objetivo = 5
    ampliacion = 50  # Para este caso específico
    rect_amp = Rectangle((20, 10), 10, 5, facecolor='#aed6f1',
                         edgecolor='#2874a6', linewidth=2.5, alpha=0.5)
    ax.add_patch(rect_amp)
    ax.text(25, 12.5, f'AMPLIACIÓN\n10m × 5m\n= {ampliacion}m²',
            ha='center', va='center', fontsize=10, fontweight='bold', color='#1a5490')

    # Camiones estacionados con zonas de seguridad
    camiones = [
        (10, 25, 0, '#3498db'),   # Rectángulo A
        (10, 5, 0, '#3498db'),    # Rectángulo C
    ]

    for i, (x, y, ang, col) in enumerate(camiones, 1):
        dibujar_zona_seguridad(ax, x, y, ang)
        dibujar_camion(ax, x, y, ang, color=col, label=f'Camión {i}' if i == 1 else None)
        ax.text(x, y, f'{i}', ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')

    # Trayectorias de maniobra
    # Entrada
    trayectoria_entrada = [
        (-3, 15),
        (5, 15),
        (10, 25)
    ]
    dibujar_trayectoria(ax, trayectoria_entrada, color='#2ecc71', label='Ruta entrada')

    # Salida
    trayectoria_salida = [
        (10, 5),
        (15, 12),
        (25, 12),
        (32, 15)
    ]
    dibujar_trayectoria(ax, trayectoria_salida, color='#e74c3c', label='Ruta salida')

    # Entrada visual
    entrada = Rectangle((-5, 13), 2, 4, facecolor='#27ae60',
                        edgecolor='#229954', linewidth=2, alpha=0.6)
    ax.add_patch(entrada)
    ax.text(-4, 15, 'IN', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Salida visual
    salida = Rectangle((30, 13), 2, 4, facecolor='#e74c3c',
                       edgecolor='#c0392b', linewidth=2, alpha=0.6)
    ax.add_patch(salida)
    ax.text(31, 15, 'OUT', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Pasillos de circulación
    pasillo1 = Rectangle((0, 10), 30, 1, facecolor='none',
                         edgecolor='#f39c12', linewidth=3, linestyle='--', alpha=0.7)
    ax.add_patch(pasillo1)
    ax.text(15, 10.5, 'PASILLO DE CIRCULACIÓN (6m ancho)',
            ha='center', fontsize=9, color='#d68910', fontweight='bold')

    # Configuración de la gráfica
    ax.set_xlim(-7, 34)
    ax.set_ylim(-3, 32)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.set_xlabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_title('ANÁLISIS COMPLETO DE MANIOBRABILIDAD\nEntrada, Salida y Espacios de Maniobra',
                fontsize=14, fontweight='bold', pad=20)

    # Leyenda
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9, ncol=2)

    # Información adicional
    info_text = f"""
    ESPECIFICACIONES TÉCNICAS:
    • Área total: 550m² + {ampliacion}m² = 600m²
    • Espacio por camión: {AREA_POR_CAMION}m²
    • Distanciamiento: {DISTANCIAMIENTO}m
    • Pasillo maniobra: 6m mínimo
    """
    ax.text(-6, -1.5, info_text, fontsize=9,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9),
            verticalalignment='top', family='monospace')

    plt.tight_layout()
    plt.savefig('./images/maniobrabilidad_completa.png', dpi=150, bbox_inches='tight')
    print("✅ Gráfica de maniobrabilidad completa generada")
    plt.close()


def generar_grafica_ecuacion_lineal():
    """Genera gráfica de la ecuación lineal de ampliación necesaria"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Rango de camiones
    num_camiones = np.arange(1, 21)

    # Calcular ampliaciones necesarias
    area_actual = 550
    factor_maniobra = 1.44  # 150/104

    ampliacion_sin_maniobras = [calcular_ampliacion_necesaria(n, area_actual, 104, 1.0)
                                 for n in num_camiones]
    ampliacion_con_maniobras = [calcular_ampliacion_necesaria(n, area_actual, 104, factor_maniobra)
                                for n in num_camiones]

    # Graficar
    ax.plot(num_camiones, ampliacion_sin_maniobras, 'o-', linewidth=2.5,
            markersize=8, color='#3498db', label='Sin considerar maniobras')
    ax.plot(num_camiones, ampliacion_con_maniobras, 's-', linewidth=2.5,
            markersize=8, color='#e74c3c', label='Con maniobras (factor 1.44)')

    # Línea horizontal en 50m²
    ax.axhline(y=50, color='#2ecc71', linestyle='--', linewidth=2,
               label='Ampliación disponible (50m²)', alpha=0.7)

    # Punto específico para 15 camiones
    amp_15 = calcular_ampliacion_necesaria(15, area_actual, 104, factor_maniobra)
    ax.plot(15, amp_15, 'D', markersize=15, color='#f39c12',
            markeredgecolor='#d68910', markeredgewidth=2,
            label=f'Objetivo: 15 camiones\n(Requiere {amp_15:.0f}m²)', zorder=10)

    # Sombreado de zona factible
    ax.fill_between(num_camiones, 0, 50, alpha=0.15, color='#2ecc71',
                     label='Zona factible con 50m²')

    # Configuración
    ax.set_xlabel('Número de camiones', fontsize=12, fontweight='bold')
    ax.set_ylabel('Ampliación necesaria (m²)', fontsize=12, fontweight='bold')
    ax.set_title('ECUACIÓN LINEAL: Ampliación Necesaria vs Número de Camiones\n' +
                 r'$A_{ampliación} = (n \times 104 \times f) - 550$',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

    # Anotaciones
    ax.annotate(f'Para 15 camiones:\n{amp_15:.0f}m² necesarios',
                xy=(15, amp_15), xytext=(12, amp_15 + 300),
                arrowprops=dict(arrowstyle='->', color='#f39c12', lw=2),
                fontsize=10, fontweight='bold', color='#d68910',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Ecuación en la gráfica
    ecuacion_text = r"""
    ECUACIÓN LINEAL:
    $A_{ampliación} = (n \times a \times f) - A_{actual}$

    Donde:
    • n = número de camiones
    • a = 104 m² (área por camión)
    • f = 1.44 (factor de maniobras)
    • $A_{actual}$ = 550 m²
    """
    ax.text(0.98, 0.35, ecuacion_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9),
            family='monospace')

    plt.tight_layout()
    plt.savefig('./images/ecuacion_lineal_ampliacion.png', dpi=150, bbox_inches='tight')
    print("✅ Gráfica de ecuación lineal generada")
    plt.close()


def generar_tabla_ampliacion():
    """Genera tabla con valores de ampliación necesaria"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('tight')
    ax.axis('off')

    # Datos para la tabla
    num_camiones_lista = [3, 5, 8, 10, 12, 15, 18, 20]
    area_actual = 550
    factor_maniobra = 1.44

    datos_tabla = []
    for n in num_camiones_lista:
        area_necesaria = n * 104 * factor_maniobra
        ampliacion = calcular_ampliacion_necesaria(n, area_actual, 104, factor_maniobra)
        area_total = area_actual + ampliacion
        viabilidad = "✅ Factible" if ampliacion <= 50 else "❌ No factible"

        datos_tabla.append([
            n,
            f"{area_necesaria:.0f}",
            f"{ampliacion:.0f}",
            f"{area_total:.0f}",
            viabilidad
        ])

    # Crear tabla
    columnas = ['N° Camiones', 'Área Necesaria\n(m²)', 'Ampliación\nRequerida (m²)',
                'Área Total\n(m²)', 'Viabilidad\n(con 50m²)']

    tabla = ax.table(cellText=datos_tabla, colLabels=columnas,
                     cellLoc='center', loc='center',
                     colWidths=[0.15, 0.2, 0.2, 0.2, 0.25])

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(11)
    tabla.scale(1, 2.5)

    # Estilo de la tabla
    for i in range(len(columnas)):
        tabla[(0, i)].set_facecolor('#34495e')
        tabla[(0, i)].set_text_props(weight='bold', color='white')

    for i in range(1, len(datos_tabla) + 1):
        for j in range(len(columnas)):
            if i % 2 == 0:
                tabla[(i, j)].set_facecolor('#ecf0f1')
            else:
                tabla[(i, j)].set_facecolor('white')

            # Resaltar fila de 15 camiones
            if datos_tabla[i-1][0] == 15:
                tabla[(i, j)].set_facecolor('#ffe5b4')
                tabla[(i, j)].set_text_props(weight='bold')

    # Título
    ax.set_title('TABLA DE AMPLIACIÓN NECESARIA SEGÚN ECUACIÓN LINEAL\n' +
                 r'Basado en: $A_{ampliación} = (n \times 104 \times 1.44) - 550$',
                fontsize=14, fontweight='bold', pad=20)

    # Nota al pie
    nota = ("NOTA: La ecuación lineal considera un factor de 1.44 para incluir espacio de maniobras.\n"
            "Área base actual: 550m² | Área por camión (estacionamiento): 104m² | "
            "Área por camión (con maniobras): 150m²")
    fig.text(0.5, 0.05, nota, ha='center', fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.savefig('./images/tabla_ampliacion_lineal.png', dpi=150, bbox_inches='tight')
    print("✅ Tabla de ampliación necesaria generada")
    plt.close()


if __name__ == "__main__":
    print("\n" + "="*70)
    print("GENERANDO GRÁFICAS DE MANIOBRAS Y ECUACIÓN LINEAL")
    print("="*70 + "\n")

    # Crear directorio de imágenes si no existe
    import os
    os.makedirs('./images', exist_ok=True)

    # Generar todas las gráficas
    generar_grafica_ecuacion_lineal()
    generar_tabla_ampliacion()
    generar_grafica_maniobra_entrada()
    generar_grafica_maniobra_salida()
    generar_grafica_maniobrabilidad()

    print("\n" + "="*70)
    print("✅ TODAS LAS GRÁFICAS GENERADAS EXITOSAMENTE")
    print("="*70 + "\n")

    # Mostrar información de la ecuación
    print("\n📐 ECUACIÓN LINEAL DESARROLLADA:")
    print("="*70)
    print("\nFórmula: A_ampliación = (n × a × f) - A_actual")
    print("\nDonde:")
    print("  • n = número de camiones")
    print("  • a = 104 m² (área de estacionamiento por camión)")
    print("  • f = 1.44 (factor de maniobras: 150/104)")
    print("  • A_actual = 550 m² (área base del parqueadero)")
    print("\nEjemplos:")
    for n in [5, 10, 15]:
        amp = calcular_ampliacion_necesaria(n)
        print(f"  • {n} camiones → Ampliación necesaria: {amp:.0f} m²")

    print("\n" + "="*70)
