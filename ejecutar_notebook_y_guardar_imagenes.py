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

# Mapeo de figuras a nombres de archivo
# Ajustar según el orden real de generación de figuras en tu notebook
figura_nombres = {
    1: ('terreno_actual.png', 'Terreno actual'),
    2: ('espacio_camion.png', 'Espacio requerido por camión'),
    3: ('comparacion.png', 'Comparación de áreas'),
    4: ('optimizacion_ampliacion.png', 'Análisis de optimización'),
    5: ('opcion1.png', 'Opción 1 - Distribución básica'),
    6: ('opcion2.png', 'Opción 2 - Solución óptima'),
    7: ('opcion3.png', 'Opción 3 - Solución realista'),
    8: ('opcion4.png', 'Opción 4 - Con pasillos'),
    9: ('solucion_realista.png', 'Solución realista final'),
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
                    print(f"  ✓ Celda {i}: Guardada → {nombre_archivo} ({descripcion})")
                    figuras_generadas = len(figuras_actuales)
                else:
                    print(f"  • Celda {i}: Figura {nueva_figura} generada")
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

        # Solo guardar si no existe o si queremos sobreescribir
        if not os.path.exists(ruta) or True:  # Siempre sobreescribir
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
        faltantes.append(nombre)

if faltantes:
    print(f"\n⚠️ Figuras faltantes ({len(faltantes)}):")
    for nombre in faltantes:
        print(f"   • {nombre}")
    print("\nPuedes generarlas manualmente ejecutando el notebook en Colab")

print("\n" + "="*70)
print("PRÓXIMOS PASOS")
print("="*70)
print("""
1. Verificar las imágenes generadas:
   ls -lh images/

2. Agregar las imágenes a Git:
   git add images/

3. Hacer commit:
   git commit -m "Agregar imágenes del análisis de parqueadero"

4. Push a main:
   git push origin main

5. Verificar en GitHub que las imágenes se ven en proyect_final.md
""")

print("="*70)
print("✅ SCRIPT COMPLETADO")
print("="*70)
