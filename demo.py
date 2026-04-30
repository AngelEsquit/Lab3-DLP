"""
Script de demostración del programa.
Ejecuta las dos gramáticas de prueba y muestra los resultados.
"""

from parser import GrammarParser
from analyzer import GrammarAnalyzer
from ui import UI

def demonstrate():
    """Ejecuta demostración con dos gramáticas diferentes."""
    
    UI.print_header()
    
    # Gramática 1: Expresiones aritméticas
    print("\n" + "="*60)
    print("DEMOSTRACIÓN 1: EXPRESIONES ARITMÉTICAS")
    print("="*60)
    
    grammar1_text = """E -> E + T | T
T -> T * F | F
F -> ( E ) | id"""
    
    print("\nGramática:")
    print(grammar1_text)
    
    grammar1 = GrammarParser.parse(grammar1_text)
    analyzer1 = GrammarAnalyzer(grammar1)
    analyzer1.calculate_first()
    analyzer1.calculate_follow()
    
    UI.print_symbols(grammar1)
    UI.print_first_sets(analyzer1)
    UI.print_follow_sets(analyzer1)
    
    # Gramática 2: Con epsilon
    print("\n" + "="*60)
    print("DEMOSTRACIÓN 2: PRODUCCIONES CON EPSILON")
    print("="*60)
    
    grammar2_text = """S -> A B
A -> a A | ε
B -> b B | ε"""
    
    print("\nGramática:")
    print(grammar2_text)
    
    grammar2 = GrammarParser.parse(grammar2_text)
    analyzer2 = GrammarAnalyzer(grammar2)
    analyzer2.calculate_first()
    analyzer2.calculate_follow()
    
    UI.print_symbols(grammar2)
    UI.print_first_sets(analyzer2)
    UI.print_follow_sets(analyzer2)
    
    print("\n" + "="*60)
    print("DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
    print("="*60 + "\n")

if __name__ == "__main__":
    demonstrate()
