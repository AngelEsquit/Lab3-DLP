# Funciones Primero y Siguiente - Lab 3 DLP

## Descripción
Programa que implementa el cálculo de las funciones **FIRST** (primero) y **FOLLOW** (siguiente) para gramáticas libres de contexto.

## Estructura del Proyecto

```
├── main.py           # Programa principal interactivo
├── demo.py           # Demostración automatizada
├── grammar.py        # Clase Grammar
├── parser.py         # Parser de gramáticas
├── analyzer.py       # Algoritmos FIRST y FOLLOW
├── ui.py             # Interfaz de usuario
├── test_cases.py     # Gramáticas predefinidas
└── README.md         # Este archivo
```

## Requisitos
- Python 3.6 o superior
- No requiere librerías externas

## Uso

### Ejecutar Programa Interactivo
```bash
python main.py
```

### Ejecutar Demostración
```bash
python demo.py
```

## Funcionalidades

### 1. Ingresar Gramática Manualmente
- Formato: `A -> a | B C | ε`
- Línea vacía para terminar
- Identifica automáticamente terminales y no-terminales

### 2. Usar Gramáticas Predefinidas
- Expresiones aritméticas
- Producciones con epsilon
- Palíndromos

### 3. Cálculo FIRST
Calcula el conjunto de terminales que pueden aparecer al inicio de cualquier derivación desde un no-terminal.

### 4. Cálculo FOLLOW
Calcula el conjunto de terminales que pueden aparecer inmediatamente después de un no-terminal.

## Algoritmos Implementados

### FIRST
- Basado en iteración hasta convergencia
- Maneja epsilon correctamente
- Máximo 100 iteraciones

### FOLLOW
- Incluye símbolo $ para el símbolo inicial
- Propaga FIRST de símbolos siguientes
- Maneja epsilon en cadenas de derivación

## Ejemplos de Uso

### Ejemplo 1: Expresiones Aritméticas
```
E -> E + T | T
T -> T * F | F
F -> ( E ) | id
```

### Ejemplo 2: Con Epsilon
```
S -> A B
A -> a A | ε
B -> b B | ε
```

## Notas Importantes
- No utiliza librerías automáticas para calcular FIRST/FOLLOW
- Todos los algoritmos están implementados manualmente
- La interfaz es por consola