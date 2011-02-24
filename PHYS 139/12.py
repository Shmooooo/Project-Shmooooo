"""
-----------------------------------------------------------------
2011W phys139
bestfit.py
2011-02-08

Evgeny Naumov
"""
def bestFit(x, y):
    """
    Function to calculate the simple least squares best fit given lists
    of corresponding coordinates.

    If lists are of different lengths truncates the longest list, notifies user.

    Outputs a, b where y = ax + b is the line of best fit.

    Uses Covar(x,y)/Var(x) to find a, y_av - a*x_av to find b, where
    x_av and y_av are the average x and y values of the given data respectively.

        >>> print bestFit([1,2,3,4,5],[1.1,1.3,1.2,1.4,1.3])
        (0.049999999999999822, 1.1100000000000005)

    In that case the line of best fit would be approximately y = 0.050x + 1.11.

    If later plotting the data, note that list truncation is local and
    you might still run into errors if otherwise using lists of unequal length.
    """
    # check given lists both the same length; else truncate; notify
    
    if len(x) != len(y):
        y = y[:min(len(x),len(y))]
        x = x[:min(len(x),len(y))]
        print x, y
        print "Given lists not the same length! Truncating."

    # averages
    x_av = float(sum(x))/len(x)
    y_av = float(sum(y))/len(y)
    
    xx_av = 0
    for i in x:
        xx_av += i*i
    xx_av = xx_av/float(len(x))

    xy_av = 0
    for i in range(len(x)):
        xy_av += x[i]*y[i]
    xy_av = xy_av/len(x)

    # variance and covariance
    x_var = xx_av - (x_av)**2
    xy_cvar = xy_av - x_av*y_av

    # for y = ax + b
    a = xy_cvar/x_var
    b = y_av - a*x_av
    
    return a, b




# running as `main` -- call the bestFit() function and show the result

if __name__ == '__main__' :
    
    # sample data
    x1 = [ 1.1, 2, 3, 4, 5]
    y1 = [ 1.1, 2.3, 2.9, 4.7, 4.4]
    a, b = bestFit( x1, y1 )
    print """
      The best fit to data set 1 is:\n
        a = %7.3g
        b = %7.3g.

      Plotting output and saving to bestfit.png.
    """ % ( a, b )
    # import required libraries, attempt to placate gnh

    from matplotlib import use
    import matplotlib.pyplot as plt

    use( 'Agg' ) # use file output instead of a graphical window

    # clear axis and any existing figure
    plt.cla()
    plt.clf()

    plt.ylabel("y")
    plt.xlabel("x")
    plt.title("Best fit")

    # range + 2 to make the graph more presentable and attempt to prevent clipping
    plt.plot(x1,y1,"k.")
    plt.plot(range(int(max(x1)) + 2),[a*i + b for i in range(int(max(x1)) + 2)])

    plt.savefig("bestfit.png", dpi=100)
    
   
