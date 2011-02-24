"""
2011W phys139
Assignment 11b
due: 2011-02-13

Evgeny Naumov
"""
def poissonPlot(u, t) :
    """--------------------------------------------------
    Function to plot the main part of the poisson distribution for a given intensity u and duration t.

    Function attemtps to correct inadmissible values of u and t and warns the user.

    The plot is saved to an output file.
    --------------------------------------------------"""

    # import required libraries

    from math import factorial, e  
    from matplotlib import use
    import matplotlib.pyplot as plt
    
    use( 'Agg' ) # use file output instead of a graphical window

    # define check variable for value correction attempt

    t_ = t
    u_ = u

    # attempt to correct invalid values of u and t, warn user
    
    t = abs(t)
    u = abs(u)

    if t != t_:
        print t_, "is not a nonnegative real number. Using t =", t, "instead."
    if u != u_:
        print u_, "is not a nonnegative real number. Using u =", u, "instead."

    # create list with probabilities for each number of successes possible                                   

    probs = [((u*t)**i)*(e**(-u*t))/factorial(i) for i in range(t)]

    # clear axes and figure, plot

    plt.cla()
    plt.clf()

    plt.plot(probs,'k.')
    plt.ylabel('Probability')
    plt.xlabel('Number of occurrences')
    plt.savefig("poissonplot.png", dpi=50) #!!

if __name__ == '__main__' :
    
    # constants
    t = 30    # length of experiment in time
    u = 1/6   # the 'success' rate per unit time

    ################
    # tell the user about this program
    print """
    This program plots the Poisson distribution, Po(x; u, t),
    for an experiment in which a die is rolled once per second for 30
    seconds (ie t=30) and 'success' is rolling a one (ie lambda=1/6).
    """

    # call the function 
    poissonPlot( u, t )
