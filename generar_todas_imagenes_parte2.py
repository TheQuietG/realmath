"""
Script completo para generar TODAS las imágenes del proyecto - PARTE 2/2
Análisis de Parqueadero Rodrish S.A.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Configuración global
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 10

# Constantes
CAMION_LARGO = 12
CAMION_ANCHO = 2.5
DISTANCIAMIENTO = 2
ESPACIO_LARGO = 16
ESPACIO_ANCHO = 6.5
AREA_POR_CAMION = 104
FACTOR_MANIOBRAS = 1.44
AREA_ACTUAL = 550

import os
os.makedirs('./images', exist_ok=True)

def calcular_ampliacion_necesaria(num_camiones, area_actual=550, area_por_camion=104,
                                   factor_maniobra=1.44):
    """Ecuación lineal para calcular ampliación necesaria"""
    area_necesaria = num_camiones * area_por_camion * factor_maniobra
    ampliacion = area_necesaria - area_actual
    return max(0, ampliacion)

def dibujar_camion(ax, x, y, angulo, color='#3498db', label=None, alpha=1.0):
    """Dibuja un camión"""
    largo, ancho = CAMION_LARGO, CAMION_ANCHO
    vertices = np.array([[-largo/2, -ancho/2], [largo/2, -ancho/2],
                         [largo/2, ancho/2], [-largo/2, ancho/2]])
    theta = np.radians(angulo)
    rot_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                           [np.sin(theta), np.cos(theta)]])
    vertices_rot = vertices @ rot_matrix.T
    vertices_final = vertices_rot + np.array([x, y])
    camion = Polygon(vertices_final, facecolor=color, edgecolor='#2c3e50',
                     linewidth=2, alpha=alpha, label=label)
    ax.add_patch(camion)
    return camion

#=============================================================================
# IMAGEN 4a: ECUACIÓN LINEAL
#=============================================================================

def generar_ecuacion_lineal():
    """Genera gráfica de la ecuación lineal"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Rango de camiones
    num_camiones = np.arange(1, 21)
    ampliacion_necesaria = [calcular_ampliacion_necesaria(n) for n in num_camiones]

    # Graficar
    ax.plot(num_camiones, ampliacion_necesaria, 'o-', linewidth=3,
            markersize=8, color='#e74c3c', label='A_amp = 149.76n - 550')

    # Punto para 5 camiones (capacidad simultánea requerida)
    amp_5 = calcular_ampliacion_necesaria(5)
    ax.plot(5, amp_5, 'D', markersize=15, color='#2ecc71',
            markeredgecolor='#27ae60', markeredgewidth=2,
            label=f'5 camiones simultáneos\n(Requiere {amp_5:.1f}m²)', zorder=10)

    # Punto de referencia para 15 camiones (total de la flota)
    amp_15 = calcular_ampliacion_necesaria(15)
    ax.plot(15, amp_15, 'o', markersize=12, color='#95a5a6',
            markeredgecolor='#7f8c8d', markeredgewidth=2,
            label=f'15 camiones (flota completa)\n(Requeriría {amp_15:.1f}m²)', zorder=9)

    # Anotaciones
    ax.annotate(f'Solución óptima:\n5 camiones → {amp_5:.0f}m²',
                xy=(5, amp_5), xytext=(8, amp_5 + 150),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2),
                fontsize=10, fontweight='bold', color='#27ae60',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.annotate(f'Flota completa:\n15 camiones → {amp_15:.0f}m²\n(no simultáneos)',
                xy=(15, amp_15), xytext=(12, amp_15 + 200),
                arrowprops=dict(arrowstyle='->', color='#95a5a6', lw=1.5),
                fontsize=9, color='#7f8c8d',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    # Configuración
    ax.set_xlabel('Número de camiones (n)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Ampliación necesaria (m²)', fontsize=12, fontweight='bold')
    ax.set_title('ECUACIÓN LINEAL: Ampliación Necesaria vs Número de Camiones\n' +
                 r'$A_{ampliación} = 149.76n - 550$',
                 fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

    # Ecuación
    ecuacion_text = r"""
    ECUACIÓN LINEAL:
    $A_{amp} = (n \times a \times f) - A_{actual}$

    Donde:
    • n = número de camiones
    • a = 104 m²
    • f = 1.44 (factor maniobras)
    • $A_{actual}$ = 550 m²

    Resultado:
    $A_{amp} = 149.76n - 550$
    """
    ax.text(0.98, 0.35, ecuacion_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig('./images/ecuacion_lineal_ampliacion.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 4a: ecuacion_lineal_ampliacion.png generada")
    plt.close()


#=============================================================================
# IMAGEN 4b: TABLA DE AMPLIACIÓN
#=============================================================================

def generar_tabla_ampliacion():
    """Genera tabla con valores de ampliación"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('tight')
    ax.axis('off')

    # Datos
    num_camiones_lista = [3, 5, 8, 10, 12, 15, 18, 20]
    datos_tabla = []

    for n in num_camiones_lista:
        area_necesaria = n * 104 * 1.44
        ampliacion = calcular_ampliacion_necesaria(n)
        area_total = 550 + ampliacion

        datos_tabla.append([
            n, f"{area_necesaria:.0f}", f"{ampliacion:.0f}",
            f"{area_total:.0f}"
        ])

    # Crear tabla
    columnas = ['N° Camiones', 'Área Necesaria\n(m²)', 'Ampliación\nRequerida (m²)',
                'Área Total\n(m²)']

    tabla = ax.table(cellText=datos_tabla, colLabels=columnas,
                     cellLoc='center', loc='center',
                     colWidths=[0.2, 0.27, 0.27, 0.26])

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(11)
    tabla.scale(1, 2.5)

    # Estilo
    for i in range(len(columnas)):
        tabla[(0, i)].set_facecolor('#34495e')
        tabla[(0, i)].set_text_props(weight='bold', color='white')

    for i in range(1, len(datos_tabla) + 1):
        for j in range(len(columnas)):
            if i % 2 == 0:
                tabla[(i, j)].set_facecolor('#ecf0f1')
            else:
                tabla[(i, j)].set_facecolor('white')

            # Resaltar 5 camiones (solución óptima)
            if datos_tabla[i-1][0] == 5:
                tabla[(i, j)].set_facecolor('#d5f4e6')
                tabla[(i, j)].set_text_props(weight='bold', color='#27ae60')

    # Título
    ax.set_title('TABLA DE AMPLIACIÓN NECESARIA SEGÚN ECUACIÓN LINEAL\n' +
                 r'Basado en: $A_{amp} = 149.76n - 550$',
                 fontsize=14, fontweight='bold', pad=20)

    # Nota
    nota = ("NOTA: La ecuación considera factor 1.44 para incluir espacio de maniobras.\n"
            "Área base: 550m² | Área estacionamiento/camión: 104m² | Área real/camión (con maniobras): 150m²\n"
            "SOLUCIÓN: La flota de 15 camiones opera en batches de 5 (16h fuera + 8h dentro) → Requiere ampliación de 198.8m²")
    fig.text(0.5, 0.05, nota, ha='center', fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='#d5f4e6', alpha=0.9))

    plt.savefig('./images/tabla_ampliacion_lineal.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 4b: tabla_ampliacion_lineal.png generada")
    plt.close()


#=============================================================================
# IMAGEN 5: COMPARACIÓN DE ÁREAS
#=============================================================================

def generar_comparacion():
    """Genera comparación visual de áreas"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Datos
    areas = [550, 748.8, 198.8, 2246.4]
    labels = ['Área\nActual', 'Área\nRequerida\n(5 cam.)', 'Ampliación\nNecesaria\n(5 cam.)', 'Área para\n15 cam.\n(referencia)']
    colors = ['#3498db', '#2ecc71', '#f39c12', '#95a5a6']

    # Gráfico de barras
    bars = ax.bar(range(len(areas)), areas, color=colors, alpha=0.7,
                  edgecolor='black', linewidth=2)

    # Valores sobre las barras
    for i, (bar, area) in enumerate(zip(bars, areas)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 50,
                f'{area:.1f} m²', ha='center', va='bottom',
                fontsize=12, fontweight='bold')

    # Configuración
    ax.set_ylabel('Área (m²)', fontsize=12, fontweight='bold')
    ax.set_title('COMPARACIÓN DE ÁREAS DEL PARQUEADERO\n' +
                 'Análisis: Solución Optimizada con Batches de Camiones',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=11, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle=':', linewidth=1)

    # Anotaciones
    # Flecha mostrando la ampliación necesaria
    ax.annotate('', xy=(1, 748.8), xytext=(1, 550),
                arrowprops=dict(arrowstyle='<->', color='#27ae60', lw=3))
    ax.text(1.3, 650, 'Ampliación:\n198.8 m²', fontsize=11,
            color='#27ae60', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Información
    info = """
    SOLUCIÓN OPTIMIZADA:
    • 15 camiones en la flota
    • 5 camiones simultáneos (batches)
    • Ciclo: 16h fuera + 8h dentro
    • Área actual: 550 m²
    • Ampliación necesaria: 198.8 m²
    • Área total: 748.8 m²
    """
    ax.text(0.02, 0.98, info, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='#d5f4e6', alpha=0.9),
            family='monospace')

    plt.tight_layout()
    plt.savefig('./images/comparacion.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 5: comparacion.png generada")
    plt.close()


#=============================================================================
# IMAGEN 6: CONFIGURACIONES DE AMPLIACIÓN
#=============================================================================

def generar_configuraciones_ampliacion():
    """Genera visualización de 3 configuraciones de ampliación"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    configuraciones = [
        {
            'nombre': 'Configuración 1\nJunto a B',
            'color_b': '#2ecc71',
            'ampliacion': (15, 10, 19.88, 10),  # (x, y, ancho, alto) ~200m²
            'resultado': '~35m × 10m\nUNIFORME\n✅',
            'capacidad': '5 camiones'
        },
        {
            'nombre': 'Configuración 2\nJunto a A',
            'color_b': '#2ecc71',
            'ampliacion': (20, 20, 19.88, 10),  # ~200m²
            'resultado': '~40m × 10m\nUNIFORME\n✅',
            'capacidad': '5 camiones'
        },
        {
            'nombre': 'Configuración 3\nCuadrada',
            'color_b': '#f9e79f',
            'ampliacion': (15, 10, 14.1, 14.1),  # ~200m²
            'resultado': '~14 × 14m\nREGULAR\n⚠️',
            'capacidad': '5 camiones'
        }
    ]

    for idx, (ax, config) in enumerate(zip(axes, configuraciones)):
        # Rectángulos base
        rect_a = Rectangle((0, 20), 20, 10, facecolor='#aed6f1',
                           edgecolor='#2874a6', linewidth=2, alpha=0.5)
        ax.add_patch(rect_a)
        ax.text(10, 25, 'A\n200m²', ha='center', va='center',
                fontsize=9, fontweight='bold')

        rect_b = Rectangle((0, 10), 15, 10, facecolor=config['color_b'],
                           edgecolor='#f39c12', linewidth=2, alpha=0.5)
        ax.add_patch(rect_b)
        ax.text(7.5, 15, 'B\n150m²', ha='center', va='center',
                fontsize=9, fontweight='bold')

        rect_c = Rectangle((0, 0), 20, 10, facecolor='#aed6f1',
                           edgecolor='#2874a6', linewidth=2, alpha=0.5)
        ax.add_patch(rect_c)
        ax.text(10, 5, 'C\n200m²', ha='center', va='center',
                fontsize=9, fontweight='bold')

        # Ampliación
        x, y, w, h = config['ampliacion']
        ampliacion = Rectangle((x, y), w, h, facecolor='#e74c3c',
                               edgecolor='#c0392b', linewidth=3, alpha=0.6)
        ax.add_patch(ampliacion)
        ax.text(x + w/2, y + h/2, 'AMPLIACIÓN\n~200m²',
                ha='center', va='center', fontsize=8,
                fontweight='bold', color='white')

        # Configuración
        ax.set_xlim(-2, 45)
        ax.set_ylim(-2, 32)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.2)
        ax.set_title(f"{config['nombre']}\n{config['resultado']}\nCapacidad: {config['capacidad']}",
                     fontsize=10, fontweight='bold', pad=10)

    fig.suptitle('CONFIGURACIONES POSIBLES DE AMPLIACIÓN (~200m²)\n' +
                 'Basado en ecuación para 5 camiones simultáneos',
                 fontsize=14, fontweight='bold')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('./images/configuraciones_ampliacion.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 6: configuraciones_ampliacion.png generada")
    plt.close()


#=============================================================================
# IMAGEN 7: SOLUCIÓN OPTIMIZADA CON ~200m²
#=============================================================================

def generar_solucion_optimizada():
    """Genera visualización de la solución optimizada"""
    fig, ax = plt.subplots(figsize=(16, 12))

    # Rect A
    rect_a = Rectangle((0, 20), 20, 10, facecolor='#aed6f1',
                       edgecolor='#2874a6', linewidth=3, alpha=0.5)
    ax.add_patch(rect_a)
    ax.text(10, 29, 'RECTÁNGULO A\n20m × 10m = 200 m²',
            ha='center', va='top', fontsize=10, fontweight='bold',
            color='#1a5490')

    # Rect B EXPANDIDO (~35m con ampliación)
    rect_b = Rectangle((0, 10), 34.88, 10, facecolor='#2ecc71',
                       edgecolor='#27ae60', linewidth=3, alpha=0.5)
    ax.add_patch(rect_b)
    ax.text(17.5, 15, 'RECTÁNGULO B (EXPANDIDO)\n~35m × 10m = 350 m²\n✅ UNIFORME',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color='#1e8449')

    # Indicador de ampliación en B
    amp_indicator = Rectangle((15, 10), 19.88, 10, facecolor='none',
                              edgecolor='red', linewidth=3, linestyle='--')
    ax.add_patch(amp_indicator)
    ax.text(25, 9, '+198.8m²', ha='center', fontsize=9, fontweight='bold',
            color='red', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Rect C
    rect_c = Rectangle((0, 0), 20, 10, facecolor='#aed6f1',
                       edgecolor='#2874a6', linewidth=3, alpha=0.5)
    ax.add_patch(rect_c)
    ax.text(10, 1, 'RECTÁNGULO C\n20m × 10m = 200 m²',
            ha='center', va='bottom', fontsize=10, fontweight='bold',
            color='#1a5490')

    # Camiones (5 camiones distribuidos)
    # Zona A - 2 camiones
    dibujar_camion(ax, 6, 25, 0, color='#3498db', alpha=0.7)
    dibujar_camion(ax, 14, 25, 0, color='#3498db', alpha=0.7)

    # Zona B - 2 camiones
    dibujar_camion(ax, 8, 15, 0, color='#3498db', alpha=0.7)
    dibujar_camion(ax, 20, 15, 0, color='#3498db', alpha=0.7)

    # Zona C - 1 camión
    dibujar_camion(ax, 10, 5, 0, color='#3498db', alpha=0.7)

    # Numeración
    for i, (x, y) in enumerate([(6, 25), (14, 25), (8, 15), (20, 15), (10, 5)], 1):
        ax.text(x, y, str(i), ha='center', va='center',
                fontsize=14, fontweight='bold', color='white',
                bbox=dict(boxstyle='circle', facecolor='red', alpha=0.8))

    # Configuración
    ax.set_xlim(-3, 38)
    ax.set_ylim(-2, 32)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.set_xlabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=12, fontweight='bold')
    ax.set_title('SOLUCIÓN OPTIMIZADA CON ~200m² DE AMPLIACIÓN\n' +
                 'Configuración para 5 camiones simultáneos (batches)\n' +
                 'Área total: 748.8m² | Inversión: ~$18,373',
                 fontsize=14, fontweight='bold', pad=20)

    # Información
    info = """
    SOLUCIÓN ÓPTIMA:
    • Ampliación: ~20m × 10m = 198.8 m²
    • Ubicación: Junto a B
    • Resultado: Área uniforme de 10m
    • Capacidad: 5 camiones simultáneos
    • Batches: 3 grupos de 5 camiones
    • Ciclo: 16h fuera + 8h dentro
    • Inversión: ~$18,373
    • Cubre 100% necesidades operativas
    """
    ax.text(0.02, 0.98, info, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='#d5f4e6', alpha=0.9),
            family='monospace')

    plt.tight_layout()
    plt.savefig('./images/solucion_optimizada.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 7: solucion_optimizada.png generada")
    plt.close()


#=============================================================================
# IMÁGENES 8a-c: OPCIONES DE DISTRIBUCIÓN
#=============================================================================

def dibujar_zona_seguridad(ax, x, y, angulo=0, color='yellow', alpha=0.2):
    """Dibuja zona de seguridad alrededor de un camión (16m × 6.5m)"""
    largo = 16  # 12m camión + 2m adelante + 2m atrás
    ancho = 6.5  # 2.5m camión + 2m izq + 2m der

    # Crear polígono de la zona
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

    # Dibujar zona
    from matplotlib.patches import Polygon
    zona = Polygon(vertices_final, facecolor=color, edgecolor='orange',
                   linewidth=1.5, alpha=alpha, linestyle='--')
    ax.add_patch(zona)

def generar_opciones():
    """Genera las 3 opciones de distribución con espaciamiento HSE correcto"""

    # OPCIÓN 1: SIN AMPLIACIÓN - Solo con 550 m² actuales
    # Capacidad: 3 camiones máximo (espaciados adecuadamente)
    fig, ax = plt.subplots(figsize=(14, 10))

    # Rectángulos base (550 m² total)
    for (x, y, w, h, label, area, color) in [
        (0, 20, 20, 10, 'A', '200m²', '#d5dbdb'),
        (0, 10, 15, 10, 'B', '150m²', '#f9e79f'),  # Original sin ampliar
        (0, 0, 20, 10, 'C', '200m²', '#d5dbdb')
    ]:
        rect = Rectangle((x, y), w, h, facecolor=color,
                         edgecolor='#34495e', linewidth=2, alpha=0.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, f'{label}\n{area}',
                ha='center', va='center', fontsize=10, fontweight='bold')

    # 3 camiones con zonas de seguridad (1 por rectángulo)
    posiciones = [
        (10, 25),  # A
        (7.5, 15),  # B
        (10, 5)    # C
    ]

    for i, (x, y) in enumerate(posiciones, 1):
        dibujar_zona_seguridad(ax, x, y, 0, color='yellow', alpha=0.15)
        dibujar_camion(ax, x, y, 0, color='#3498db', alpha=0.8)
        ax.text(x, y, str(i), ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')

    ax.set_xlim(-2, 25)
    ax.set_ylim(-2, 32)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Distancia (metros)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=11, fontweight='bold')
    ax.set_title('OPCIÓN 1: Sin Ampliación (550 m²)\n' +
                 '3 camiones con distanciamiento HSE de 2m',
                 fontsize=13, fontweight='bold', pad=15)

    # Leyenda
    info = "• Área disponible: 550 m²\n• Capacidad: 3 camiones\n• Sin inversión\n• Zonas amarillas: seguridad 2m"
    ax.text(0.02, 0.98, info, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig('./images/opcion1.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 8a: opcion1.png generada")
    plt.close()

    # OPCIÓN 2: CON AMPLIACIÓN DE 198.8 m² - SOLUCIÓN ÓPTIMA
    # Capacidad: 5 camiones simultáneos (batches)
    fig, ax = plt.subplots(figsize=(16, 10))

    # Rectángulos con ampliación
    for (x, y, w, h, label, area, color) in [
        (0, 20, 20, 10, 'A', '200m²', '#aed6f1'),
        (0, 10, 34.88, 10, 'B (expandido)', '~350m²', '#d5f4e6'),  # Con ampliación
        (0, 0, 20, 10, 'C', '200m²', '#aed6f1')
    ]:
        rect = Rectangle((x, y), w, h, facecolor=color,
                         edgecolor='#2874a6', linewidth=2.5, alpha=0.6)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, f'{label}\n{area}',
                ha='center', va='center', fontsize=10, fontweight='bold')

    # Indicador de ampliación
    amp_rect = Rectangle((15, 10), 19.88, 10, facecolor='none',
                          edgecolor='red', linewidth=3, linestyle='--')
    ax.add_patch(amp_rect)
    ax.text(25, 9, '+198.8m²', ha='center', fontsize=9, fontweight='bold',
            color='red', bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))

    # 5 camiones distribuidos con zonas de seguridad
    # En A: 2 camiones lado a lado (comparten espacio de 2m entre ellos)
    # Cálculo: camión 1 centro a 6m, camión 2 centro a 14m (separación de 8m)
    # Cada camión mide 2.5m de ancho, más 2m de seguridad = distancia mínima centro a centro: 2.5 + 2 + 2.5 = 7m
    posiciones_optima = [
        (6, 25),    # A1
        (14, 25),   # A2 (separado 8m del centro, suficiente para 2m de distancia)
        (8, 15),    # B1
        (22, 15),   # B2
        (10, 5)     # C1
    ]

    for i, (x, y) in enumerate(posiciones_optima, 1):
        dibujar_zona_seguridad(ax, x, y, 0, color='lightgreen', alpha=0.15)
        dibujar_camion(ax, x, y, 0, color='#2ecc71', alpha=0.8)
        ax.text(x, y, str(i), ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')

    ax.set_xlim(-2, 38)
    ax.set_ylim(-2, 32)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Distancia (metros)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=11, fontweight='bold')
    ax.set_title('OPCIÓN 2: Con Ampliación de 198.8 m² (ÓPTIMA)\n' +
                 '5 camiones simultáneos - Cumple 100% necesidades operativas - ✅ RECOMENDADA',
                 fontsize=13, fontweight='bold', pad=15, color='#27ae60')

    # Leyenda
    info = ("• Área total: 748.8 m² (550 + 198.8)\n"
            "• Capacidad: 5 camiones simultáneos\n"
            "• Inversión: ~$18,373\n"
            "• Batches: 3 grupos de 5\n"
            "• Zonas verdes: seguridad 2m HSE")
    ax.text(0.02, 0.98, info, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='#d5f4e6', alpha=0.9))

    plt.tight_layout()
    plt.savefig('./images/opcion2.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 8b: opcion2.png generada")
    plt.close()

    # OPCIÓN 3: DISTRIBUCIÓN ALTERNATIVA CON ÁREAS ACTUALES
    # 4 camiones con pasillos más amplios
    fig, ax = plt.subplots(figsize=(14, 10))

    # Rectángulos base
    for (x, y, w, h, label, area, color) in [
        (0, 20, 20, 10, 'A', '200m²', '#d5dbdb'),
        (0, 10, 15, 10, 'B (pasillo)', '150m²', '#fcf3cf'),
        (0, 0, 20, 10, 'C', '200m²', '#d5dbdb')
    ]:
        rect = Rectangle((x, y), w, h, facecolor=color,
                         edgecolor='#34495e', linewidth=2, alpha=0.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, f'{label}\n{area}',
                ha='center', va='center', fontsize=10, fontweight='bold')

    # Pasillo central en B
    pasillo_rect = Rectangle((3, 10), 9, 10, facecolor='none',
                              edgecolor='orange', linewidth=2.5, linestyle=':')
    ax.add_patch(pasillo_rect)
    ax.text(7.5, 15, 'PASILLO\nMANIOBRAS\n5m', ha='center', va='center',
            fontsize=9, color='orange', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # 4 camiones: 2 en A, 0 en B (pasillo), 2 en C
    posiciones_alt = [
        (6, 25),    # A1
        (14, 25),   # A2
        (6, 5),     # C1
        (14, 5)     # C2
    ]

    for i, (x, y) in enumerate(posiciones_alt, 1):
        dibujar_zona_seguridad(ax, x, y, 0, color='lightyellow', alpha=0.15)
        dibujar_camion(ax, x, y, 0, color='#f39c12', alpha=0.8)
        ax.text(x, y, str(i), ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')

    ax.set_xlim(-2, 25)
    ax.set_ylim(-2, 32)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Distancia (metros)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Distancia (metros)', fontsize=11, fontweight='bold')
    ax.set_title('OPCIÓN 3: Con Pasillo Central de Maniobras\n' +
                 '4 camiones - Prioriza espacio de circulación',
                 fontsize=13, fontweight='bold', pad=15)

    # Leyenda
    info = "• Área: 550 m²\n• Capacidad: 4 camiones\n• B usado como pasillo\n• Mayor espacio de maniobra"
    ax.text(0.02, 0.98, info, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig('./images/opcion3.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 8c: opcion3.png generada")
    plt.close()


#=============================================================================
# IMAGEN 9: TABLA COMPARATIVA
#=============================================================================

def generar_tabla_comparativa():
    """Genera tabla comparativa de opciones"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('tight')
    ax.axis('off')

    datos = [
        ['Opción 1', 'Sin ampliación\n(550 m²)', '3', 'Distanciamiento\nHSE correcto', 'Sin inversión', 'Base actual'],
        ['Opción 2', 'Con ampliación\n(748.8 m²)', '5', 'Cumple normas\nHSE + batches', '~$18,373', '✅ ÓPTIMA - 100% necesidades'],
        ['Opción 3', 'Pasillo central\n(550 m²)', '4', 'Prioriza\nmaniobras', 'Sin inversión', 'Mayor circulación']
    ]

    columnas = ['Opción', 'Configuración', 'Camiones\nSimultáneos', 'Seguridad HSE',
                'Inversión', 'Observación']

    tabla = ax.table(cellText=datos, colLabels=columnas,
                     cellLoc='center', loc='center',
                     colWidths=[0.12, 0.20, 0.14, 0.18, 0.13, 0.23])

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1, 2.5)

    # Estilo
    for i in range(len(columnas)):
        tabla[(0, i)].set_facecolor('#34495e')
        tabla[(0, i)].set_text_props(weight='bold', color='white')

    for i in range(1, 4):
        for j in range(len(columnas)):
            if i == 2:  # Opción 2 (óptima)
                tabla[(i, j)].set_facecolor('#d5f4e6')
                tabla[(i, j)].set_text_props(weight='bold')
            elif i % 2 == 0:
                tabla[(i, j)].set_facecolor('#ecf0f1')
            else:
                tabla[(i, j)].set_facecolor('white')

    ax.set_title('TABLA COMPARATIVA DE OPCIONES EVALUADAS\n' +
                 'Análisis con Distanciamiento HSE de 2m (Bidireccional)',
                 fontsize=14, fontweight='bold', pad=20)

    # Nota al pie
    nota = ("NOTA: Todas las opciones cumplen normas HSE con distanciamiento de 2m bidireccional.\n"
            "Opción 2 requiere ampliación de 198.8m² calculada con ecuación: A_amp = 149.76n - 550\n"
            "Sistema de batches: 15 camiones en 3 grupos de 5 (16h fuera + 8h dentro)")
    fig.text(0.5, 0.05, nota, ha='center', fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='#d5f4e6', alpha=0.9))

    plt.savefig('./images/tabla_comparativa.png', dpi=150, bbox_inches='tight')
    print("✅ Imagen 9: tabla_comparativa.png generada")
    plt.close()


#=============================================================================
# MAIN
#=============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("GENERANDO IMÁGENES DEL PROYECTO - PARTE 2/2")
    print("="*70 + "\n")

    generar_ecuacion_lineal()
    generar_tabla_ampliacion()
    generar_comparacion()
    generar_configuraciones_ampliacion()
    generar_solucion_optimizada()
    generar_opciones()
    generar_tabla_comparativa()

    print("\n" + "="*70)
    print("✅ PARTE 2/2 COMPLETADA")
    print("✅ TODAS LAS IMÁGENES GENERADAS EXITOSAMENTE")
    print("="*70 + "\n")
