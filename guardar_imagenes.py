#!/usr/bin/env python3
"""
Script para guardar las imágenes del notebook Parqueadero_Rodrish_Analisis.ipynb
a la carpeta images/ para ser usadas en proyect_final.md

Uso:
1. Ejecutar todas las celdas del notebook en Google Colab
2. Ejecutar este script al final del notebook

El script guardará automáticamente todas las figuras generadas.
"""

import matplotlib.pyplot as plt
import os

# Crear la carpeta images si no existe
os.makedirs('images', exist_ok=True)

print("="*70)
print("GUARDANDO IMÁGENES DEL NOTEBOOK")
print("="*70)

# Mapeo de números de figura a nombres de archivo
# Las figuras se generan en el orden en que se ejecutan las celdas
figura_nombres = {
    1: 'terreno_actual.png',          # Celda 6: Gráfico 1
    2: 'espacio_camion.png',          # Celda 8: Gráfico 2
    3: 'comparacion.png',             # Celda 10: Gráfico 3
    4: 'optimizacion_ampliacion.png', # Celda 12: Gráfico 4
    5: 'opcion1.png',                 # Celda 14: OPCIÓN 1
    6: 'opcion2.png',                 # Celda 16: OPCIÓN 2 (Solución óptima)
    7: 'opcion3.png',                 # Celda 18: OPCIÓN 3 (Solución realista)
    8: 'opcion4.png',                 # Celda 19: OPCIÓN 3 con pasillos
    9: 'solucion_realista.png',       # Celda 20: OPCIÓN 2
}

# Obtener todas las figuras abiertas
figuras = plt.get_fignums()

if not figuras:
    print("⚠️ No se encontraron figuras. Asegúrate de ejecutar todas las celdas del notebook primero.")
else:
    print(f"\n📊 Figuras encontradas: {len(figuras)}")
    print()

    guardadas = 0
    for i, num_figura in enumerate(figuras, 1):
        if i in figura_nombres:
            nombre_archivo = figura_nombres[i]
            ruta_completa = os.path.join('images', nombre_archivo)

            fig = plt.figure(num_figura)
            fig.savefig(ruta_completa, dpi=300, bbox_inches='tight', facecolor='white')

            print(f"✅ Figura {i} guardada como: {ruta_completa}")
            guardadas += 1
        else:
            print(f"⚠️ Figura {i}: No hay nombre asignado (se omite)")

    print()
    print("="*70)
    print(f"RESUMEN: {guardadas} imágenes guardadas en la carpeta 'images/'")
    print("="*70)
    print()
    print("📝 PRÓXIMOS PASOS:")
    print("1. Verifica que las imágenes se guardaron correctamente")
    print("2. Descarga la carpeta 'images/' desde Colab:")
    print("   - Haz clic derecho en la carpeta 'images' en el panel izquierdo")
    print("   - Selecciona 'Download'")
    print("3. Sube la carpeta 'images/' a tu repositorio de GitHub")
    print("4. El archivo proyect_final.md ya tiene las referencias correctas")
    print()

# Nota: también puedes guardar la tabla comparativa
print("💡 TIP: Para la tabla comparativa (tabla_comparativa.png),")
print("   puedes crear una captura de pantalla de la tabla en el notebook")
print("   o crearla con una herramienta de diagramas.")
