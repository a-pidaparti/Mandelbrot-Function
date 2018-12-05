from complex import Complex
class Mandelbrot:
    def __init__(self,C0,limit=50):
        self.__limit = limit
        self.__cardinality = 0
        self.__colormap = ["red","salmon","orange","gold","seagreen","chartreuse",
        "green","darkgreen","cyan","blue","darkorchid","magenta","maroon"]
        self.__C0 = C0
        z = Complex(0,0)    #start point for set
        iterations = int(limit)
        while iterations > 0:
            z = (z * z) + C0    #definition of set
            if abs(z) <= 2:
                self.__cardinality += 1
            elif abs(z) > 100:  #if greater than 100, it is not in the set
                iterations = 0
            iterations -= 1
    def get_color(self):
        if self.__cardinality == self.__limit:
            return "black"
        elif round(13 * self.__cardinality/self.__limit,0) == 0:
            return "red"
        else:
            color_number = round(13 * (self.__cardinality/self.__limit),0) - 1
            return self.__colormap[int(color_number)]
