# Ashvin Pidaparti pidap008
#I understand that this is a graded, individual examination that may not be
#discussed with anyone. I also understand that obtaining solutions or
#partial solutions from outside sources, or discussing any aspect of the examination
#with anyone is academic misconduct and will result in failing the course.
#I further certify that this program represents my own work and that none of
#it was obtained from any source other than material presented as part of the
#course.

import turtle
import complex
import mandelbrot

class Display:
    def __init__(self,res=50):
        self.t = turtle.Turtle()
        self.t.up()
        self.t.ht()
        self.t.speed(0)
        self.t.screen.tracer(2000, 0)
        self.t.pensize(1)
        self.scr = self.t.getscreen()
        self.screensize = self.scr.screensize()
        self.real_range = (2, -2)
        self.imag_range = (2, -2 )
        self.t.goto(-1 * (self.screensize[0]),-1 * (self.screensize[1]))
        for x in range(-1 * self.screensize[0],self.screensize[0]): #iterates through every pixel
            self.t.up()
            for y in range(-1 * self.screensize[1],self.screensize[1]):
                complex_point = complex.Complex(2* x/self.screensize[0],2*y/self.screensize[1]) #creates complex object to create mandelbrot object
                self.t.color(mandelbrot.Mandelbrot(complex_point,res).get_color())
                if y == -1 * self.screensize[1]:
                    self.t.up()
                self.t.goto(x,y)  #don't try to pen up/down before/after the goto; it slows it way down
                self.t.pd()
    def draw(self,x,y,res=50):
        self.t.up()
        self.t.goto(-1 * self.screensize[0],-1 * self.screensize[1])   #stops from drawing line across screen
        self.t.pd()
        for xcor in range(-1 * self.screensize[0],self.screensize[0]):
            for ycor in range(-1 * self.screensize[1],self.screensize[1]):
                complex_point = complex.Complex(((xcor + 2*x) * (self.real_range[0] - self.real_range[1]))/(2 * self.screensize[0]), #converts x/y to complex with
                ((ycor + 2*y) * (self.imag_range[0] - self.imag_range[1]))/(2 *self.screensize[1]))                                 #modified complex range
                self.t.color(mandelbrot.Mandelbrot(complex_point,res).get_color())
                if ycor == -1 * self.screensize[1] or xcor == -1 * self.screensize[0]:
                    self.t.up()
                self.t.goto(xcor,ycor)
                self.t.down()
    def zoom(self,x,y,res=50):
        self.real_range = (2 * x / self.screensize[0] + self.real_range[0]/2, 2 * x / self.screensize[0] + self.real_range[1]/2)    #range = point + .5 * old range
        self.imag_range = (2 * y / self.screensize[0] + self.imag_range[0]/2, 2 * y / self.screensize[1] + self.imag_range[1]/2)
        self.draw(x,y,res)
    def click(self):
        self.scr.onclick(self.zoom)     #puts it all together
        self.scr.listen()
def main():
    d = Display()
    d.click()

if __name__ == "__main__":
    main()
