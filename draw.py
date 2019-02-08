from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=abs(y1-y0)
    B=abs(x1-x0)
    if y0<y1:#oct 1 && oct 8
            d=2A-B
            while x <=x1:
                plot(screen,color,x,y)
                if d > 0:
                    y++
                    d-=2B
                x++
                d+=2A
    else if y0>y1:
            pass
    else:#dot
            plot(screen,color, x0,y0)
