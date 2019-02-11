from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=y1-y0 
    B=x1-x0
    if B==0:
        if(y<y1):
            while(y<y1):
                plot(screen,color,x,y)
                y+=1
        else:
            while(y>y1):
                plot(screen,color,x,y)
                y-=1
    else:
        if x0<x1:#oct 1 && oct 2
            slope=A/B
            if slope<=1 and slope>=0:
                d=2*A-B
                while x <= x1:
                    plot(screen,color,x,y)
                    if d > 0:
                        y+=1
                        d-=2*B
                    x+=1
                    d+=2*A
            elif slope >1:
                d=A-2*B
                while y <= y1:
                    plot(screen,color,x,y)
                    if d<0:
                        x+=1
                        d+=2*A
                    y+=1
                    d-=2*B
            #oct 7 && oct 8
            elif slope>=-1 and slope<0:
                d=2*A+B
                while x <= x1:
                    plot(screen,color,x,y)
                    if d<0:
                        y-=1
                        d+=2*B
                    x+=1
                    d+=2*A
            elif slope <-1:
                d=A+2*B
                while y >= y1:
                    plot(screen,color,x,y)
                    if d > 0:
                        x+=1
                        d+=2*A
                    y-=1
                    d+=2*B
        elif x0>x1:
            draw_line(x1,y1,x0,y0,screen,color)
        else:
            draw_line(x1,y1,x0,y0,screen,color)
