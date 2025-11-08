# 🚛 Análisis y Optimización de Parqueadero - Rodrish S.A.

## 📋 Descripción

Análisis matemático y visualización optimizada para el diseño del parqueadero de maniobras de camiones de la empresa logística **Rodrish S.A.**

## 🎯 Características

- **Visualización exacta** de camiones y zonas de seguridad
- **Cálculos precisos** de espacios requeridos con distanciamiento de 2m
- **Distribución optimizada** usando rotaciones de 0°, 45° y 90°
- **Posicionamiento matemático** garantizando que todos los vehículos estén dentro de los límites
- **Zonas de seguridad** marcadas con conos en posiciones exactas

## 🔧 Mejoras Implementadas

### ✅ Sistema de Coordenadas Preciso
- Funciones `dibujar_camion_exacto()` y `dibujar_zona_seguridad()` con cálculos matemáticos exactos
- Posicionamiento basado en el centro de cada camión (x, y)
- Soporte para rotaciones de 0°, 45° y 90° con matrices de rotación

### ✅ Visualización Mejorada
- Camiones de 12m × 2.5m con dimensiones reales
- Zonas de seguridad de 16m × 6.5m (incluye distanciamiento de 2m)
- Conos de radio 0.4m posicionados en las esquinas exactas
- Todos los elementos dentro de los límites de los rectángulos

## 📊 Datos del Proyecto

- **Rectángulo A**: 20m × 10m = 200 m²
- **Rectángulo B**: 15m × 10m = 150 m²
- **Rectángulo C**: 20m × 10m = 200 m²
- **Ampliación**: 10m × 5m = 50 m²
- **Camiones requeridos**: 15
- **Distanciamiento de seguridad**: 2m
- **Radio de conos**: 0.4m

## 🚀 Uso

Ejecutar el notebook `Parqueadero_Rodrish_Analisis.ipynb` en Jupyter:

```bash
jupyter notebook Parqueadero_Rodrish_Analisis.ipynb
```

## 📈 Resultados

El análisis incluye:
1. Cálculo de áreas y perímetros
2. Visualización del terreno actual
3. Análisis de espacio por camión con medidas exactas
4. Comparación gráfica de escenarios
5. Layout optimizado con 15 camiones correctamente distribuidos
