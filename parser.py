"""
Módulo para parsear gramáticas en formato texto.
"""

from grammar import Grammar

class GrammarParser:
    """
    Parsea gramáticas en formato texto a estructura Grammar.
    Formato esperado:
        A -> a | B C
        B -> b | ε
    """
    
    @staticmethod
    def parse(text):
        """
        Parsea una gramática desde un string.
        
        Args:
            text (str): Texto con la gramática
            
        Returns:
            Grammar: Objeto Grammar con la gramática parseada
        """
        grammar = Grammar()
        lines = text.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Separar LHS y RHS
            if '->' not in line:
                raise ValueError(f"Línea inválida: {line}")
            
            parts = line.split('->')
            lhs = parts[0].strip()
            rhs_str = parts[1].strip()
            
            # Separar alternativas
            alternatives = [alt.strip() for alt in rhs_str.split('|')]
            
            grammar.add_production(lhs, alternatives)
        
        # Identificar terminales
        grammar.identify_symbols()
        
        return grammar
    
    @staticmethod
    def parse_interactive():
        """
        Lee una gramática interactivamente desde consola.
        
        Returns:
            Grammar: Objeto Grammar
        """
        print("\n=== Ingrese la gramática ===")
        print("Formato: A -> a | B C | ε")
        print("Ingrese línea vacía para terminar:\n")
        
        lines = []
        while True:
            line = input().strip()
            if not line:
                break
            lines.append(line)
        
        text = '\n'.join(lines)
        
        try:
            grammar = GrammarParser.parse(text)
            return grammar
        except ValueError as e:
            print(f"Error al parsear: {e}")
            return None
