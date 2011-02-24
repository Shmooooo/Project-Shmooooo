from math import sqrt

xli = [1,2,3,4,5,6,7,8]
yli = [0.7,2.1,3.1,3.9,5.7,5.9,6.4,8.1]

def lsr(xli,yli,iterations):
    """
    """
    
    mid_x, mid_y = len(xli)/2, len(yli)/2
    slope_guess = float(yli[mid_y])/xli[mid_x]
    intercept_guess = yli[0]-xli[0]
    line_guess = []
    
    
    for x in xli:
        line_guess.append([x,slope_guess*x + intercept_guess])

    print line_guess

    while iterations >= 0:

        m1 = 0 #~#
        for i,[x, y] in enumerate(line_guess):
            m1 += y - yli[i]

        print m1

        m2 = 0 #~#
        for i,[x, y] in enumerate(line_guess):
            m2 += sqrt((y - yli[i])**2)
      
        print m2
        
        tilt = 0 #~#
        for i,[x, y] in enumerate(line_guess):
            tilt += (y - yli[i])*(xli[i]-xli[mid_x])

        print tilt

        iterations -=1
lsr(xli,yli,0)
