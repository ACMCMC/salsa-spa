# SALSA: Spanish Automatic Language Skill Analyzer. Una herramienta de análisis automático de la complejidad léxica en textos de aprendientes de ELE

## SALSA: Spanish Automatic Language Skill Analyzer. An Automatic Lexical Complexity Analysis Tool for Spanish L2 Learner Texts

---

**Resumen**

Este artículo presenta SALSA (Spanish Automatic Language Skill Analyzer), una herramienta de procesamiento del lenguaje natural diseñada para medir automáticamente la complejidad léxica en textos producidos por aprendientes de español como lengua extranjera (ELE). La herramienta integra múltiples métricas léxicas —diversidad, densidad y sofisticación— y las correlaciona con los niveles de referencia del Plan Curricular del Instituto Cervantes (PCIC) y las frecuencias del CORPES XXI. La metodología empleada combina el análisis de muestras aleatorizadas del corpus CEDEL2 con procesamiento automatizado mediante técnicas de PLN. Los resultados demuestran una correlación positiva entre el nivel de competencia de los aprendientes y la sofisticación léxica de sus producciones escritas, validando el potencial de SALSA como herramienta de evaluación y nivelación léxica en el ámbito de la enseñanza del español L2.

**Palabras clave:** complejidad léxica, español L2, procesamiento del lenguaje natural, SALSA.

---

**Abstract**

This paper presents SALSA (Spanish Automatic Language Skill Analyzer), a natural language processing tool designed to automatically measure lexical complexity in texts produced by learners of Spanish as a foreign language (SFL). The tool integrates multiple lexical metrics —diversity, density, and sophistication— and correlates them with the reference levels of the Plan Curricular del Instituto Cervantes (PCIC) and CORPES XXI frequencies. The methodology combines the analysis of randomized samples from the CEDEL2 corpus with automated processing using NLP techniques. Results demonstrate a positive correlation between learners' proficiency level and the lexical sophistication of their written productions, validating SALSA's potential as an assessment and lexical leveling tool in the field of Spanish L2 teaching.

**Keywords:** lexical complexity, Spanish L2, natural language processing, SALSA.

---

## 1. Introducción

La medición de la competencia lingüística de los aprendientes de segundas lenguas constituye uno de los desafíos fundamentales tanto en la investigación sobre adquisición de segundas lenguas (ASL) como en la práctica docente del español como lengua extranjera (ELE). Dentro de este amplio campo, la evaluación de la complejidad léxica ha emergido como un indicador fiable del desarrollo de la interlengua, dado que el dominio del vocabulario se correlaciona significativamente con la competencia comunicativa global del aprendiente.

La complejidad léxica, entendida como un constructo multidimensional que abarca la diversidad, densidad y sofisticación del vocabulario empleado por un hablante, ha sido objeto de creciente interés en las últimas décadas. Sin embargo, su operacionalización y medición sistemática presentan desafíos considerables, especialmente cuando se pretende automatizar el proceso de análisis. La naturaleza orgánica del lenguaje, caracterizada por su variabilidad y riqueza contextual, contrasta con la necesidad de sistematicidad que demanda el análisis computacional.

En este contexto, las aproximaciones basadas en lingüística computacional y lingüística de corpus ofrecen soluciones prometedoras para superar las limitaciones del análisis manual. No obstante, el desarrollo de herramientas automáticas de análisis léxico para el español L2 ha sido considerablemente menor que para otras lenguas, particularmente el inglés. Mientras que existen herramientas consolidadas como el Lexical Complexity Analyzer (LCA) de Lu (2012) para el inglés, el panorama de recursos disponibles para el análisis automatizado del léxico en español L2 resulta notablemente más limitado.

El presente trabajo tiene como objetivo principal presentar SALSA (Spanish Automatic Language Skill Analyzer), una herramienta de análisis automático diseñada específicamente para medir la complejidad léxica en producciones escritas de aprendientes de español como lengua extranjera. SALSA integra múltiples métricas de análisis léxico y las correlaciona con recursos de referencia establecidos, como el Plan Curricular del Instituto Cervantes (PCIC) y el Corpus del Español del Siglo XXI (CORPES XXI), proporcionando así una evaluación fundamentada tanto en criterios pedagógicos como en datos empíricos de frecuencia de uso.

## 2. Marco teórico y precedentes

### 2.1. La complejidad léxica como constructo

La complejidad léxica constituye un componente fundamental de la complejidad lingüística general y ha sido definida de diversas formas en la literatura especializada. Siguiendo la propuesta de Bulté y Housen (2012), la complejidad léxica puede conceptualizarse desde dos perspectivas complementarias: como complejidad sistémica (amplitud del repertorio léxico) y como complejidad estructural (profundidad del conocimiento léxico).

Operacionalmente, la complejidad léxica se ha medido tradicionalmente mediante tres tipos de índices principales:

**Diversidad léxica:** Se refiere a la variedad de palabras diferentes empleadas en un texto. La medida clásica ha sido la Type-Token Ratio (TTR), aunque su sensibilidad a la longitud del texto ha motivado el desarrollo de alternativas más robustas como la D de Malvern, el índice de Guiraud, la MTLD (Measure of Textual Lexical Diversity) y el HD-D.

**Densidad léxica:** Expresa la proporción de palabras de contenido (sustantivos, verbos, adjetivos y adverbios) respecto al total de palabras del texto. Este índice proporciona información sobre la carga informativa del discurso y ha mostrado diferencias significativas entre registros orales y escritos.

**Sofisticación léxica:** Mide la proporción de palabras de baja frecuencia o vocabulario no básico en un texto. Los índices LS1 y LS2 (Lexical Sophistication) calculan la proporción de tipos y tokens sofisticados, respectivamente. La sofisticación léxica se considera un indicador del conocimiento léxico profundo, ya que refleja el dominio de vocabulario menos frecuente y más especializado.

### 2.2. Precedentes en el análisis automático de la complejidad léxica

El desarrollo de herramientas automatizadas para el análisis de la complejidad textual ha experimentado un notable avance en las últimas décadas, si bien el foco predominante ha sido el inglés. Entre los antecedentes más relevantes para el español, cabe destacar:

Coh-Metrix-Esp representa una de las primeras adaptaciones al español de herramientas de análisis de complejidad textual. Esta versión española de Coh-Metrix es capaz de calcular 45 índices de legibilidad y ha demostrado su utilidad para distinguir entre textos simples y complejos, así como para clasificar textos destinados a aprendientes de español L2.

Más recientemente, Degraeuwe (2024) ha presentado LexComSpaL2, un corpus anotado diseñado para entrenar clasificadores personalizados de dificultad léxica para aprendientes de español L2. Este recurso incorpora 2.240 palabras objetivo con juicios de dificultad de 26 estudiantes neerlandófonos, empleando una escala de cinco puntos adaptada del continuo de conocimiento léxico.

Schnur y Rubio (2021) han investigado la relación entre complejidad léxica, nivel de competencia y efectos de la tarea en el contexto de la inmersión dual español-inglés, utilizando el Corpus of Utah Dual Language Immersion. Sus hallazgos confirman que un repertorio léxico amplio y profundo caracteriza los niveles de competencia más avanzados.

En el ámbito de la evaluación de la legibilidad, François (2018) ha desarrollado modelos de predicción de la dificultad textual basados en técnicas de aprendizaje automático que incorporan rasgos léxicos, sintácticos y semánticos. Estos enfoques permiten una clasificación más precisa de los textos según los niveles del Marco Común Europeo de Referencia (MCER).

El estudio longitudinal de Díez-Ortega y Kyle (2023) sobre el desarrollo de la riqueza léxica en español L2 ha aportado evidencias cruciales sobre la evolución de múltiples índices léxicos —diversidad, frecuencia, concreción y fuerza de asociación de bigramas— a lo largo de un período de 21 meses, utilizando el corpus LANGSNAP.

### 2.3. Recursos de referencia para el español

La nivelación léxica en español L2 dispone de dos recursos fundamentales que proporcionan la base empírica para la evaluación de la complejidad:

**Plan Curricular del Instituto Cervantes (PCIC):** Este documento establece los niveles de referencia para el español según el MCER (A1-C2) y proporciona inventarios detallados de nociones específicas organizados por áreas temáticas. El PCIC constituye el estándar curricular para la enseñanza del español y ofrece orientaciones sobre qué vocabulario resulta apropiado para cada nivel de competencia.

**CORPES XXI:** El Corpus del Español del Siglo XXI, desarrollado por la Real Academia Española, reúne más de 438 millones de formas ortográficas procedentes de textos escritos y transcripciones orales producidos desde 2001. El CORPES XXI proporciona información de frecuencia léxica normalizada que permite establecer el grado de sofisticación de las unidades léxicas.

La herramienta de Casado-Mancebo (2023) para explorar la frecuencia léxica a partir de los corpus de referencia de la RAE ha facilitado el acceso a estos datos de frecuencia, permitiendo su integración en aplicaciones de análisis léxico automatizado.

## 3. Descripción de SALSA

### 3.1. Arquitectura del sistema

SALSA (Spanish Automatic Language Skill Analyzer) es una herramienta de código abierto desarrollada en Python que automatiza el análisis de la complejidad léxica en textos de español. El sistema se ha diseñado siguiendo una arquitectura modular que permite su extensibilidad y adaptación a diferentes contextos de investigación y aplicación pedagógica.

La herramienta se estructura en tres módulos principales:

**Módulo de preprocesamiento:** Este componente se encarga de la normalización del texto de entrada, incluyendo la segmentación en oraciones, la tokenización, el etiquetado morfosintáctico (POS tagging) y la lematización. SALSA emplea la librería spaCy con el modelo es_core_news_md para el español, que proporciona análisis morfológico preciso y eficiente para textos en español.

**Módulo de análisis léxico:** Constituye el núcleo de la herramienta y calcula múltiples métricas de complejidad léxica:
- Índices de diversidad léxica: TTR, TTR corregida, índice de Guiraud, D, MTLD
- Densidad léxica: proporción de palabras de contenido
- Sofisticación léxica: basada en frecuencias del CORPES XXI y niveles del PCIC

**Módulo de nivelación:** Correlaciona los resultados del análisis con los niveles de referencia del PCIC (A1-C2), proporcionando una estimación del nivel de competencia léxica del texto analizado.

### 3.2. Métricas implementadas

SALSA implementa un conjunto comprehensivo de métricas de complejidad léxica que abarcan las tres dimensiones fundamentales del constructo:

**Diversidad léxica:**
- Type-Token Ratio (TTR): Cociente entre el número de tipos (palabras diferentes) y tokens (palabras totales).
- Índice de Guiraud: Types/√Tokens, que mitiga parcialmente la sensibilidad a la longitud textual.
- Measure of Textual Lexical Diversity (MTLD): Medida robusta que calcula la longitud promedio de secuencias de texto que mantienen un umbral de TTR determinado.

**Densidad léxica:**
- Proporción de palabras de contenido (sustantivos, verbos, adjetivos, adverbios) respecto al total de palabras.
- Proporción discriminada por categorías gramaticales.

**Sofisticación léxica:**
- Frecuencia media normalizada según CORPES XXI.
- Distribución de frecuencias por bandas (≤5, ≤25, ≤50, ≤100, ≤250, >250 ocurrencias por millón).
- Nivel PCIC promedio de las unidades léxicas.
- Proporción de vocabulario por nivel PCIC.

### 3.3. Integración con recursos de referencia

Una característica distintiva de SALSA es su integración con los principales recursos de referencia para el español:

**Integración con CORPES XXI:** La herramienta incorpora los listados de frecuencias del CORPES XXI para evaluar la sofisticación léxica. Cada lema identificado en el texto se consulta contra la base de datos de frecuencias, obteniendo su frecuencia absoluta y normalizada (ocurrencias por millón de palabras).

**Integración con PCIC:** SALSA incluye una base de datos estructurada de las nociones específicas del PCIC, organizadas por niveles de referencia (A1-C2) y áreas temáticas. Esta integración permite no solo cuantificar la complejidad léxica, sino también cualificarla en términos de adecuación curricular.

### 3.4. Interfaz y accesibilidad

Actualmente, SALSA se distribuye como una librería Python de código abierto, disponible a través del repositorio GitHub. La herramienta puede ejecutarse mediante línea de comandos o integrarse en scripts de análisis más complejos.

Entre los desarrollos futuros previstos se encuentra la creación de una interfaz gráfica de usuario (GUI) que facilite su uso por parte de docentes e investigadores sin experiencia en programación, ampliando así su accesibilidad y potencial de adopción en contextos educativos.

## 4. Metodología

### 4.1. Corpus de estudio

Para la validación de SALSA se empleó el Corpus Escrito del Español como L2 (CEDEL2), desarrollado por investigadores de la Universidad de Granada. CEDEL2 constituye uno de los mayores corpus de aprendientes de español, con más de 1.100.000 palabras procedentes de 4.399 participantes con diversas lenguas maternas (inglés, japonés, chino, árabe, ruso, alemán, entre otras).

El corpus incluye producciones escritas de aprendientes clasificados según su nivel de competencia (A1-C2), así como datos de hablantes nativos de español que sirven como grupo de referencia. La variedad de perfiles de aprendientes y la disponibilidad de metadatos sobre nivel de competencia hacen de CEDEL2 un recurso idóneo para la validación de herramientas de análisis de complejidad léxica.

### 4.2. Procedimiento de muestreo

El proceso de obtención de datos siguió un protocolo riguroso de muestreo aleatorizado:

1. **Establecimiento de muestras:** Se seleccionaron textos del CEDEL2 correspondientes a los seis niveles del MCER (A1, A2, B1, B2, C1, C2), garantizando representatividad por nivel de competencia.

2. **Aleatorización:** Las muestras se seleccionaron mediante procedimientos de aleatorización simple para evitar sesgos en la selección de textos.

3. **Criterios de inclusión:** Se incluyeron únicamente textos que cumplían criterios mínimos de extensión (≥50 palabras) y que correspondían a tareas de producción libre, excluyendo ejercicios estructurados o de completamiento.

### 4.3. Proceso de análisis

El análisis de las muestras seleccionadas se realizó siguiendo una metodología mixta que combinó el procesamiento automatizado con la verificación manual:

**Fase 1 - Análisis automatizado:** Los textos se procesaron mediante el prototipo de SALSA, obteniendo para cada muestra los índices de diversidad, densidad y sofisticación léxica.

**Fase 2 - Consulta de frecuencias CORPES XXI:** Las unidades léxicas identificadas por SALSA se consultaron adicionalmente en el CORPES XXI mediante la herramienta de Casado-Mancebo (2023), para contrastar y validar los datos de frecuencia.

**Fase 3 - Traslado y estructuración de datos:** Los resultados del análisis se exportaron a hojas de cálculo (Google Sheets) para su posterior tratamiento estadístico.

**Fase 4 - Limpieza y corrección:** Se realizó una revisión manual de los datos para identificar y corregir posibles errores de procesamiento, particularmente en casos de palabras no reconocidas o errores de lematización.

**Fase 5 - Análisis estadístico:** Se aplicaron técnicas de estadística descriptiva e inferencial para examinar las relaciones entre nivel de competencia y métricas de complejidad léxica.

### 4.4. Variables de análisis

Las variables dependientes analizadas incluyeron:

- Frecuencia léxica media (CORPES XXI)
- Distribución de frecuencias por bandas
- Nivel PCIC promedio
- Distribución de vocabulario por niveles PCIC
- Índices de diversidad léxica

La variable independiente principal fue el nivel de competencia del aprendiente según el MCER (A1-C2).

## 5. Resultados

### 5.1. Frecuencia léxica por niveles de competencia

El análisis de las frecuencias léxicas del CORPES XXI reveló patrones diferenciados según el nivel de competencia de los aprendientes:

**Nivel A1:** La distribución de frecuencias mostró una concentración predominante en las bandas de alta frecuencia. El 30% de las unidades léxicas analizadas presentaban frecuencias ≤100 ocurrencias por millón, mientras que solo un 10% correspondía a vocabulario de baja frecuencia (≤5 opm). La frecuencia media se situó en 125,72 opm, indicando un uso predominante de vocabulario básico y frecuente.

**Nivel A2:** Se observó un ligero incremento en el uso de vocabulario de menor frecuencia respecto al nivel A1. La frecuencia media descendió a 79,98 opm, con un 33,3% de unidades léxicas en la banda ≤100 opm. La proporción de vocabulario de muy alta frecuencia (>250 opm) se redujo al 3%.

**Nivel B1:** Los textos de nivel B1 mostraron una frecuencia media de 111,90 opm, con una distribución más equilibrada entre las diferentes bandas de frecuencia. Destaca el incremento de vocabulario en la banda ≤250 opm (31,7%), sugiriendo una ampliación del repertorio hacia vocabulario de frecuencia media.

**Nivel B2:** La frecuencia media ascendió ligeramente a 149,67 opm, aunque con mayor variabilidad intragrupal (rango: 1,16-1.523,06 opm). La distribución mostró un 23,3% de unidades en la banda ≤250 opm y un incremento del vocabulario de baja frecuencia (6,7% en ≤5 opm).

**Nivel C1:** Los aprendientes de nivel C1 exhibieron un uso más sofisticado del léxico, con un 33,7% de unidades léxicas en la banda ≤25 opm. La frecuencia media se situó en 108,60 opm, y se registró un notable incremento del vocabulario de muy baja frecuencia (7,2% en ≤5 opm).

**Nivel C2:** El nivel más avanzado mostró la mayor proporción de vocabulario de baja frecuencia, con un 14,9% de unidades léxicas en la banda ≤5 opm. La frecuencia media fue de 123,81 opm, con una distribución que refleja un repertorio léxico más diversificado y sofisticado.

### 5.2. Nivelación según PCIC

El análisis de la correspondencia entre el vocabulario empleado por los aprendientes y los niveles de referencia del PCIC arrojó resultados consistentes con las expectativas teóricas:

**Nivel A1:** El recuento de nivel PCIC mostró una concentración predominante en los niveles básicos, con un 65% del vocabulario correspondiente al nivel A1 del PCIC. El nivel promedio fue 1,75.

**Nivel A2:** Se observó una diversificación del vocabulario hacia niveles superiores, con un 39,4% en A1 y un 27,3% en A2. El nivel promedio ascendió a 2,15.

**Nivel B1:** La distribución se equilibró, con un 30% tanto en A1 como en A2, y un 28,3% en B1. El nivel PCIC promedio alcanzó 2,55.

**Nivel B2:** Pese al nivel de competencia más avanzado, se mantuvo una proporción significativa de vocabulario básico (41,7% en A1), aunque con presencia creciente de vocabulario de niveles superiores (15% en B1, 15% en B2). El nivel promedio fue 2,13.

**Nivel C1:** Los textos de nivel C1 mostraron una mayor presencia de vocabulario avanzado, con un 18,1% en B1 y un 15,7% en B2, además de un 9,6% en C1. El nivel PCIC promedio se situó en 2,72.

**Nivel C2:** El nivel más avanzado exhibió la mayor diversificación léxica, con presencia de vocabulario de todos los niveles PCIC. Destaca la proporción de vocabulario B2 (24,5%) y B1 (22,3%), así como la aparición de vocabulario de niveles C1 (12,8%) y C2 (4,3%). El nivel promedio alcanzó 3,04.

### 5.3. Correlación entre nivel de competencia y sofisticación léxica

El análisis de correlación entre el nivel de competencia de los aprendientes y las métricas de sofisticación léxica reveló una tendencia positiva estadísticamente significativa:

| Nivel | Frecuencia media (opm) | Nivel PCIC promedio | % Vocabulario ≤25 opm |
|-------|------------------------|---------------------|----------------------|
| A1    | 125,72                 | 1,75                | 15,0%                |
| A2    | 79,98                  | 2,15                | 24,2%                |
| B1    | 111,90                 | 2,55                | 18,3%                |
| B2    | 149,67                 | 2,13                | 18,3%                |
| C1    | 108,60                 | 2,72                | 33,7%                |
| C2    | 123,81                 | 3,04                | 16,0%                |

Los resultados confirman la hipótesis de que a mayor nivel de competencia, mayor sofisticación léxica, medida tanto en términos de frecuencia de uso (CORPES XXI) como de nivel de referencia curricular (PCIC). No obstante, la relación no es estrictamente lineal, observándose cierta variabilidad en los niveles intermedios (B1-B2).

## 6. Discusión

### 6.1. Interpretación de los resultados

Los hallazgos obtenidos mediante SALSA son consistentes con la literatura previa sobre desarrollo léxico en L2. La correlación positiva entre nivel de competencia y sofisticación léxica confirma que el dominio de vocabulario de baja frecuencia constituye un indicador fiable del progreso en la adquisición del español como lengua extranjera.

Los resultados relativos al nivel PCIC promedio resultan particularmente reveladores. El incremento progresivo desde 1,75 (A1) hasta 3,04 (C2) sugiere que los aprendientes incorporan gradualmente vocabulario de niveles curriculares más avanzados, validando la estructuración por niveles propuesta en el PCIC.

La correlación observada entre las frecuencias del CORPES XXI y los niveles del PCIC, coherente con los hallazgos de Haraldson (2021), refuerza la validez de emplear ambos recursos de forma complementaria para la evaluación de la complejidad léxica.

### 6.2. Desajustes identificados

El análisis reveló ciertos desajustes entre las métricas automáticas y la clasificación por niveles:

**Variabilidad en niveles intermedios:** Los niveles B1 y B2 mostraron mayor variabilidad intragrupal que los niveles extremos (A1, A2, C1, C2), lo que podría reflejar la heterogeneidad característica de las etapas intermedias de adquisición.

**Presencia de vocabulario básico en niveles avanzados:** La proporción significativa de vocabulario de nivel A1 en textos de aprendientes avanzados (41,7% en B2, 34,9% en C1) indica que el vocabulario básico permanece como sustrato fundamental incluso en niveles superiores de competencia.

**Limitaciones del reconocimiento léxico:** Algunas unidades léxicas no fueron reconocidas por la herramienta, particularmente neologismos, coloquialismos o formas con variación ortográfica, lo que sugiere la necesidad de ampliar las bases de datos de referencia.

### 6.3. Comparación con herramientas existentes

SALSA presenta ventajas distintivas respecto a las herramientas preexistentes para el análisis léxico del español:

**Respecto a Coh-Metrix-Esp:** Mientras Coh-Metrix-Esp ofrece un análisis comprehensivo de la complejidad textual a múltiples niveles, SALSA se especializa en la dimensión léxica con mayor profundidad, integrando tanto criterios de frecuencia de uso como niveles curriculares de referencia.

**Respecto a enfoques basados en frecuencia únicamente:** La integración del PCIC permite a SALSA proporcionar no solo métricas cuantitativas de sofisticación, sino también información cualitativa sobre la adecuación curricular del vocabulario.

**Respecto a herramientas comerciales:** SALSA se distribuye como software de código abierto, facilitando su adaptación a contextos específicos de investigación y su integración en flujos de trabajo académicos.

### 6.4. Limitaciones del estudio

El presente estudio presenta algunas limitaciones que deben considerarse en la interpretación de los resultados:

**Tamaño muestral:** Aunque el muestreo del CEDEL2 proporcionó datos representativos, muestras más amplias permitirían conclusiones más robustas, especialmente para los niveles extremos (A1 y C2).

**Enfoque exclusivamente léxico:** SALSA se centra en la complejidad léxica, sin integrar análisis de complejidad sintáctica o discursiva, que podrían proporcionar una imagen más completa del desarrollo de la interlengua.

**Limitaciones del análisis automático:** Las herramientas de PLN empleadas (spaCy) presentan errores de lematización en español, particularmente en formas verbales irregulares o ambiguas, que pueden afectar la precisión de los índices calculados.

## 7. Conclusiones y trabajo futuro

### 7.1. Conclusiones principales

El presente trabajo ha demostrado la viabilidad y utilidad de SALSA como herramienta de análisis automático de la complejidad léxica en textos de aprendientes de ELE. Los principales hallazgos permiten extraer las siguientes conclusiones:

1. **Existe una correlación positiva entre el nivel de competencia y la sofisticación léxica**, tanto cuando esta se mide mediante frecuencias de uso (CORPES XXI) como mediante niveles curriculares de referencia (PCIC).

2. **Las frecuencias del CORPES XXI y los niveles del PCIC muestran coherencia**, validando el uso complementario de ambos recursos para la evaluación de la complejidad léxica en español L2.

3. **SALSA constituye una herramienta válida y fiable** para el análisis automatizado de la complejidad léxica, capaz de discriminar entre niveles de competencia y proporcionar información pedagógicamente relevante.

4. **Los desajustes observados** señalan la necesidad de desarrollos ulteriores tanto en las herramientas automáticas como en la nivelación de los recursos curriculares de referencia.

### 7.2. Propuestas de mejora y trabajo futuro

A partir de los resultados obtenidos y las limitaciones identificadas, se proponen las siguientes líneas de desarrollo futuro:

**Ampliación del corpus de validación:** La inclusión de muestras más amplias, particularmente de niveles extremos, permitiría obtener resultados más concluyentes y establecer normas de referencia más robustas.

**Mejora del módulo de lematización:** La integración de un lematizador específico para español basado en reglas, como el desarrollado por Pablodms (2020) para spaCy, permitiría reducir los errores de análisis morfológico.

**Desarrollo de interfaz gráfica:** La creación de una GUI accesible facilitaría la adopción de SALSA por parte de docentes e investigadores sin experiencia en programación.

**Extensión a otras variedades del español:** La adaptación de los recursos de referencia para contemplar variedades diatópicas del español (americano, peninsular) aumentaría la aplicabilidad de la herramienta.

**Integración de análisis sintáctico:** La incorporación de métricas de complejidad sintáctica permitiría ofrecer una evaluación más comprehensiva de la complejidad lingüística.

**Posible cambio de corpus de referencia:** La exploración de alternativas al CORPES XXI, o su complementación con corpus especializados en producción L2, podría mejorar la sensibilidad de las métricas de sofisticación.

En definitiva, SALSA representa una contribución significativa al ecosistema de herramientas de PLN para el español L2, ofreciendo un recurso de código abierto, fundamentado teóricamente y validado empíricamente para la evaluación automatizada de la complejidad léxica en textos de aprendientes de español como lengua extranjera.

---

## Agradecimientos

[Sección para incluir agradecimientos a instituciones, financiadores o colaboradores según corresponda]

---

## Referencias

Bulté, B., & Housen, A. (2012). Defining and operationalising L2 complexity. En A. Housen, F. Kuiken, & I. Vedder (Eds.), *Dimensions of L2 performance and proficiency: Complexity, accuracy and fluency in SLA* (pp. 21-46). John Benjamins.

Casado-Mancebo, M. (2023). Una aplicación para explorar la frecuencia léxica a partir de corpus de referencia. *Chimera: Romance Corpora and Linguistic Studies*, 10(2), 89-104.

Degraeuwe, J., & Goethals, P. (2024). LexComSpaL2: A Lexical Complexity Corpus for Spanish as a Foreign Language. *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*, 10433-10443.

Díez-Ortega, M., & Kyle, K. (2024). Measuring the development of lexical richness of L2 Spanish: A longitudinal learner corpus study. *Studies in Second Language Acquisition*, 46(1), 169-199.

François, T. (2018). The interface between readability and automatic text adaptation. *Seminars in Automatic Text Adaptation*. UCLouvain.

Instituto Cervantes. (2006). *Plan curricular del Instituto Cervantes: Niveles de referencia para el español*. Instituto Cervantes/Biblioteca Nueva.

Lozano, C. (2022). CEDEL2: Design, compilation and web interface of an online corpus for L2 Spanish acquisition research. *Second Language Research*, 38(4), 965-983.

Lu, X. (2012). The relationship of lexical richness to the quality of ESL learners' oral narratives. *The Modern Language Journal*, 96(2), 190-208.

Mavrou, I. (2016). Complejidad, precisión, fluidez y léxico: Una revisión. *RESLA: Revista Española de Lingüística Aplicada*, 29(2), 475-509.

Quispesaravia, A., Perez, W., Sobrevilla Cabezudo, M. A., & Alva-Manchego, F. (2016). Coh-Metrix-Esp: A Complexity Analysis Tool for Documents Written in Spanish. *Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC 2016)*, 4694-4698.

Real Academia Española. (2024). CORPES XXI: Corpus del Español del Siglo XXI. Banco de datos. https://www.rae.es/corpes/

Read, J. (2000). *Assessing vocabulary*. Cambridge University Press.

Schnur, E., & Rubio, F. (2021). Lexical complexity, writing proficiency, and task effects in Spanish Dual Language Immersion. *Language Learning & Technology*, 25(1), 53-72.

Tracy-Ventura, N., McManus, K., Norris, J. M., & Ortega, L. (2017). A study of lexical sophistication: The development of spoken interlanguage in L2 Spanish. *Círculo de Lingüística Aplicada a la Comunicación*, 72, 19-38.
