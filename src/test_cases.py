"""
Gramáticas predefinidas para pruebas.
"""

# Gramática 1: Expresiones aritméticas simples
GRAMMAR_1 = """
E -> E + T | T
T -> T * F | F
F -> ( E ) | id
"""

# Gramática 2: Sentencias simples con epsilon
GRAMMAR_2 = """
S -> A B
A -> a A | ε
B -> b B | ε
"""

# Gramática 3: Más compleja con multiple alternativas
GRAMMAR_3 = """
S -> a S b | c
"""

GRAMMARS = {
    "1": ("Expresiones aritméticas", GRAMMAR_1),
    "2": ("Asignaciones con epsilon", GRAMMAR_2),
    "3": ("Palíndromos", GRAMMAR_3),
}

def get_predefined_grammar(choice):
    """
    Obtiene una gramática predefinida.
    
    Args:
        choice (str): Número de gramática
        
    Returns:
        tuple: (nombre, texto_gramática) o None
    """
    return GRAMMARS.get(choice)

def list_grammars():
    """Lista las gramáticas disponibles."""
    print("\nGramáticas predefinidas:")
    for key, (name, _) in GRAMMARS.items():
        print(f"  {key}. {name}")
