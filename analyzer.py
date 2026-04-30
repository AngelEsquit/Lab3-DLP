"""
Módulo para calcular las funciones FIRST y FOLLOW de una gramática.
"""

class GrammarAnalyzer:
    """
    Calcula los conjuntos FIRST y FOLLOW de una gramática libre de contexto.
    """
    
    def __init__(self, grammar):
        """
        Inicializa el analizador.
        
        Args:
            grammar (Grammar): La gramática a analizar
        """
        self.grammar = grammar
        self.first = {}  # {símbolo: set(terminales)}
        self.follow = {}  # {no-terminal: set(terminales)}
    
    def calculate_first(self):
        """
        Calcula la función FIRST para todos los símbolos.
        
        FIRST(A) = conjunto de terminales que pueden aparecer al inicio
        de cualquier derivación desde A.
        """
        # Inicializar FIRST vacío para cada no-terminal
        for nt in self.grammar.non_terminals:
            self.first[nt] = set()
        
        # FIRST para terminales
        for t in self.grammar.terminals:
            self.first[t] = {t}
        
        # Iteración hasta convergencia
        changed = True
        iterations = 0
        max_iterations = 100  # Prevenir loops infinitos
        
        while changed and iterations < max_iterations:
            changed = False
            iterations += 1
            
            for lhs in self.grammar.non_terminals:
                for rhs in self.grammar.productions[lhs]:
                    # Procesar cada alternativa
                    self._add_first_from_rhs(lhs, rhs)
                    
                    # Verificar si hubo cambios
                    if len(self.first[lhs]) > 0:
                        changed = True
        
        return self.first
    
    def _add_first_from_rhs(self, lhs, rhs):
        """
        Añade símbolos FIRST de una producción al FIRST del lhs.
        
        Args:
            lhs (str): No-terminal del lado izquierdo
            rhs (str): Producción del lado derecho
        """
        symbols = rhs.split()
        
        # Caso epsilon
        if len(symbols) == 1 and symbols[0] == 'ε':
            self.first[lhs].add('ε')
            return
        
        # Para cada símbolo en la producción
        all_can_be_epsilon = True
        for symbol in symbols:
            if symbol in self.first:
                # Añadir FIRST(símbolo) - {ε}
                for t in self.first[symbol]:
                    if t != 'ε':
                        self.first[lhs].add(t)
                
                # Si no contiene epsilon, parar
                if 'ε' not in self.first[symbol]:
                    all_can_be_epsilon = False
                    break
            else:
                # Es un terminal (podría no estar en first aún)
                if symbol != 'ε':
                    self.first[lhs].add(symbol)
                all_can_be_epsilon = False
                break
        
        # Si todos los símbolos tienen epsilon
        if all_can_be_epsilon:
            self.first[lhs].add('ε')
    
    def calculate_follow(self):
        """
        Calcula la función FOLLOW para todos los no-terminales.
        
        FOLLOW(A) = conjunto de terminales que pueden aparecer inmediatamente
        después de A en alguna forma sentencial.
        """
        # Inicializar FOLLOW vacío
        for nt in self.grammar.non_terminals:
            self.follow[nt] = set()
        
        # FOLLOW(S) contiene $ (fin de entrada)
        if self.grammar.start_symbol:
            self.follow[self.grammar.start_symbol].add('$')
        
        # Iteración hasta convergencia
        changed = True
        iterations = 0
        max_iterations = 100
        
        while changed and iterations < max_iterations:
            changed = False
            iterations += 1
            
            for lhs in self.grammar.non_terminals:
                for rhs in self.grammar.productions[lhs]:
                    symbols = rhs.split()
                    
                    # Para cada símbolo en la producción
                    for i, symbol in enumerate(symbols):
                        if self.grammar.is_non_terminal(symbol):
                            # Mirar lo que viene después
                            rest = symbols[i+1:]
                            
                            if rest:
                                # Hay símbolos después
                                self._add_follow_from_rest(symbol, rest)
                                changed = True
                            else:
                                # No hay nada después, añadir FOLLOW(lhs)
                                old_size = len(self.follow[symbol])
                                self.follow[symbol].update(self.follow[lhs])
                                if len(self.follow[symbol]) > old_size:
                                    changed = True
        
        return self.follow
    
    def _add_follow_from_rest(self, symbol, rest_symbols):
        """
        Añade símbolos FOLLOW basado en lo que viene después.
        
        Args:
            symbol (str): No-terminal para el cual calcular FOLLOW
            rest_symbols (list): Símbolos que vienen después
        """
        all_have_epsilon = True
        
        for rest_sym in rest_symbols:
            if rest_sym in self.first:
                # Añadir FIRST(rest_sym) - {ε}
                for t in self.first[rest_sym]:
                    if t != 'ε':
                        self.follow[symbol].add(t)
                
                # Si no tiene epsilon, parar
                if 'ε' not in self.first[rest_sym]:
                    all_have_epsilon = False
                    break
            else:
                # Es un terminal
                if rest_sym != 'ε':
                    self.follow[symbol].add(rest_sym)
                all_have_epsilon = False
                break
    
    def get_first(self, symbol):
        """Retorna el conjunto FIRST de un símbolo."""
        return self.first.get(symbol, set())
    
    def get_follow(self, symbol):
        """Retorna el conjunto FOLLOW de un símbolo."""
        return self.follow.get(symbol, set())
