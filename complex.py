class Complex:
    def __init__(self,real=0.0,imag=0.0):
        self.__real = float(real)
        self.__imag = float(imag)
    def __repr__(self):
        if self.__imag >= 0:
            return str(self.__real) + " + " + str(self.__imag) + "i"
        elif self.__imag < 0:
            return str(self.__real) + " - " + str(self.__imag) + "i"
    def getReal(self):
        print(self.__real)
    def getImag(self):
        print(self.__imag)
    def __add__(self,number2):
        self.__real += number2.__real       #adds
        self.__imag += number2.__imag
        return self
    def __mul__(self,number2):  #FOILs the two numbers
        newComplex = Complex(0,0)
        newComplex.__real = self.__real * number2.__real    #First
        newComplex.__real += -(self.__imag * number2.__imag)    #last
        newComplex.__imag = (self.__imag * number2.__real) + (self.__real * number2.__imag)     #outside and inside
        return newComplex
    def __abs__(self):
        distance = ((self.__real)**(2) + (self.__imag)**2)**.5
        return distance
