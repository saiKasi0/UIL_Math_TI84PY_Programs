from ti_system import *
from math import * 

def quad(a, b, c):
    d = b*b - 4*a*c
    if d < 0: return None
    x = sqrt(d)/(2*a)
    return -b/2/a + x, -b/2/a - x 

def ang_lines(m1, m2):
    if m1 == m2: return 0
    if m1 * m2 == -1: return 90
    return degrees(atan(abs((m1-m2)/(1+m1*m2))))

def sphere(r):
    return (4/3)*pi*r**3, 4*pi*r**2, 2*pi*r

def cone(r, h):
    s = sqrt(r*r + h*h)
    return pi*r*r*h/3, pi*r*(r + s), s

def seq_arith(a1, d, n):
    an = a1 + (n-1)*d
    return n*(a1 + an)/2, an  

def seq_geom(a1, r, n):
    an = a1*r**(n-1)
    return (a1*n if r==1 else a1*(1-r**n)/(1-r)), an

def polygon(s, n):
    if n < 3: return None
    a = s/(2*tan(pi/n))
    return n*s*a/2, a

def shoelace():
    try:
        x, y = list_from_ti("L1"), list_from_ti("L2")
        if len(x) != len(y): return None
        n = len(x)
        area = abs(sum(x[i]*y[(i+1)%n] - y[i]*x[(i+1)%n] for i in range(n)))/2
        perim = sum(sqrt((x[(i+1)%n]-x[i])**2 + (y[(i+1)%n]-y[i])**2) for i in range(n))
        return area, perim
    except: return None

def plane_dist(x, y, z, a, b, c, d):
    mag = sqrt(a*a + b*b + c*c)
    return 0 if mag == 0 else abs(a*x + b*y + c*z + d)/mag

while True:
    disp_clr()
    print("Math Tools:")
    print("1:Quadratic")
    print("2:Line Angles")
    print("3:Sphere")
    print("4:Cone")
    print("5:Arith Seq")
    print("6:Geom Seq")
    print("7:Polygon")
    print("8:Shoelace")
    print("9:Plane Dist")
    print("0:Quit")
    
    try:
        c = int(input("Choice:"))
        
        if c == 1:
            a = float(input("a:"))
            b = float(input("b:"))
            c = float(input("c:"))
            r = quad(a,b,c)
            if r:
                print("x1={:.4f}".format(r[0]))
                print("x2={:.4f}".format(r[1]))
            else:
                print("No real roots")
                
        elif c == 2:
            m1 = float(input("m1:"))
            m2 = float(input("m2:"))
            print("Angle={:.2f}°".format(ang_lines(m1,m2)))
            
        elif c == 3:
            r = float(input("r:"))
            v,a,c = sphere(r)
            print("V={:.4f}".format(v))
            print("A={:.4f}".format(a))
            print("C={:.4f}".format(c))
            
        elif c == 4:
            r = float(input("r:"))
            h = float(input("h:"))
            v,a,s = cone(r,h)
            print("V={:.4f}".format(v))
            print("A={:.4f}".format(a))
            print("s={:.4f}".format(s))
            
        elif c == 5:
            a1 = float(input("a1:"))
            d = float(input("d:"))
            n = int(input("n:"))
            s,an = seq_arith(a1,d,n)
            print("Sum={:.4f}".format(s))
            print("an={:.4f}".format(an))
            
        elif c == 6:
            a1 = float(input("a1:"))
            r = float(input("r:"))
            n = int(input("n:"))
            s,an = seq_geom(a1,r,n)
            print("Sum={:.4f}".format(s))
            print("an={:.4f}".format(an))
            
        elif c == 7:
            s = float(input("side:"))
            n = int(input("sides:"))
            r = polygon(s,n)
            if r:
                print("Area={:.4f}".format(r[0]))
                print("Apoth={:.4f}".format(r[1]))
            else:
                print("Invalid sides")
                
        elif c == 8:
            r = shoelace()
            if r:
                print("Area={:.4f}".format(r[0]))
                print("Perim={:.4f}".format(r[1]))
            else:
                print("Invalid lists")
                
        elif c == 9:
            print("Point (x,y,z):")
            x = float(input("x:"))
            y = float(input("y:"))
            z = float(input("z:"))
            print("Plane ax+by+cz+d=0:")
            a = float(input("a:"))
            b = float(input("b:"))
            c = float(input("c:"))
            d = float(input("d:"))
            dist = plane_dist(x,y,z,a,b,c,d)
            print("Dist={:.4f}".format(dist))
            
        elif c == 0:
            break
            
        else:
            print("Invalid choice")
            
    except:
        print("Invalid input")
    
    input("Press enter")