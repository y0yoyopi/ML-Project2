# ML-Project2
# 🌳 Classification Video Demo: Decision Trees

> **Curso:** Machine Learning  
> **Proyecto:** Classification Video  
> **Herramienta de Animación:** [Manim Community](https://www.manim.community/) <br>
> **Integrantes:** Aaron Rojas; Piero Pilco; Mateo Silva

## 📖 Descripción del Proyecto

Este repositorio contiene el código fuente para generar una demostración visual educativa sobre **Árboles de Decisión (Decision Trees)** y **Random Forest**. 

El objetivo principal es deconstruir la "caja negra" de estos algoritmos, utilizando animaciones para explicar conceptos matemáticos complejos de manera intuitiva. Desde la entropía y el criterio de división (Split), hasta la construcción recursiva del árbol y la solución al overfitting mediante ensamblaje (Ensembling).

## 🚀 Contenido del Video (Estructura del Código)

El proyecto se divide en 5 escenas principales animadas con Python:

1.  **Introducción e Intuición:** Visualización de un camino de decisiones binarias usando ejemplos cotidianos.
2.  **Criterio de División (Gini Impurity):** * Animación de partículas separándose físicamente (Intuición).
    * Explicación matemática de la fórmula de Gini e Impureza.
3.  **Construcción del Árbol:** Simulación del algoritmo con un dataset bancario, mostrando cómo las filas de la tabla se mueven y transforman en nodos.
4.  **Dataset Real (Wine Quality):** * Visualización de fronteras de decisión ortogonales.
    * Análisis de métricas y demostración visual de Overfitting vs. Poda.
5.  **Random Forest:** Animación de múltiples árboles (Bagging) y el proceso de Votación por Mayoría.

## 🛠️ Requisitos e Instalación

Este proyecto fue diseñado para ejecutarse en **Google Colab** o en un entorno local con las siguientes dependencias:

```bash
manim
numpy
pandas
scikit-learn
