import numpy as np
import sympy as sym

class FunctionCreator:
    def __init__(self):
        """
        Initialize the FunctionCreator class attributes.
        
        Attributes:
            __x (sympy.Symbol): Symbolic variable used in the function expressions.
            PolyOrder (int): Randomly generated polynomial order between 1 and 4.
            base (int): Randomly generated base coefficient between -5 and 5.
            FunList (list): Predefined list of transcendental functions.
            fx (sympy.Expr): User-defined function, initially set to 0.
            __min_poly (int or None): Minimum polynomial order, initially None.
            __max_poly (int or None): Maximum polynomial order, initially None.
            __min_base (int or None): Minimum base coefficient, initially None.
            __max_base (int or None): Maximum base coefficient, initially None.
            __derivate_order (int): Current derivative order, initially set to 1.
        """
        
        self.__x = sym.symbols('x')
        self.PolyOrder = np.random.randint(1, 5)
        self.base = np.random.randint(-5, 6)
        
        # Lista di Funzioni Trascendentali
        self.FunList = [
            sym.cos(self.__x), 
            sym.sin(self.__x), 
            sym.exp(self.__x), 
            sym.log(self.__x), 
            1 + sym.exp(-self.__x)
        ]
        
        # Funzione Utente
        self.fx = 0
        
        # Attributi
        self.__min_poly = None
        self.__max_poly = None
        self.__min_base = None
        self.__max_base = None
        self.__derivate_order = 1
        
    # ------------------ Poly Order --------------------
    def set_poly_order(self, min_, max_):
        """
        Sets the minimum and maximum limits for the polynomial order.
    
        Randomly generates a polynomial order (`PolyOrder`) between `min_` and `max_`.
    
        Args:
            min_ (int): Minimum limit for the polynomial order.
            max_ (int): Maximum limit for the polynomial order.
        """
        self.__min_poly = min_
        self.__max_poly = max_
        self.PolyOrder = np.random.randint(self.__min_poly, self.__max_poly)
        
    def get_poly_order(self):
        """
        Returns the minimum and maximum limits for the polynomial order.
    
        Returns:
            tuple: A tuple containing the minimum and maximum limits for the polynomial order.
        """
        return (self.__min_poly, self.__max_poly)
            
    # ---------------------- Base ------------------------
    def set_base_range(self, min_base, max_base):
        """
        Sets the minimum and maximum limits for the base coefficient.
    
        Args:
            min_base (int): Minimum limit for the base coefficient.
            max_base (int): Maximum limit for the base coefficient.
        """
        self.__min_base = min_base
        self.__max_base = max_base
            
    def set_base(self):
        """
        Randomly generates a base coefficient (`base`) between the previously set minimum and maximum limits.
        """
        self.base = np.random.randint(self.__min_base, self.__max_base)
    
    # --------------------- Function ------------------------
    def add_function_to_list(self, new_function):
        """
        Adds a new function to the list of transcendental functions.
    
        Args:
            new_function (sympy function): The new function to add to the list of transcendental functions.
        
        Raises:
            Exception: If an error occurs while adding the new function.
        """
        try:
            self.FunList.append(new_function)
        except Exception as e:
            print(f"An error occurred: {e}")
                
    def make_numerator(self):
        """
        Creates the numerator of the user-defined function.
    
        The function combines polynomial terms and randomly selected transcendental functions from the `FunList`.
        """
        for i in range(1, self.PolyOrder):
            self.fx += self.base * self.__x**i
    
        transcend = np.random.choice(self.FunList, 2, replace=False)
        for f in transcend:
            self.fx += np.random.choice([-1, 1]) * f
            
    def make_denominator(self):
        """
        Creates the denominator of the user-defined function.
    
        Randomly selects a transcendental function from the `FunList` and uses it as the denominator of the user-defined function.
        """
        denom = np.random.choice(self.FunList, 1)[0]
        self.fx /= denom
            
    # ---------------- Derivates and Plot ------------------------
    def next_derivate(self):
        """
        Calculates the next derivative of the user-defined function.
    
        Increments the derivative order (`__derivate_order`) and calculates the derivative of the user-defined function (`fx`) with respect to the variable `x`.
        """
        self.__derivate_order += 1
        self.fx = sym.diff(self.fx, self.__x, self.__derivate_order)
            
    def plot_function(self):
        """
        Plots the current user-defined function (`fx`).
        """
        sym.plot(self.fx)
            
    # ------------------- Reset Func ------------------------
    def reset_function(self):
        """
        Resets the user-defined function (`fx`) to 0.
        """
        self.fx = 0
    
    