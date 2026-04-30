"""
Programa principal para análisis de funciones FIRST y FOLLOW.
"""

from parser import GrammarParser
from analyzer import GrammarAnalyzer
from ui import UI
from test_cases import get_predefined_grammar, list_grammars

def main():
    """Función principal del programa."""
    UI.print_header()
    
    while True:
        UI.print_menu()
        choice = UI.get_user_choice()
        
        if choice == "1":
            # Ingresar nueva gramática
            result = UI.analyze_grammar()
            if result:
                grammar, analyzer = result
                UI.print_complete_analysis(grammar, analyzer)
                input("\nPresione Enter para continuar...")
        
        elif choice == "2":
            # Usar gramática predefinida
            list_grammars()
            grammar_choice = input("\nSeleccione gramática: ").strip()
            
            result = get_predefined_grammar(grammar_choice)
            if result:
                name, text = result
                print(f"\nCargando: {name}")
                
                try:
                    grammar = GrammarParser.parse(text)
                    analyzer = GrammarAnalyzer(grammar)
                    analyzer.calculate_first()
                    analyzer.calculate_follow()
                    
                    UI.print_complete_analysis(grammar, analyzer)
                    input("\nPresione Enter para continuar...")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Opción inválida.")
        
        elif choice == "3":
            print("\n¡Hasta luego!\n")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
