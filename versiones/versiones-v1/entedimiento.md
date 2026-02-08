Aquí tienes un **README.md profesional** explicando claramente que la v1 es una **arquitectura base experimental** pensada para luego integrar librerías como SymPy sin cambiar el diseño.

Puedes copiar y pegar directamente en tu `README.md`.

---

# 🧮 MathWorship v1 — Núcleo de Arquitectura Matemática

## 📌 Descripción

**MathWorship v1** no es una simple calculadora.

Es la **primera versión de una arquitectura experimental** diseñada para construir, paso a paso, un **motor matemático tipo GeoGebra**, basado en:

* Arquitectura **MVC**
* Programación Orientada a Objetos (POO)
* Separación estricta de responsabilidades
* Evaluación de expresiones matemáticas con paréntesis y prioridad de operadores

Esta versión implementa únicamente aritmética básica:

* Suma
* Resta
* Multiplicación
* División

Pero su objetivo **NO es la calculadora**, sino sentar la base del **diseño del motor matemático**.

---

## 🎯 Objetivo real de la v1

Construir desde cero el flujo que usan motores como:

* GeoGebra
* Wolfram
* SymPy
* Motores CAS (Computer Algebra Systems)

Es decir:

```
Texto → Parser → Orden lógico → Objetos de operación → Resultado
```

Sin usar librerías externas.

---

## 🧠 ¿Por qué no usar SymPy desde el inicio?

Porque esta versión busca:

* Entender cómo funciona internamente un evaluador matemático
* Diseñar una arquitectura escalable
* Separar correctamente View, Controller, Parser y Operations
* Dejar preparado el sistema para que, en versiones futuras, se pueda reemplazar el parser propio por librerías especializadas **sin cambiar la arquitectura**

---

## 🏗️ Arquitectura del proyecto

```
MathWorship/
│
├── main.py
├── views/
├── controllers/
├── models/
│   ├── parser/
│   └── operations/
```

### Responsabilidades

| Capa       | Función                                            |
| ---------- | -------------------------------------------------- |
| View       | Recibe la expresión del usuario                    |
| Controller | Orquesta el flujo                                  |
| Parser     | Interpreta la expresión matemática (Shunting Yard) |
| Operations | Ejecuta las operaciones mediante clases POO        |

---

## 🔄 Flujo del sistema

1. El usuario escribe una expresión:

   ```
   ( 8 / 2 ) + 3 * ( 2 + 1 )
   ```
2. La vista la envía al controller.
3. El controller llama al parser.
4. El parser convierte la expresión a notación postfija (RPN).
5. El evaluador recorre la RPN.
6. Cuando encuentra un operador, llama a la clase correspondiente:

   * `AddOperation`
   * `SubOperation`
   * `MulOperation`
   * `DivOperation`
7. Se obtiene el resultado final.

---

## 🚀 Visión a futuro (v2, v3…)

Gracias a esta arquitectura, en versiones posteriores será posible reemplazar:

```
ExpressionParser
```

por:

* `sympy.sympify`
* `asteval`
* `numexpr`

sin modificar:

* Views
* Controllers
* Operations

Esto convierte a MathWorship en una base sólida para evolucionar hacia:

* Álgebra simbólica
* Derivadas
* Integrales
* Gráficas 2D y 3D con Worship
* Interpretación de texto con IA

---

## ✅ Conclusión

MathWorship v1 demuestra que antes de usar librerías avanzadas, es fundamental diseñar correctamente:

> la arquitectura del motor matemático.

Esta versión es la **base conceptual y estructural** sobre la cual se construirán las siguientes versiones del sistema.
