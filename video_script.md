# SCRIPT DE VIDEO - REAL MATHS
## Optimización de Parqueadero con Ecuaciones Lineales
**Duración:** 5 minutos | **Autores:** Lizandro Alfonso Ruiz García & Pedro Pablo Forero Espejo

---

## 🎬 ESCENA 1: INTRODUCCIÓN (0:00 - 0:30)

**[VISUAL: Título animado "REAL MATHS" + Logo de la empresa Rodrish S.A.]**

**NARRADOR:**
"¿Alguna vez te has preguntado cómo las matemáticas pueden resolver problemas reales en una empresa? Hoy les presentamos un caso fascinante: la optimización del parqueadero de camiones de la empresa logística Rodrish S.A. usando ecuaciones lineales y geometría."

**[VISUAL: Transición a imagen del terreno en forma de C con los tres rectángulos A, B, C]**

**NARRADOR:**
"Soy [Nombre], y junto con mi compañero [Nombre], desarrollamos una solución matemática precisa para un problema de logística y seguridad."

---

## 🎬 ESCENA 2: EL PROBLEMA (0:30 - 1:15)

**[VISUAL: Mostrar imagen terreno_actual.png]**

**NARRADOR:**
"La empresa Rodrish S.A. enfrenta un desafío: su parqueadero tiene forma de C, compuesto por tres rectángulos con un área total de 550 metros cuadrados."

**[VISUAL: Destacar las dimensiones de cada rectángulo]**
- **Rectángulo A:** 20m × 10m = 200 m²
- **Rectángulo B:** 15m × 10m = 150 m²
- **Rectángulo C:** 20m × 10m = 200 m²

**NARRADOR:**
"La empresa opera 15 camiones diariamente, pero aquí viene lo interesante: no todos están en el parqueadero al mismo tiempo."

**[VISUAL: Animación mostrando el ciclo operativo]**

**NARRADOR:**
"Cada camión tiene un ciclo de 16 horas en ruta y 8 horas en el parqueadero. Esto significa que solo 5 camiones están estacionados simultáneamente, organizados en 3 batches."

**[VISUAL: Texto destacado]**
**"La pregunta clave: ¿Cuánta área de ampliación necesitamos para cumplir con las normas de seguridad HSE?"**

---

## 🎬 ESCENA 3: ANÁLISIS MATEMÁTICO (1:15 - 2:15)

**[VISUAL: Mostrar imagen espacio_camion.png]**

**NARRADOR:**
"Para resolver este problema, aplicamos cuatro conceptos matemáticos fundamentales."

**[VISUAL: Lista animada de conceptos]**
1. **Geometría básica** - Para calcular áreas
2. **Propiedades de números reales** - Para operaciones con medidas
3. **Ecuaciones lineales** - Para relacionar camiones con área necesaria
4. **Geometría de maniobras** - Para calcular radio de giro

**NARRADOR:**
"Primero, calculamos el espacio de seguridad que requiere cada camión según las normas HSE, que exigen 2 metros de distanciamiento."

**[VISUAL: Animación mostrando el cálculo]**

**Espacio longitudinal:**
- Camión: 12m
- Distanciamiento: 2m × 2 = 4m
- **Total: 16 metros**

**Espacio transversal:**
- Camión: 2.5m
- Distanciamiento: 2m × 2 = 4m
- **Total: 6.5 metros**

**[VISUAL: Destacar el resultado]**

**NARRADOR:**
"Esto nos da 104 metros cuadrados de estacionamiento por camión. Pero espera, ¡necesitamos más espacio para las maniobras!"

**[VISUAL: Mostrar imágenes maniobra_entrada.png y maniobra_salida.png]**

**NARRADOR:**
"Calculamos el radio de giro práctico de 8 metros, lo que nos da un factor de maniobras de 1.44. Esto significa que cada camión realmente necesita 150 metros cuadrados."

---

## 🎬 ESCENA 4: LA ECUACIÓN LINEAL (2:15 - 3:45)

**[VISUAL: Mostrar imagen ecuacion_lineal_ampliacion.png]**

**NARRADOR:**
"Ahora viene la parte más emocionante: desarrollamos una ecuación lineal que nos permite calcular exactamente cuánta área de ampliación necesitamos."

**[VISUAL: Animación de la ecuación apareciendo paso a paso]**

**Ecuación fundamental:**

$$A_{\text{ampliación}} = 149.76n - 550$$

**Donde:**
- n = número de camiones
- 149.76 = espacio real por camión (104 × 1.44)
- 550 = área actual del terreno

**NARRADOR:**
"Esta ecuación es poderosa porque podemos usarla para cualquier cantidad de camiones."

**[VISUAL: Mostrar tabla_ampliacion_lineal.png]**

**Ejemplos:**
- **3 camiones:** No requiere ampliación (cabe en 550 m²)
- **5 camiones:** 198.8 m² de ampliación
- **10 camiones:** 947.6 m² de ampliación
- **15 camiones:** 1,696.4 m² de ampliación

**NARRADOR:**
"Pero recordemos: solo necesitamos espacio para 5 camiones simultáneos debido al sistema de batches."

**[VISUAL: Destacar el cálculo para 5 camiones]**

$$A_{\text{ampliación}} = 149.76 \times 5 - 550 = 198.8 \text{ m}^2$$

**NARRADOR:**
"¡La respuesta es 198.8 metros cuadrados! Menos de 200 metros cuadrados de ampliación."

**[VISUAL: Mostrar opcion2.png - la solución óptima]**

---

## 🎬 ESCENA 5: CONFIGURACIONES Y COMPARACIÓN (3:45 - 4:30)

**[VISUAL: Mostrar configuraciones_ampliacion.png]**

**NARRADOR:**
"Evaluamos tres configuraciones posibles para esta ampliación, manteniendo el ancho uniforme de 10 metros para preservar la simetría del diseño."

**[VISUAL: Split screen mostrando las tres opciones evaluadas]**

**NARRADOR:**
"También analizamos tres opciones operativas:"

**[VISUAL: Mostrar tabla_comparativa.png]**

**Opción 1 - Sin ampliación:**
- 3 camiones
- Inversión: $0
- ❌ No cumple con los 5 camiones requeridos

**Opción 2 - Con ampliación de 198.8 m²:**
- 5 camiones simultáneos
- Inversión: ~$18,373
- ✅ **SOLUCIÓN ÓPTIMA** - Cumple 100% de necesidades

**Opción 3 - Con pasillo central:**
- 4 camiones
- Inversión: $0
- ⚠️ Solo cumple 80% de necesidades

**[VISUAL: Destacar la Opción 2 con checkmark verde]**

---

## 🎬 ESCENA 6: CONCLUSIONES (4:30 - 5:00)

**[VISUAL: Resumen visual con los resultados clave]**

**NARRADOR:**
"Entonces, ¿qué aprendimos?"

**[VISUAL: Lista animada de conclusiones]**

**1. Las matemáticas aplicadas resuelven problemas reales**
- Ecuaciones lineales precisas
- Cálculos de geometría y trigonometría
- Optimización basada en datos

**2. La solución óptima para Rodrish S.A.:**
- Ampliación: **198.8 m²** (~200 m²)
- Inversión: **~$18,373**
- Configuración: **~20m × 10m** junto al rectángulo B o A
- Cumple **100%** de necesidades operativas
- Cumple normas **HSE** con 2m de distanciamiento

**3. La ecuación puede escalar:**

$$A_{\text{ampliación}} = 149.76n - 550$$

**NARRADOR:**
"Esta ecuación permite a la empresa planificar futuras expansiones basándose en datos precisos, no en estimaciones."

**[VISUAL: Logo REAL MATHS + Créditos]**

**NARRADOR:**
"La matemática no es solo teoría, es una herramienta poderosa para tomar decisiones informadas en el mundo real. Gracias por acompañarnos en este proyecto de optimización."

**[VISUAL: Contacto y referencias]**

**FIN**

---

# 📊 DRAFT DE LA PRESENTACIÓN

## Diapositiva 1: PORTADA
**Contenido:**
- Título: **REAL MATHS**
- Subtítulo: Optimización de Parqueadero con Ecuaciones Lineales
- Autores: Lizandro Alfonso Ruiz García & Pedro Pablo Forero Espejo
- Tutor: Anggie Acero O.
- Año: 2025
- Logo/imagen de fondo: Camiones y ecuaciones

**Tiempo en pantalla:** 10 segundos

---

## Diapositiva 2: EL PROBLEMA
**Contenido:**
- Imagen: terreno_actual.png
- Texto destacado:
  - Empresa: **Rodrish S.A.**
  - Área actual: **550 m²**
  - Forma: **C (3 rectángulos)**
  - Flota: **15 camiones**
  - Simultáneos: **5 camiones (batches)**
- Pregunta central: "¿Cuánta área de ampliación necesitamos?"

**Tiempo en pantalla:** 30 segundos

---

## Diapositiva 3: DIMENSIONES DEL TERRENO
**Contenido:**
- Imagen: terreno_actual.png con dimensiones destacadas
- Tabla:
  | Rectángulo | Dimensiones | Área |
  |:---:|:---:|:---:|
  | A | 20m × 10m | 200 m² |
  | B | 15m × 10m | 150 m² |
  | C | 20m × 10m | 200 m² |
  | **TOTAL** | - | **550 m²** |

**Tiempo en pantalla:** 15 segundos

---

## Diapositiva 4: CICLO OPERATIVO
**Contenido:**
- Gráfico animado mostrando:
  - 15 camiones totales
  - 16h en ruta (icono de carretera)
  - 8h en parqueadero (icono de parking)
  - 3 batches de 5 camiones
- Texto destacado: **"Solo 5 camiones simultáneos"**

**Tiempo en pantalla:** 15 segundos

---

## Diapositiva 5: ESPACIO POR CAMIÓN
**Contenido:**
- Imagen: espacio_camion.png
- Cálculos visuales:
  - Largo: 12m + 4m = **16m**
  - Ancho: 2.5m + 4m = **6.5m**
  - Área de estacionamiento: **104 m²**
- Nota: Distanciamiento HSE de **2 metros**

**Tiempo en pantalla:** 20 segundos

---

## Diapositiva 6: RADIO DE GIRO Y MANIOBRAS
**Contenido:**
- Imágenes: maniobra_entrada.png + maniobra_salida.png (split screen)
- Datos clave:
  - Radio de giro práctico: **8m**
  - Factor de maniobras: **1.44**
  - Espacio REAL por camión: **150 m²**

**Tiempo en pantalla:** 20 segundos

---

## Diapositiva 7: LA ECUACIÓN LINEAL ⭐
**Contenido:**
- Ecuación destacada en grande:

$$\boxed{A_{\text{ampliación}} = 149.76n - 550}$$

- Explicación de variables:
  - n = número de camiones
  - 149.76 = espacio real por camión
  - 550 = área actual
- Imagen: ecuacion_lineal_ampliacion.png

**Tiempo en pantalla:** 30 segundos

---

## Diapositiva 8: APLICACIÓN DE LA ECUACIÓN
**Contenido:**
- Imagen: tabla_ampliacion_lineal.png
- Ejemplos calculados:
  | Camiones | Ampliación | Área Total |
  |:---:|:---:|:---:|
  | 3 | No requiere | 449 m² |
  | **5** | **198.8 m²** | **748.8 m²** ✅ |
  | 10 | 947.6 m² | 1,497.6 m² |
  | 15 | 1,696.4 m² | 2,246.4 m² |

**Tiempo en pantalla:** 30 segundos

---

## Diapositiva 9: CONFIGURACIONES DE AMPLIACIÓN
**Contenido:**
- Imagen: configuraciones_ampliacion.png
- Tres configuraciones mostradas
- Dimensión recomendada: **~20m × 10m**
- Ubicación: Junto a rectángulo B o A

**Tiempo en pantalla:** 20 segundos

---

## Diapositiva 10: COMPARACIÓN DE OPCIONES
**Contenido:**
- Imagen: tabla_comparativa.png
- Tres opciones comparadas:

  | | Opción 1 | Opción 2 | Opción 3 |
  |:---|:---:|:---:|:---:|
  | Camiones | 3 | **5** ✅ | 4 |
  | Inversión | $0 | **$18,373** | $0 |
  | Cumplimiento | ❌ 60% | ✅ **100%** | ⚠️ 80% |

**Tiempo en pantalla:** 30 segundos

---

## Diapositiva 11: SOLUCIÓN ÓPTIMA
**Contenido:**
- Imagen: opcion2.png
- Destacar con marco verde
- Texto principal:
  - **Ampliación:** 198.8 m² (~200 m²)
  - **Inversión:** ~$18,373
  - **Capacidad:** 5 camiones simultáneos
  - **Cumplimiento HSE:** ✅ 100%
  - **Cumplimiento operativo:** ✅ 100%

**Tiempo en pantalla:** 20 segundos

---

## Diapositiva 12: CONCLUSIONES MATEMÁTICAS
**Contenido:**
- Lista con iconos:
  ✓ Ecuación lineal precisa desarrollada
  ✓ Geometría básica aplicada correctamente
  ✓ Radio de giro calculado: 8m
  ✓ Factor de maniobras: 1.44
  ✓ Optimización mediante análisis de batches
  ✓ Decisiones basadas en datos reales

**Tiempo en pantalla:** 20 segundos

---

## Diapositiva 13: RECOMENDACIÓN FINAL
**Contenido:**
- Título grande: **RECOMENDACIÓN PARA RODRISH S.A.**
- Cuadro destacado:

  **IMPLEMENTAR AMPLIACIÓN DE 198.8 m²**

  ✅ Cumple 100% de necesidades operativas
  ✅ Cumple normas HSE (2m de distanciamiento)
  ✅ Permite maniobras seguras (radio 8m)
  ✅ Inversión proporcional (~$18,373)
  ✅ Escalable mediante ecuación lineal

**Tiempo en pantalla:** 20 segundos

---

## Diapositiva 14: CIERRE Y CRÉDITOS
**Contenido:**
- Logo REAL MATHS
- Texto:
  **"La matemática aplicada resuelve problemas reales"**
- Créditos:
  - Autores: Lizandro Alfonso Ruiz García & Pedro Pablo Forero Espejo
  - Tutor: Anggie Acero O.
  - Año: 2025
- Contacto/Referencias

**Tiempo en pantalla:** 10 segundos

---

# 📝 NOTAS PARA LA PRESENTACIÓN

## Timing Total:
- 14 diapositivas
- ~300 segundos (5 minutos)
- Promedio: ~21 segundos por diapositiva

## Recomendaciones de Presentación:

### 🎯 Énfasis Visual:
1. **Diapositiva 7** (Ecuación Lineal): Esta es la diapositiva central - usar animación especial
2. **Diapositiva 11** (Solución Óptima): Destacar con marco verde y checkmarks
3. **Diapositiva 13** (Recomendación): Usar colores llamativos para el cuadro

### 🎨 Colores Sugeridos:
- **Verde:** Para soluciones óptimas, aprobaciones, cumplimientos
- **Amarillo:** Para advertencias, cumplimientos parciales
- **Rojo:** Para deficiencias, incumplimientos
- **Azul:** Para datos técnicos, ecuaciones, cálculos
- **Gris:** Para información secundaria

### 🎬 Transiciones:
- Usar transiciones suaves entre diapositivas
- Animaciones de aparición para ecuaciones (tipo "escribir")
- Destacados con pulso o brillo para resultados clave

### 🗣️ Tono de Narración:
- **Profesional pero accesible**
- **Entusiasta** al presentar la ecuación lineal
- **Confiado** al dar la recomendación final
- **Pausas estratégicas** después de resultados importantes

### 📊 Datos a Memorizar:
- Área actual: **550 m²**
- Camiones simultáneos: **5**
- Ampliación necesaria: **198.8 m²**
- Ecuación: **A = 149.76n - 550**
- Inversión: **~$18,373**

---

# 🎥 TIPS PARA LA GRABACIÓN

1. **Equipo necesario:**
   - Micrófono de calidad (evitar eco)
   - Buena iluminación
   - Fondo limpio o pantalla verde
   - Software de edición (DaVinci Resolve, Adobe Premiere, etc.)

2. **Durante la grabación:**
   - Hablar con claridad y ritmo moderado
   - Hacer pausas después de conceptos clave
   - Usar gestos para enfatizar puntos importantes
   - Sonreír (transmite confianza)

3. **En la edición:**
   - Sincronizar narración con diapositivas
   - Agregar música de fondo sutil
   - Insertar efectos de sonido para transiciones
   - Agregar subtítulos si es posible

4. **Ensayar:**
   - Practicar varias veces antes de grabar
   - Cronometrar para asegurar que dure 5 minutos
   - Ajustar ritmo según sea necesario

---

**¡Éxito con su presentación! 🚀**
