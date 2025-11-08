# 📸 Instrucciones para Guardar y Cargar Imágenes del Notebook

Este documento explica cómo guardar las imágenes generadas en el notebook `Parqueadero_Rodrish_Analisis.ipynb` y cargarlas en Git para que aparezcan en `proyect_final.md`.

---

## 📋 Tabla de Contenido

1. [Resumen Rápido (5 pasos)](#resumen-rápido)
2. [Instrucciones Detalladas](#instrucciones-detalladas)
3. [Método Automático (Recomendado)](#método-automático-recomendado)
4. [Método Manual (Alternativa)](#método-manual-alternativa)
5. [Verificación](#verificación)
6. [Solución de Problemas](#solución-de-problemas)

---

## 🚀 Resumen Rápido

```bash
# 1. En Google Colab: Ejecutar todas las celdas del notebook
# 2. Agregar una celda al final con:
!wget https://raw.githubusercontent.com/TheQuietG/realmath/main/guardar_imagenes.py
%run guardar_imagenes.py

# 3. Descargar la carpeta 'images/' desde Colab
# 4. En tu repositorio local:
git add images/
git commit -m "Agregar imágenes del análisis de parqueadero"
git push origin main

# 5. ¡Listo! Las imágenes ya están en GitHub
```

---

## 📝 Instrucciones Detalladas

### Paso 1: Ejecutar el Notebook en Google Colab

1. Abre el notebook en Google Colab:
   - Ve a https://colab.research.google.com/
   - Abre desde GitHub: `TheQuietG/realmath`
   - Selecciona `Parqueadero_Rodrish_Analisis.ipynb`

2. Ejecuta TODAS las celdas en orden:
   - Menú: **Runtime → Run all**
   - O presiona: `Ctrl+F9` (Windows/Linux) o `Cmd+F9` (Mac)
   - Espera a que todas las celdas terminen de ejecutarse

3. Verifica que todas las gráficas se muestren correctamente

---

## ⚙️ Método Automático (Recomendado)

### Opción A: Usando el script guardar_imagenes.py

1. **Agregar una nueva celda** al final del notebook en Colab:
   ```python
   # Descargar el script
   !wget https://raw.githubusercontent.com/TheQuietG/realmath/main/guardar_imagenes.py

   # Ejecutar el script
   %run guardar_imagenes.py
   ```

2. **Ejecutar la celda**. Verás una salida como:
   ```
   ======================================================================
   GUARDANDO IMÁGENES DEL NOTEBOOK
   ======================================================================

   📊 Figuras encontradas: 9

   ✅ Figura 1 guardada como: images/terreno_actual.png
   ✅ Figura 2 guardada como: images/espacio_camion.png
   ✅ Figura 3 guardada como: images/comparacion.png
   ...
   ```

3. **Descargar la carpeta images/** desde Colab:
   - En el panel izquierdo, haz clic en el icono de carpeta 📁
   - Busca la carpeta `images/`
   - Haz clic derecho → **Download**

### Opción B: Guardar manualmente cada figura

En una nueva celda al final del notebook:

```python
import matplotlib.pyplot as plt
import os

# Crear carpeta
os.makedirs('images', exist_ok=True)

# Guardar cada figura manualmente
plt.figure(1).savefig('images/terreno_actual.png', dpi=300, bbox_inches='tight')
plt.figure(2).savefig('images/espacio_camion.png', dpi=300, bbox_inches='tight')
plt.figure(3).savefig('images/comparacion.png', dpi=300, bbox_inches='tight')
plt.figure(4).savefig('images/optimizacion_ampliacion.png', dpi=300, bbox_inches='tight')
plt.figure(5).savefig('images/opcion1.png', dpi=300, bbox_inches='tight')
plt.figure(6).savefig('images/opcion2.png', dpi=300, bbox_inches='tight')
plt.figure(7).savefig('images/opcion3.png', dpi=300, bbox_inches='tight')
plt.figure(8).savefig('images/opcion4.png', dpi=300, bbox_inches='tight')
plt.figure(9).savefig('images/solucion_realista.png', dpi=300, bbox_inches='tight')

print("✅ Todas las imágenes guardadas en la carpeta images/")
```

Luego descargar la carpeta `images/` como se indicó arriba.

---

## 📥 Método Manual (Alternativa)

Si prefieres guardar cada imagen individualmente:

1. **Clic derecho** en cada gráfica del notebook
2. Selecciona **"Save image as..."**
3. Guarda con el nombre correcto:
   - `terreno_actual.png`
   - `espacio_camion.png`
   - `comparacion.png`
   - `optimizacion_ampliacion.png`
   - `opcion1.png`
   - `opcion2.png`
   - `opcion3.png`
   - `opcion4.png`
   - `solucion_realista.png`
   - `tabla_comparativa.png` (captura de pantalla de la tabla)

4. Coloca todas las imágenes en una carpeta llamada `images/`

---

## 📤 Subir las Imágenes a Git

Una vez que tengas la carpeta `images/` descargada:

### En la Terminal/CMD:

```bash
# 1. Navegar a tu repositorio local
cd /ruta/a/tu/repositorio/realmath

# 2. Copiar la carpeta images/ descargada al repositorio
# (Asume que descargaste images/ en ~/Downloads/)
cp -r ~/Downloads/images/ .

# 3. Verificar que las imágenes estén ahí
ls images/

# 4. Agregar las imágenes a git
git add images/

# 5. Verificar qué se va a commitear
git status

# 6. Hacer commit
git commit -m "Agregar imágenes del análisis de parqueadero

Imágenes generadas desde el notebook Parqueadero_Rodrish_Analisis.ipynb:
- terreno_actual.png: Configuración actual del terreno
- espacio_camion.png: Análisis del espacio requerido por camión
- comparacion.png: Comparación de áreas y capacidad
- optimizacion_ampliacion.png: Análisis de optimización
- opcion1.png: Opción 1 - Distribución básica
- opcion2.png: Opción 2 - Distribución compacta
- opcion3.png: Opción 3 - Con pasillos
- opcion4.png: Opción 4 - Solución óptima
- solucion_realista.png: Solución realista final
- tabla_comparativa.png: Tabla comparativa de opciones
"

# 7. Push a GitHub
git push origin main
```

### En Windows (sin Terminal):

1. Copia la carpeta `images/` descargada
2. Pégala en la carpeta de tu repositorio `realmath/`
3. Abre **GitHub Desktop** o **Git GUI**
4. Verás los archivos nuevos en "Changes"
5. Escribe un mensaje de commit: `"Agregar imágenes del análisis de parqueadero"`
6. Haz clic en **Commit to main**
7. Haz clic en **Push origin**

---

## ✅ Verificación

### Verificar en Local:

```bash
# Debe mostrar todas las imágenes
ls -lh images/

# Debe mostrar ~10 archivos PNG
```

### Verificar en GitHub:

1. Ve a tu repositorio: https://github.com/TheQuietG/realmath
2. Navega a la carpeta `images/`
3. Deberías ver todas las imágenes listadas
4. Haz clic en una imagen para verificar que se muestra correctamente

### Verificar en proyect_final.md:

1. Abre `proyect_final.md` en GitHub
2. Las imágenes deberían mostrarse automáticamente en la vista previa
3. Si no se muestran, verifica las rutas:
   ```markdown
   ![Texto descriptivo](./images/nombre_imagen.png)
   ```

---

## 🎯 Lista de Verificación

Marca cada ítem cuando lo completes:

- [ ] Ejecuté todas las celdas del notebook en Colab
- [ ] Guardé las imágenes usando el script automático o manualmente
- [ ] Descargué la carpeta `images/` desde Colab
- [ ] Copié la carpeta `images/` a mi repositorio local
- [ ] Ejecuté `git add images/`
- [ ] Hice commit: `git commit -m "Agregar imágenes del análisis"`
- [ ] Hice push: `git push origin main`
- [ ] Verifiqué que las imágenes aparecen en GitHub
- [ ] Verifiqué que `proyect_final.md` muestra las imágenes

---

## 🔧 Solución de Problemas

### Problema: "No se encontraron figuras"

**Solución:**
- Asegúrate de ejecutar TODAS las celdas del notebook antes de guardar
- Las figuras solo existen mientras el kernel está activo
- Ejecuta `Runtime → Run all` y luego guarda las imágenes

### Problema: "Imágenes no se muestran en proyect_final.md"

**Solución:**
- Verifica que la carpeta `images/` esté en la raíz del repositorio
- Verifica que los nombres de archivo coincidan exactamente:
  ```bash
  # Deben ser exactamente:
  terreno_actual.png  # No Terreno_Actual.png o terreno_actual.PNG
  espacio_camion.png  # No espacio_camión.png (sin tilde)
  ```
- Verifica que las rutas en `proyect_final.md` sean: `./images/nombre.png`

### Problema: "git dice que las imágenes son muy grandes"

**Solución:**
- Las imágenes PNG del notebook son pequeñas (~100-500 KB cada una)
- Si son muy grandes (>5 MB), reduce la resolución:
  ```python
  plt.savefig('imagen.png', dpi=150)  # En vez de dpi=300
  ```

### Problema: "No puedo descargar la carpeta images/ desde Colab"

**Solución alternativa:**
1. Comprime la carpeta en Colab:
   ```python
   !zip -r images.zip images/
   ```
2. Descarga el archivo `images.zip` (clic derecho → Download)
3. Descomprime `images.zip` en tu computadora
4. Sube la carpeta descomprimida a Git

---

## 📚 Imágenes Requeridas

Estas son las 10 imágenes que necesita `proyect_final.md`:

| Nombre de Archivo | Descripción | Generada en Celda |
|-------------------|-------------|-------------------|
| `terreno_actual.png` | Configuración actual del terreno | 6 |
| `espacio_camion.png` | Espacio requerido por camión | 8 |
| `comparacion.png` | Comparación de áreas | 10 |
| `optimizacion_ampliacion.png` | Análisis de optimización | 12 |
| `opcion1.png` | Opción 1 - Básica | 14 |
| `opcion2.png` | Opción 2 - Compacta | 16 |
| `opcion3.png` | Opción 3 - Pasillos | 18 |
| `opcion4.png` | Opción 4 - Óptima | 19 |
| `solucion_realista.png` | Solución final | 20 |
| `tabla_comparativa.png` | Tabla de comparación | Manual |

---

## 💡 Consejos Adicionales

1. **Alta Calidad:** Usa `dpi=300` para imágenes de alta calidad
2. **Fondo Blanco:** Usa `facecolor='white'` para evitar fondos transparentes
3. **Sin Recortes:** Usa `bbox_inches='tight'` para evitar que se corten elementos
4. **Nombres Consistentes:** Usa nombres en minúsculas sin espacios ni tildes
5. **Formato PNG:** Es el mejor formato para gráficas (mejor que JPG)

---

## 🎓 Ejemplo Completo (Copiado-Pegado)

Puedes copiar y pegar este código en una nueva celda al final del notebook:

```python
# ========================================
# GUARDAR TODAS LAS IMÁGENES AUTOMÁTICAMENTE
# ========================================

import matplotlib.pyplot as plt
import os

# Crear carpeta
os.makedirs('images', exist_ok=True)

# Mapeo de figuras a nombres
figuras_map = {
    1: 'terreno_actual.png',
    2: 'espacio_camion.png',
    3: 'comparacion.png',
    4: 'optimizacion_ampliacion.png',
    5: 'opcion1.png',
    6: 'opcion2.png',
    7: 'opcion3.png',
    8: 'opcion4.png',
    9: 'solucion_realista.png'
}

# Guardar cada figura
for num, nombre in figuras_map.items():
    try:
        fig = plt.figure(num)
        ruta = f'images/{nombre}'
        fig.savefig(ruta, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✅ {nombre}")
    except:
        print(f"❌ Figura {num} no encontrada")

print("\n🎉 ¡Imágenes guardadas! Ahora descarga la carpeta 'images/'")
```

---

**¿Necesitas ayuda?** Contacta a tu tutor o revisa la documentación de Git.
