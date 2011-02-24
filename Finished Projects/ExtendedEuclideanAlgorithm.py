def eea(a,b,e=0,v=0):

    D, d = int(max(a,b)),int(min(a,b))
    D_,d_ = D,d

    q = D/d
    
    if v==True:
        print "Finding gcd(%d,%d)..."%(D,d)
        if e==True:
            print "Finding x, y such that gcd(%d,%d) = %dx + %dy..."%(D,d,D,d)

        if D-q*d==0:
            print d, "divides", D, "\ngcd(a,b) =", d, "(",D, "=", q,"*",d,")"
            return d

    if e==True:
        xl,yl =[1,0],[0,1]
        if v==True:
            print "                       x, y =", xl[0],yl[0]

    while D-q*d != 0:
        if D-q*d >=0:
            if v==True and not e==True:
                print D,"=",q,"*",d,"+",D-q*d,"."
        
            if e==True:
                tl = [xl[0],yl[0]]
                xl[0],yl[0] = xl[1],yl[1]
                xl[1],yl[1] = -q*xl[0]+tl[0],-q*yl[0]+tl[1]

                if v==True:
                    print D,"=",q,"*",d,"+",D-q*d,", x, y =", xl[1],yl[1]

            D,d = d,D-q*d
            q = D/d

        else: #D - q*d < 0

            q = q+1

            if v==True and not e==True:
                print D,"=",q,"*",d,"+",D-q*d,"."
        
            if e==True:
                tl = [xl[0],yl[0]]
                xl[0],yl[0] = xl[1],yl[1]
                xl[1],yl[1] = -q*xl[0]+tl[0],-q*yl[0]+tl[1]

                if v==True:
                    print D,"=",q,"*",d,"+",D-q*d,", x, y =", xl[1],yl[1]

            D,d = d,D-q*d
            q = D/d

    
    if v==True:
        print "By the Extended Euclidean Algorithm, gcd(%d,%d) = %d"%(D_,d_,d)

        if e==True:
            print "gcd(%d,%d) can be written as %d*%d + %d*%d"%(D_,d_,xl[1],D_,yl[1],d_)
    if e==True:
        return [d,xl[1],yl[1]]
    return d 
print eea(2244,46134,e=1,v=1)
