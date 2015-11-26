##### start dual number class #####

class dualNum:
    """
    class for dual numbers
    epsilon is the base unit defined as:
        epsilon**2 == 0 and epsilon != 0
    """

    def __init__(self, real, dual):
        assert isinstance(real, (float, int)) and\
            isinstance(dual, (float, int))
        self.a = real
        self.b = dual
    
    def __repr__(self):
        return str(self.a) + "+" + str(self.b) +"*epsilon"
    
    def __str__(self):
        if self.b == 0:
            return str(self.a)
        return str(self.a) + "+" + str(self.b) +"\xce\xb5"
        
    def __cmp__(self, other):
        raise TypeError("no ordering relation is defined for dual numbers")
    
    def __nonzero__(self):
        if self.a == 0 and self.b == 0:
            return false
        return true
    
    def __call__(self, *args):
        raise TypeError("'dualNum' object is not callable")
    
    def __len__(self):
        if self.b == 0:
            return 1
        return 2
    
    def __add__(self, other):
        if isinstance(other, (float, int)):
            return dualNum(other+self.a, self.b)
        return dualNum(other.a+self.a, other.b+self.b)
    
    def __sub__(self, other):
        if isinstance(other, (float, int)):
            return dualNum(self.a-other, self.b)
        return dualNum(other.a-self.a, other.b-self.b)
    
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return dualNum(other*self.a,other*self.b)
        return dualNum(self.a*other.a, self.a*other.b + self.b*other.a)
    
    def __div__(self, other):
        if isinstance(other, (float, int)):
            return dualNum(self.a/other, self.b/other)
        return dualNum(self.a/other.a, 0)
    
    def __pow__(self, other):
        assert isinstance(other, int), "float and othe dual number powers\
        are not avalible for use at the moment"
        if other == 1:
            return self
        elif other == 2:
            return dualNum(self.a**2, 2*self.a*self.b)
        elif other > 1:
            return self * self**(other-1)
        else:
            return (self**(other+1))/self
    
    def __radd__(self, other):
        if isinstance(other, (float, int)):
            return dualNum(other+self.a, self.b)
        return dualNum(other.a+self.a, other.b+self.b)
    
    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            return dualNum(-self.a+other, -self.b)
        return dualNum(other.a-self.a, other.b-self.b)
    
    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            return dualNum(other*self.a,other*self.b)
        return dualNum(self.a*other.a, self.a*other.b + self.b*other.a)
    
    def __neg__(self):
        return dualNum(-self.a, -self.b)
    
    def __pos__(self):
        return self
    
    def __abs__(self):
        return sqrt(self.a**2+self.b**2)
    

epsilon = dualNum(0, 1) #while not part of the class, but very important to the
    #functioning of the class

##### end dual number class #####
