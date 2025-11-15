"""
Script completo para generar TODAS las imágenes del proyecto
Análisis de Parqueadero Rodrish S.A.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, FancyArrow, Arc, Wedge
from matplotlib.path import Path
import matplotlib.patches as mpatches
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Configuración global
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 10

# Constantes del problema
CAMION_LARGO = 12  # metros
CAMION_ANCHO = 2.5  # metros
DISTANCIAMIENTO = 2  # metros
ESPACIO_LARGO = CAMION_LARGO + 2 * DISTANCIAMIENTO  # 16m
ESPACIO_ANCHO = CAMION_ANCHO + 2 * DISTANCIAMIENTO  # 6.5m
AREA_POR_CAMION = ESPACIO_LARGO * ESPACIO_ANCHO  # 104 m²
RADIO_GIRO = 8  # metros
FACTOR_MANIOBRAS = 1.44
AREA_ACTUAL = 550  # m²

import os
os.makedirs('./images', exist_ok=True)

#=============================================================================
# FUNCIONES AUXILIARES
#=============================================================================

def dibujar_camion(ax, x, y, angulo, color='#3498db', label=None, alpha=1.0):
    """Dibuja un camión en posición y ángulo específico"""
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
    vertices_final = vertices_rot + np.array([x, y])

    # Dibujar camión
    camion = Polygon(vertices_final, facecolor=color, edgecolor='#2c3e50',
                     linewidth=2, alpha=alpha, label=label)
    ax.add_patch(camion)

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


#=============================================================================
# IMAGEN 1: TERRENO ACTUAL (forma de C)
#=============================================================================

def generar_terreno_actual():
    """Genera visualización del terreno actual en forma de C"""
    fig, ax = plt.subplots(figsize=(12, 10))

    # Rectángulo A (superior) - 20m × 10m
    rect_a = Rectangle((0, 20), 20, 10, facecolor='#aed6f1',
                       edgecolor='#2874a6', linewidth=3, alpha=0.5)
    ax.add_patch(rect_a)
    ax.text(10, 25, 'RECTÁNGULO A\n20m × 10m\n= 200 m²',
            ha='center', va='center', fontsize=12, fontweight='bold',
            color='#1a5490')

    # Rectángulo B (medio) - 15m × 10m - ASIMÉTRICO
    rect_b = Rectangle((0, 10), 15, 10, facecolor='#f9e79f',
                       edgecolor='#f39c12', linewidth=3, alpha=0.5)
    ax.add_patch(rect_b)
    ax.text(7.5, 15, 'RECTÁNGULO B\n15m × 10m\n= 150 m²\n⚠️ ASIMÉTRICO',
            ha='center', va='center', fontsize=12, fontweight='bold',
            color='#d68910')

    # Rectángulo C (inferior) - 20m × 10m
    rect_c = Rectangle((0, 0), 20, 10, facecolor='#aed6f1',
                       edgecolor='#2874a6', linewidth=3, alpha=0.5)
    ax.add_patch(rect_c)
    ax.text(10, 5, 'RECTÁNGULO C\n20m × 10m\n= 200 m²',
            ha='center', va='center', fontsize=12, fontweight='bold',
            color='#1a5490')

    # Dimensiones
    # Altura total
    ax.plot([22, 22], [0, 30], 'k-', linewidth=2)
    ax.plot([21.5, 22.5], [0, 0], 'k-', linewidth=2)
    ax.plot([21.5, 22.5], [30, 30], 'k-', linewidth=2)
    ax.text(24, 15, '30m', ha='center', va='center', fontsize=11,
            rotation=90, fontweight='bold')

    # Ancho A
    ax.plot([0, 20], [-2, -2], 'k-', linewidth=2)
    ax.plot([0, 0], [-2.5, -1.5], 'k-', linewidth=2)
    ax.plot([20, 20], [-2.5, -1.5], 'k-', linewidth=2)
    ax.text(10, -3.5, '20m', ha='center', va='center', fontsize=11,
            fontweight='bold')

    # Ancho B
    ax.plot([0, 15], [9, 9], 'k-', linewidth=1.5, linestyle='--')
    ax.text(7.5, 8, '15m', ha='center', va='center', fontsize=10,
            color='#d68910', fontweight='bold')

    # Configuración
    ax.set_xlim(-5, 27)
    ax.set_ylim(-5, 33)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.set_xlabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_title('TERRENO ACTUAL - Configuración en Forma de C\n' +
                 'Área Total: 200 + 150 + 200 = 550 m²',
                 fontsize=14, fontweight='bold', pad=20)

    # Información
    info_text = """
    CONFIGURACIÓN ACTUAL:
    • Rectángulo A: 200 m²
    • Rectángulo B: 150 m² (asimétrico)
    • Rectángulo C: 200 m²
    ────────────────────
    ÁREA TOTAL: 550 m²
    """
    ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9),
            family='monospace')

    plt.tight_layout()
    plt.savefig('./images/terreno_actual.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 1: terreno_actual.png generada")
    plt.close()


#=============================================================================
# IMAGEN 2: ESPACIO POR CAMIÓN
#=============================================================================

def generar_espacio_camion():
    """Genera visualización del espacio requerido por camión"""
    fig, ax = plt.subplots(figsize=(12, 10))

    # Posición central del camión
    x, y = 10, 8

    # Dibujar zona de seguridad
    dibujar_zona_seguridad(ax, x, y, 0, alpha=0.2)

    # Dibujar camión
    dibujar_camion(ax, x, y, 0, color='#3498db', label='Camión (12m × 2.5m)')

    # Dimensiones del espacio
    # Largo total (16m)
    ax.plot([x-8, x+8], [y-5, y-5], 'r-', linewidth=3)
    ax.plot([x-8, x-8], [y-5.5, y-4.5], 'r-', linewidth=3)
    ax.plot([x+8, x+8], [y-5.5, y-4.5], 'r-', linewidth=3)
    ax.text(x, y-6.5, '16m (12m camión + 2×2m distanciamiento)',
            ha='center', fontsize=11, fontweight='bold', color='red')

    # Ancho total (6.5m)
    ax.plot([x+10, x+10], [y-3.25, y+3.25], 'b-', linewidth=3)
    ax.plot([x+9.5, x+10.5], [y-3.25, y-3.25], 'b-', linewidth=3)
    ax.plot([x+9.5, x+10.5], [y+3.25, y+3.25], 'b-', linewidth=3)
    ax.text(x+12, y, '6.5m\n(2.5m + 2×2m)',
            ha='left', va='center', fontsize=11, fontweight='bold',
            color='blue', rotation=90)

    # Distanciamiento de seguridad (2m)
    ax.annotate('', xy=(x-6, y-2), xytext=(x-8, y-2),
                arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
    ax.text(x-7, y-2.8, '2m\nseguridad', ha='center', fontsize=9,
            color='orange', fontweight='bold')

    # Configuración
    ax.set_xlim(0, 22)
    ax.set_ylim(-2, 18)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.set_xlabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_title('ESPACIO REQUERIDO POR CAMIÓN CON ZONA DE SEGURIDAD\n' +
                 'Área de estacionamiento: 16m × 6.5m = 104 m²',
                 fontsize=14, fontweight='bold', pad=20)

    # Leyenda
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

    # Información
    formula = r"""
    CÁLCULO DEL ESPACIO:

    Largo: $L_{espacio} = 12m + 2 \times 2m = 16m$
    Ancho: $A_{espacio} = 2.5m + 2 \times 2m = 6.5m$

    Área: $16m \times 6.5m = 104 m²$
    """
    ax.text(0.02, 0.98, formula, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig('./images/espacio_camion.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 2: espacio_camion.png generada")
    plt.close()


#=============================================================================
# IMAGEN 3a: MANIOBRA DE ENTRADA CON RADIO DE GIRO
#=============================================================================

def generar_maniobra_entrada():
    """Genera gráfica de maniobra de entrada con radio de giro"""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Área de parqueadero
    parqueadero = Rectangle((0, 0), 30, 20, facecolor='#ecf0f1',
                            edgecolor='#34495e', linewidth=3, alpha=0.3)
    ax.add_patch(parqueadero)
    ax.text(15, 19, 'ÁREA DE PARQUEADERO', ha='center', fontsize=11,
            fontweight='bold', color='#34495e')

    # Entrada
    entrada = Rectangle((-3, 8), 3, 4, facecolor='#27ae60',
                        edgecolor='#229954', linewidth=2, alpha=0.6)
    ax.add_patch(entrada)
    ax.text(-1.5, 10, 'ENTRADA', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Posición final del camión
    x_final, y_final = 15, 10
    dibujar_zona_seguridad(ax, x_final, y_final, 0)
    dibujar_camion(ax, x_final, y_final, 0, color='#3498db', label='Posición final')

    # Trayectoria de entrada
    trayectoria = [
        (-1.5, 10),
        (5, 10),
        (10, 10),
        (15, 10)
    ]
    dibujar_trayectoria(ax, trayectoria, color='#2ecc71', label='Ruta de entrada')

    # Camiones en posiciones intermedias (transparentes)
    dibujar_camion(ax, 5, 10, 0, color='#3498db', alpha=0.2)
    dibujar_camion(ax, 10, 10, 0, color='#3498db', alpha=0.3)

    # RADIO DE GIRO - Círculo de maniobra
    centro_giro = (5, 10)
    radio = RADIO_GIRO

    # Dibujar círculo de radio de giro
    circulo_giro = Circle(centro_giro, radio, facecolor='none',
                          edgecolor='#e67e22', linewidth=2.5,
                          linestyle='--', alpha=0.7, label=f'Radio de giro: {radio}m')
    ax.add_patch(circulo_giro)

    # Marcar centro
    ax.plot(centro_giro[0], centro_giro[1], 'o', color='#e67e22',
            markersize=10, markeredgecolor='#d35400', markeredgewidth=2)

    # Línea de radio
    ax.plot([centro_giro[0], centro_giro[0]+radio], [centro_giro[1], centro_giro[1]],
            'r-', linewidth=2.5)
    ax.text(centro_giro[0]+radio/2, centro_giro[1]+0.8, f'R = {radio}m',
            ha='center', fontsize=10, fontweight='bold', color='red',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Área de giro
    area_giro = np.pi * radio**2
    ax.text(centro_giro[0], centro_giro[1]+radio+2,
            f'Área de maniobra:\nπ × {radio}² ≈ {area_giro:.0f} m²',
            ha='center', fontsize=10, color='#e67e22', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Configuración
    ax.set_xlim(-5, 32)
    ax.set_ylim(-2, 22)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.set_xlabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_title('MANIOBRA DE ENTRADA - Análisis de Radio de Giro\n' +
                 'Cálculo: R_práctico = 0.6 × L_total = 0.6 × 12m = 8m',
                 fontsize=14, fontweight='bold', pad=20)

    # Leyenda
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

    # Fórmulas
    formulas = r"""
    RADIO DE GIRO:

    Teórico: $R = \frac{L}{\sin(45°)} = \frac{12}{0.707} \approx 17m$

    Práctico: $R_{práctico} = 0.6 \times L = 8m$

    Área: $A = \pi R^2 \approx 201 m²$
    """
    ax.text(0.02, 0.98, formulas, transform=ax.transAxes,
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig('./images/maniobra_entrada.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 3a: maniobra_entrada.png generada")
    plt.close()


#=============================================================================
# IMAGEN 3b: MANIOBRA DE SALIDA
#=============================================================================

def generar_maniobra_salida():
    """Genera gráfica de maniobra de salida"""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Área de parqueadero
    parqueadero = Rectangle((0, 0), 30, 20, facecolor='#ecf0f1',
                            edgecolor='#34495e', linewidth=3, alpha=0.3)
    ax.add_patch(parqueadero)

    # Salida
    salida = Rectangle((30, 8), 3, 4, facecolor='#e74c3c',
                       edgecolor='#c0392b', linewidth=2, alpha=0.6)
    ax.add_patch(salida)
    ax.text(31.5, 10, 'SALIDA', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Posición inicial del camión
    x_inicial, y_inicial = 15, 10
    dibujar_zona_seguridad(ax, x_inicial, y_inicial, 0, alpha=0.1)
    dibujar_camion(ax, x_inicial, y_inicial, 0, color='#e74c3c', label='Posición inicial')

    # Trayectoria de salida
    trayectoria = [
        (15, 10),
        (20, 10),
        (25, 10),
        (31.5, 10)
    ]
    dibujar_trayectoria(ax, trayectoria, color='#e74c3c', label='Ruta de salida')

    # Camiones en posiciones intermedias
    dibujar_camion(ax, 20, 10, 0, color='#e74c3c', alpha=0.3)
    dibujar_camion(ax, 25, 10, 0, color='#e74c3c', alpha=0.2)

    # Espacio de maniobra
    maniobra = Rectangle((12, 5), 10, 10, facecolor='yellow',
                         edgecolor='orange', linewidth=2, linestyle='--', alpha=0.15)
    ax.add_patch(maniobra)
    ax.text(17, 15.5, 'Espacio de maniobra\n10m × 10m = 100 m²',
            ha='center', fontsize=10, color='orange', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Configuración
    ax.set_xlim(-2, 35)
    ax.set_ylim(-2, 22)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.set_xlabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_title('MANIOBRA DE SALIDA - Análisis de Espacio Requerido\n' +
                 'Distanciamiento de seguridad: 2m perimetral',
                 fontsize=14, fontweight='bold', pad=20)

    # Leyenda
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

    plt.tight_layout()
    plt.savefig('./images/maniobra_salida.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 3b: maniobra_salida.png generada")
    plt.close()


#=============================================================================
# IMAGEN 3c: MANIOBRABILIDAD COMPLETA
#=============================================================================

def generar_maniobrabilidad_completa():
    """Genera gráfica completa de maniobrabilidad"""
    fig, ax = plt.subplots(figsize=(16, 12))

    # Rectángulos del parqueadero (forma de C)
    # Rectángulo A
    rect_a = Rectangle((0, 20), 20, 10, facecolor='#d5dbdb',
                       edgecolor='#34495e', linewidth=2.5, alpha=0.4)
    ax.add_patch(rect_a)
    ax.text(10, 25, 'A\n20×10m', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#2c3e50')

    # Rectángulo B
    rect_b = Rectangle((0, 10), 15, 10, facecolor='#fcf3cf',
                       edgecolor='#f39c12', linewidth=2.5, alpha=0.4)
    ax.add_patch(rect_b)
    ax.text(7.5, 15, 'B\n15×10m\n(PASILLO)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#d68910')

    # Rectángulo C
    rect_c = Rectangle((0, 0), 20, 10, facecolor='#d5dbdb',
                       edgecolor='#34495e', linewidth=2.5, alpha=0.4)
    ax.add_patch(rect_c)
    ax.text(10, 5, 'C\n20×10m', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#2c3e50')

    # Camiones de ejemplo
    dibujar_camion(ax, 10, 25, 0, color='#3498db', alpha=0.6)
    dibujar_camion(ax, 10, 5, 0, color='#3498db', alpha=0.6)

    # Entrada
    entrada = Rectangle((-3, 13), 3, 4, facecolor='#27ae60',
                        edgecolor='#229954', linewidth=2, alpha=0.6)
    ax.add_patch(entrada)
    ax.text(-1.5, 15, 'IN', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Salida
    salida = Rectangle((20, 13), 3, 4, facecolor='#e74c3c',
                       edgecolor='#c0392b', linewidth=2, alpha=0.6)
    ax.add_patch(salida)
    ax.text(21.5, 15, 'OUT', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Trayectorias
    trayectoria_entrada = [(-1.5, 15), (7.5, 15), (10, 25)]
    dibujar_trayectoria(ax, trayectoria_entrada, color='#2ecc71', label='Entrada')

    trayectoria_salida = [(10, 5), (15, 15), (21.5, 15)]
    dibujar_trayectoria(ax, trayectoria_salida, color='#e74c3c', label='Salida')

    # Configuración
    ax.set_xlim(-5, 25)
    ax.set_ylim(-2, 32)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.set_xlabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_title('MANIOBRABILIDAD COMPLETA DEL PARQUEADERO\n' +
                 'Entrada, Salida y Espacios de Circulación',
                 fontsize=14, fontweight='bold', pad=20)

    # Leyenda
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

    # Información
    info = """
    REQUERIMIENTOS:
    • Pasillo circulación: 4-5m
    • Radio de giro: 8m
    • Zona seguridad: 2m
    • Área total: 550 m²
    """
    ax.text(0.02, 0.98, info, transform=ax.transAxes,
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9),
            family='monospace')

    plt.tight_layout()
    plt.savefig('./images/maniobrabilidad_completa.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 3c: maniobrabilidad_completa.png generada")
    plt.close()


#=============================================================================
# CONTINÚA EN LA SIGUIENTE PARTE...
#=============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("GENERANDO IMÁGENES DEL PROYECTO - PARTE 1/2")
    print("="*70 + "\n")

    generar_terreno_actual()
    generar_espacio_camion()
    generar_maniobra_entrada()
    generar_maniobra_salida()
    generar_maniobrabilidad_completa()

    print("\n" + "="*70)
    print("✅ PARTE 1/2 COMPLETADA")
    print("="*70 + "\n")
