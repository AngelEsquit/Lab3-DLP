"""
Módulo para representar y manipular gramáticas libres de contexto.
"""

class Grammar:
    """
    Representa una gramática libre de contexto.
    
    Atributos:
        productions: Dict[str, List[str]] - Mapeo de no-terminal a lista de producciones
        terminals: Set[str] - Conjunto de símbolos terminales
        non_terminals: Set[str] - Conjunto de símbolos no-terminales
        start_symbol: str - Símbolo inicial
    """
    
    def __init__(self):
        self.productions = {}  # {A: [producción1, producción2, ...]}
        self.terminals = set()
        self.non_terminals = set()
        self.start_symbol = None
    
    def add_production(self, lhs, rhs_list):
        """
        Añade producciones a la gramática.
        
        Args:
            lhs (str): Lado izquierdo de la producción (no-terminal)
            rhs_list (list): Lista de alternativas del lado derecho
        """
        if lhs not in self.productions:
            self.productions[lhs] = []
        
        self.non_terminals.add(lhs)
        
        # Si es el primer no-terminal añadido, es el símbolo inicial
        if self.start_symbol is None:
            self.start_symbol = lhs
        
        for rhs in rhs_list:
            self.productions[lhs].append(rhs)
    
    def identify_symbols(self):
        """
        Identifica automáticamente terminales y no-terminales.
        Los no-terminales deben ser mayúsculas o símbolos definidos como lhs.
        """
        self.terminals.clear()
        
        for lhs, rhs_list in self.productions.items():
            for rhs in rhs_list:
                symbols = rhs.split()
                for symbol in symbols:
                    if symbol == 'ε':  # Epsilon es especial
                        continue
                    if symbol not in self.non_terminals:
                        self.terminals.add(symbol)
    
    def get_all_symbols(self):
        """Retorna todos los símbolos de la gramática."""
        return self.terminals | self.non_terminals
    
    def is_terminal(self, symbol):
        """Verifica si un símbolo es terminal."""
        return symbol in self.terminals
    
    def is_non_terminal(self, symbol):
        """Verifica si un símbolo es no-terminal."""
        return symbol in self.non_terminals
    
    def __str__(self):
        """Representación en string de la gramática."""
        result = "Gramática:\n"
        for lhs in sorted(self.productions.keys()):
            alternatives = " | ".join(self.productions[lhs])
            result += f"  {lhs} -> {alternatives}\n"
        return result
