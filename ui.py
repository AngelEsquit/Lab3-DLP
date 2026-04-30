"""
Módulo para la interfaz de usuario.
"""

from parser import GrammarParser
from analyzer import GrammarAnalyzer

class UI:
    """Interfaz de usuario para interactuar con el analizador de gramáticas."""
    
    @staticmethod
    def print_header():
        """Imprime encabezado del programa."""
        print("\n" + "="*60)
        print("  FUNCIONES PRIMERO Y SIGUIENTE")
        print("  Análisis de Gramáticas Libres de Contexto")
        print("="*60 + "\n")
    
    @staticmethod
    def print_menu():
        """Imprime menú principal."""
        print("\n1. Ingresar nueva gramática")
        print("2. Usar gramática predefinida")
        print("3. Salir")
        print("-" * 40)
    
    @staticmethod
    def print_grammar(grammar):
        """Imprime la gramática parseada."""
        print("\n" + "="*60)
        print("GRAMÁTICA INGRESADA:")
        print("="*60)
        print(grammar)
    
    @staticmethod
    def print_symbols(grammar):
        """Imprime terminales y no-terminales."""
        print("="*60)
        print("SÍMBOLOS:")
        print("="*60)
        print(f"No-terminales: {sorted(grammar.non_terminals)}")
        print(f"Terminales:    {sorted(grammar.terminals)}")
        print(f"Símbolo inicial: {grammar.start_symbol}\n")
    
    @staticmethod
    def print_first_sets(analyzer):
        """Imprime los conjuntos FIRST."""
        print("="*60)
        print("CONJUNTOS FIRST:")
        print("="*60)
        
        for nt in sorted(analyzer.grammar.non_terminals):
            first_set = analyzer.get_first(nt)
            first_str = "{" + ", ".join(sorted(first_set)) + "}"
            print(f"  FIRST({nt:3}) = {first_str}")
        print()
    
    @staticmethod
    def print_follow_sets(analyzer):
        """Imprime los conjuntos FOLLOW."""
        print("="*60)
        print("CONJUNTOS FOLLOW:")
        print("="*60)
        
        for nt in sorted(analyzer.grammar.non_terminals):
            follow_set = analyzer.get_follow(nt)
            follow_str = "{" + ", ".join(sorted(follow_set)) + "}"
            print(f"  FOLLOW({nt:3}) = {follow_str}")
        print()
    
    @staticmethod
    def print_complete_analysis(grammar, analyzer):
        """Imprime análisis completo."""
        UI.print_grammar(grammar)
        UI.print_symbols(grammar)
        UI.print_first_sets(analyzer)
        UI.print_follow_sets(analyzer)
    
    @staticmethod
    def get_user_choice():
        """Obtiene la opción del usuario."""
        try:
            choice = input("Seleccione opción: ").strip()
            return choice
        except KeyboardInterrupt:
            return "3"
    
    @staticmethod
    def analyze_grammar():
        """Flujo para analizar una gramática."""
        print("\nIngrese la gramática (un no-terminal por línea)")
        print("Formato: A -> a | B C | ε")
        print("Ingrese línea vacía para terminar:\n")
        
        lines = []
        while True:
            try:
                line = input()
                if not line.strip():
                    break
                lines.append(line)
            except KeyboardInterrupt:
                return None
        
        if not lines:
            print("No se ingresó ninguna gramática.")
            return None
        
        text = '\n'.join(lines)
        
        try:
            grammar = GrammarParser.parse(text)
            analyzer = GrammarAnalyzer(grammar)
            analyzer.calculate_first()
            analyzer.calculate_follow()
            
            return grammar, analyzer
        except Exception as e:
            print(f"\nError al parsear la gramática: {e}")
            return None
