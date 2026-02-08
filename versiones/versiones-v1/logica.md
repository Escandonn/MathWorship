
```
( 8 / 2 ) + 3 * ( 2 + 1 )
```

y cómo el sistema decide **cuándo llamar suma, división, multiplicación, etc.**

---

# 🧠 IDEA CLAVE

Tu sistema trabaja en **dos fases**:

```
FASE 1 → Entender la expresión (Parser)
FASE 2 → Ejecutar operaciones (POO Operations)
```

---

# 🟦 FASE 1 — El Parser organiza el problema

### Entrada del usuario (View)

```
"( 8 / 2 ) + 3 * ( 2 + 1 )"
```

Llega al controller → parser.

---

## Paso 1 — Tokenización

El parser separa todo:

```
['(', '8', '/', '2', ')', '+', '3', '*', '(', '2', '+', '1', ')']
```

---

## Paso 2 — Shunting Yard (orden correcto sin paréntesis)

El parser convierte eso en notación postfija (RPN):

```
8 2 / 3 2 1 + * +
```

⚠️ Aquí está la magia.

Ya no hay paréntesis.
Ya no hay prioridades.

El orden correcto quedó codificado.

---

# 🟩 FASE 2 — Evaluación postfija (aquí se llaman tus clases POO)

Ahora el sistema recorre:

```
8 2 / 3 2 1 + * +
```

Usa una **pila (stack)**.

---

## 🔹 Token: `8`

Se apila:

```
[8]
```

---

## 🔹 Token: `2`

```
[8, 2]
```

---

## 🔹 Token: `/`  ← AQUÍ LLAMA DivOperation

Saca los dos últimos:

```
a = 8
b = 2
```

Llama:

```python
DivOperation.execute([8,2])
```

Resultado: `4`

Se vuelve a apilar:

```
[4]
```

---

## 🔹 Token: `3`

```
[4, 3]
```

---

## 🔹 Token: `2`

```
[4, 3, 2]
```

---

## 🔹 Token: `1`

```
[4, 3, 2, 1]
```

---

## 🔹 Token: `+`  ← LLAMA AddOperation

Saca:

```
a = 2
b = 1
```

```python
AddOperation.execute([2,1])
```

Resultado: `3`

Pila:

```
[4, 3, 3]
```

---

## 🔹 Token: `*`  ← LLAMA MulOperation

Saca:

```
a = 3
b = 3
```

```python
MulOperation.execute([3,3])
```

Resultado: `9`

Pila:

```
[4, 9]
```

---

## 🔹 Token: `+`  ← LLAMA AddOperation

Saca:

```
a = 4
b = 9
```

```python
AddOperation.execute([4,9])
```

Resultado: `13`

Pila final:

```
[13]
```

---

# 🎯 Resultado final: **13**

---

# 🗺️ Cuándo se llama cada operación

| Token encontrado | Clase que se llama |
| ---------------- | ------------------ |
| `+`              | AddOperation       |
| `-`              | SubOperation       |
| `*`              | MulOperation       |
| `/`              | DivOperation       |

El parser decide **cuándo**.

Las clases solo saben **cómo**.

---

# 🧠 ESTA ES LA CLAVE DE TU DISEÑO

El parser **nunca calcula**.

Las operaciones **nunca entienden paréntesis**.

Cada parte tiene una sola responsabilidad.

Eso es arquitectura limpia real.

---

# 📌 Resumen del flujo completo

```
Usuario escribe expresión
        ↓
View la pasa como texto
        ↓
Controller llama al Parser
        ↓
Parser convierte a RPN (orden correcto)
        ↓
Evaluator recorre RPN
        ↓
Cuando ve operador → llama clase POO correspondiente
        ↓
Resultado final
```

---

