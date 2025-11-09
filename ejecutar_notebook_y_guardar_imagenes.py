#!/usr/bin/env python3
"""
Script para ejecutar el notebook Parqueadero_Rodrish_Analisis.ipynb
y guardar automáticamente todas las figuras generadas.

Diseñado para ejecutarse en GitHub Codespaces o cualquier entorno Linux con Python.
"""

import os
import sys
import json
import warnings
warnings.filterwarnings('ignore')

# Configurar matplotlib para modo no interactivo (sin display)
import matplotlib
matplotlib.use('Agg')  # Backend sin GUI
import matplotlib.pyplot as plt

print("="*70)
print("EJECUTANDO NOTEBOOK Y GUARDANDO IMÁGENES")
print("="*70)

# Crear carpeta de imágenes
os.makedirs('images', exist_ok=True)
print("✓ Carpeta images/ creada/verificada")

# Importar dependencias del notebook
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle, Circle, Polygon, Arc

# Configurar matplotlib
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 11

print("✓ Dependencias importadas")

# ============================================================================
# EJECUTAR EL NOTEBOOK CELDA POR CELDA
# ============================================================================

print("\n" + "="*70)
print("EJECUTANDO CELDAS DEL NOTEBOOK")
print("="*70)

# Leer el notebook
notebook_path = 'Parqueadero_Rodrish_Analisis.ipynb'
print(f"\nLeyendo: {notebook_path}")

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
except FileNotFoundError:
    print(f"❌ ERROR: No se encontró {notebook_path}")
    print("   Asegúrate de estar en la carpeta correcta del repositorio")
    sys.exit(1)

print(f"✓ Notebook cargado: {len(notebook['cells'])} celdas")

# Mapeo CORRECTO de figuras a nombres de archivo
# Basado en el orden REAL de generación
figura_nombres = {
    1: ('terreno_actual.png', 'Terreno actual (celda 6)'),
    2: ('espacio_camion.png', 'Espacio requerido por camión (celda 8)'),
    3: ('comparacion.png', 'Comparación de áreas (celda 10)'),
    4: ('optimizacion_ampliacion.png', 'Análisis de optimización (celda 12)'),
    5: ('opcion1.png', 'Opción 1 - Distribución básica (celda 14)'),
    6: ('tabla_comparativa.png', 'Tabla comparativa (celda 15)'),
    7: ('opcion2.png', 'Opción 2 - Solución óptima compacta (celda 16)'),
    8: ('opcion3.png', 'Opción 3 - Solución realista (celda 18)'),
    9: ('opcion4.png', 'Opción 4 - Con pasillos (celda 19)'),
    10: ('solucion_realista.png', 'Opción 2 (celda 20)'),
    # Nota: La celda 21 (rotación 90°) podría no generar figura si hay error
}

# Namespace global para ejecutar el código
global_namespace = {
    '__name__': '__main__',
    'np': np,
    'pd': pd,
    'plt': plt,
    'Rectangle': Rectangle,
    'Circle': Circle,
    'Polygon': Polygon,
    'Arc': Arc,
    'warnings': warnings,
}

# Ejecutar celdas de código
codigo_ejecutado = 0
figuras_generadas = 0

print("\nEjecutando celdas...")

for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        # Obtener el código fuente
        source = cell['source']
        if isinstance(source, list):
            codigo = ''.join(source)
        else:
            codigo = source

        # Saltar celdas vacías o de instalación
        if not codigo.strip():
            continue
        if 'pip install' in codigo and '!{sys.executable}' in codigo:
            print(f"  Celda {i}: Saltando instalación de paquetes")
            continue

        try:
            # Ejecutar el código
            exec(codigo, global_namespace)
            codigo_ejecutado += 1

            # Verificar si se generó una nueva figura
            figuras_actuales = plt.get_fignums()
            if len(figuras_actuales) > figuras_generadas:
                nueva_figura = figuras_actuales[-1]
                if nueva_figura in figura_nombres:
                    nombre_archivo, descripcion = figura_nombres[nueva_figura]
                    ruta = os.path.join('images', nombre_archivo)

                    fig = plt.figure(nueva_figura)
                    fig.savefig(ruta, dpi=300, bbox_inches='tight', facecolor='white')
                    print(f"  ✓ Celda {i}: Guardada → {nombre_archivo}")
                    figuras_generadas = len(figuras_actuales)
                else:
                    print(f"  • Celda {i}: Figura {nueva_figura} generada (no mapeada)")
                    figuras_generadas = len(figuras_actuales)

        except Exception as e:
            # Algunos errores pueden ser esperados (ej: comandos de Jupyter)
            if 'matplotlib inline' in codigo or '%' in codigo:
                print(f"  - Celda {i}: Comando de Jupyter (saltado)")
            elif 'print(' in codigo and len(codigo) < 200:
                # Celdas de impresión simples - ejecutar sin mostrar error
                pass
            else:
                print(f"  ⚠ Celda {i}: Error (continuando) - {str(e)[:50]}")

print(f"\n✓ Celdas ejecutadas: {codigo_ejecutado}")
print(f"✓ Figuras detectadas: {len(plt.get_fignums())}")

# ============================================================================
# GUARDAR TODAS LAS FIGURAS RESTANTES
# ============================================================================

print("\n" + "="*70)
print("GUARDANDO FIGURAS FINALES")
print("="*70)

figuras_guardadas = []

for num_fig in plt.get_fignums():
    if num_fig in figura_nombres:
        nombre_archivo, descripcion = figura_nombres[num_fig]
        ruta = os.path.join('images', nombre_archivo)

        # Siempre sobreescribir
        fig = plt.figure(num_fig)
        fig.savefig(ruta, dpi=300, bbox_inches='tight', facecolor='white')

        # Verificar tamaño del archivo
        tamaño_kb = os.path.getsize(ruta) / 1024
        print(f"✓ {nombre_archivo:30s} ({tamaño_kb:6.1f} KB) - {descripcion}")
        figuras_guardadas.append(nombre_archivo)

# ============================================================================
# RESUMEN
# ============================================================================

print("\n" + "="*70)
print("RESUMEN")
print("="*70)

print(f"\n📊 Figuras guardadas: {len(figuras_guardadas)}/{len(figura_nombres)}")

if figuras_guardadas:
    print("\n✅ Imágenes generadas correctamente:")
    for nombre in figuras_guardadas:
        print(f"   • images/{nombre}")
else:
    print("\n⚠️ No se guardaron imágenes. Posibles causas:")
    print("   • El notebook no generó figuras (verificar que se ejecutó correctamente)")
    print("   • Error al ejecutar las celdas del notebook")

# Verificar qué figuras faltan
faltantes = []
for num, (nombre, desc) in figura_nombres.items():
    ruta = os.path.join('images', nombre)
    if not os.path.exists(ruta):
        faltantes.append((nombre, desc))

if faltantes:
    print(f"\n⚠️ Figuras faltantes ({len(faltantes)}):")
    for nombre, desc in faltantes:
        print(f"   • {nombre} - {desc}")

print("\n" + "="*70)
print("PRÓXIMOS PASOS")
print("="*70)
print("""
1. Verificar las imágenes generadas:
   ls -lh images/

2. Agregar las imágenes a Git:
   git add images/

3. Hacer commit:
   git commit -m "Regenerar imágenes con correcciones"

4. Push:
   git push origin <tu-rama>
""")

print("="*70)
print("✅ SCRIPT COMPLETADO")
print("="*70)
