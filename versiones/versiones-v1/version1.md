
---

# 🎯 Objetivo de Worship v1

Resolver expresiones como:

```
( 2 + 3 ) * 4
10 + 5 * 2
( 8 / 2 ) + 3 * ( 2 + 1 )
```

Respetando:

* Paréntesis
* Prioridad de operadores
* Arquitectura MVC
* POO pura
* Escalable a GeoGebra / SymPy

---

# 🗂️ Estructura final de carpetas

```
MathWorship/
│
├── main.py
│
├── views/
│   └── console_view.py
│
├── controllers/
│   └── calc_controller.py
│
├── models/
│   ├── base_operation.py
│   ├── parser/
│   │   └── expression_parser.py
│   │
│   └── operations/
│       ├── add/add_model.py
│       ├── sub/sub_model.py
│       ├── mul/mul_model.py
│       └── div/div_model.py
```

---

# 🧠 IDEA ARQUITECTÓNICA

Tu sistema tiene 4 cerebros:

| Capa               | Función                          |
| ------------------ | -------------------------------- |
| View               | Recibe lo que escribe el usuario |
| Controller         | Decide qué hacer                 |
| Parser (Model)     | Entiende la expresión matemática |
| Operations (Model) | Ejecuta las matemáticas          |

---

# 🔄 FLUJO COMPLETO (paso a paso real)

Supongamos que el usuario escribe:

```
( 2 + 3 ) * 4
```

---

## 1️⃣ main.py — Punto de entrada

```python
run()
```

Llama a la vista.

---

## 2️⃣ console_view.py — VIEW

```python
expr = input(...)
result = controller.operate(expr)
```

La vista **no sabe matemáticas**.
Solo pasa el texto al controller.

---

## 3️⃣ calc_controller.py — CONTROLLER

```python
return self.parser.evaluate(expression)
```

El controller no calcula.
Solo delega al parser.

---

## 4️⃣ expression_parser.py — EL CEREBRO REAL

Aquí pasa lo importante.

### Paso A — Tokenización

Convierte el string en piezas:

```
['(', '2', '+', '3', ')', '*', '4']
```

---

### Paso B — Algoritmo Shunting Yard (Dijkstra)

Convierte de notación normal a **postfija (RPN)**:

```
2 3 + 4 *
```

¿Por qué?

Porque esta forma elimina paréntesis y prioridades.

---

### Paso C — Evaluación postfija

Lee de izquierda a derecha:

1. Apila `2`
2. Apila `3`
3. Ve `+` → llama a **AddOperation**
4. Resultado `5` vuelve a la pila
5. Apila `4`
6. Ve `*` → llama a **MulOperation**
7. Resultado final `20`

---

## 5️⃣ operations/add_model.py (POO)

```python
def execute(self, numbers):
    return sum(numbers)
```

Cada operador es una clase independiente.

---

# 🧠 ¿Por qué esto es tan importante?

Porque tu sistema NO evalúa con `eval()`.

Evalúa así:

```
Parser → Operation Objects → Resultado
```

Exactamente como:

* GeoGebra
* Wolfram
* SymPy
* Motores CAS

---

# 🗺️ Mapa visual del flujo

```
Usuario escribe expresión
          ↓
       VIEW
          ↓
    CONTROLLER
          ↓
       PARSER
          ↓
 convierte a RPN
          ↓
 llama a objetos Operation (POO)
          ↓
      Resultado
```

---

# 🔥 Lo que ya lograste (muy importante)

Sin darte cuenta construiste:

> Un **evaluador de expresiones matemáticas orientado a objetos**

Eso es **la base exacta** para luego soportar:

```
x^2 + 3x
sin(x)
derivar(...)
matrices
vectores
```

Sin cambiar la arquitectura.

---

# 🧩 Por qué esto escala perfecto a GeoWorship

Porque luego solo cambias:

```
float → símbolos (SymPy)
```

Y todo sigue funcionando.

---

# 🏁 Resumen conceptual para tu tesis

Worship v1 implementa un motor de evaluación matemática basado en:

* Arquitectura MVC
* Programación Orientada a Objetos
* Algoritmo Shunting Yard para parsing
* Evaluación postfija desacoplada por clases de operación

Esto permite una evolución directa hacia un sistema de álgebra simbólica y graficación interactiva.
