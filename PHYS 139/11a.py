"""
2011W phys139
Assignment 11a
due: 2011-02-13

Evgeny Naumov
"""
def comparePlot(n, p) :
    """--------------------------------------------------
    Function to plot the entire binomial distribution for a given number of trials, n,
    and the probability of success, p.

    Function stops with an illegal value of p and attemtps to correct inadmissible values
    of n.
    --------------------------------------------------"""

    # import required libraries

    from math import factorial  
    from matplotlib import use
    import matplotlib.pyplot as plt
    
    use( 'Agg' ) # use file output instead of a graphical window

    # define check variable for value correction attempt

    n_ = n                         

    # invalid probability stops function and warns user 
    
    if p > 1 or p < 0: 
        print "Invalid probability. p must be less than or equal to 1 and greater than or equal to 0. Supplied:", p  
        return None

    # attempt to correct invalid values of n, warn user
    
    n = int(abs(n))

    if n != n_:
        print n_, "is not a nonnegative integer. Using n =", n, "instead."

    # create list with probabilities for each number of successes possible                                   

    probs_bi = [factorial(n)*(p**i)*((1-p)**(n-i))/(factorial(i)*factorial(n-i)) for i in range(n+1)]
    probs_po = [((p*n)**i)*(e**(-p*n))/factorial(i) for i in range(n+1)]
    # clear axes and figure, plot

    plt.cla()
    plt.clf()

    plt.plot(probs_bi,'k.')
    plt.plot(probs_po,'g.')
    
    plt.ylabel('Probability')
    plt.xlabel('Number of successes or occurrences')
    plt.savefig("binomialplot.png", dpi=50) #!!

if __name__ == '__main__' :
    
    # constants
    n = 30.5 # the number of experiments
    p = 1/6. # the probability of 'success'

    print """
    This program plots the binomial distribution, B( k; n, p ), for an
    experiment in which a die is rolled 30 times (ie n=30) and 'success' is
    rolling a one (ie p=1/6).
    """

    # call the function 
    binomialPlot( n, p )
