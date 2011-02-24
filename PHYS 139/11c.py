"""
2011W phys139
Assignment 11a
due: 2011-02-13

Evgeny Naumov
"""
def comparePlot(n, p) :
    """--------------------------------------------------
    Funtion to plot the binomial and poisson distributions for a given probability (intensity)
    and number of trials (duration) on the same set of axes.

    Gives user detailed comparison of the two distributions and explains their mathematical
    differences.

    Saves plot output to file.
    --------------------------------------------------"""

    # import required libraries

    from math import factorial, e  
    from matplotlib import use
    import matplotlib.pyplot as plt
    
    use( 'Agg' ) # use file output instead of a graphical window

    # invalid probability stops function and warns user 
    
    if p > 1 or p < 0: 
        print "Invalid probability. p must be less than or equal to 1 and greater than or equal to 0. Supplied:", p  
        return None

    # attempt to correct invalid values of n, warn user
    
    n = int(abs(n))

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
    plt.savefig("compareplot.png", dpi=50) #!!

    # sum the probabilities in each distribution:

    print "Summing the binomial probabilities:", sum(probs_bi)
    print "Summing the poission probabilities:", sum(probs_po),"\n"

    print """As you can see the cumulative probability in both appears to be 1.
However, this is a limitation of the program. Summing the probabilities
to 20 trials/occurences will be more illustrative.\n"""

    print "Summing the binomial probabilities to 20 events:", sum(probs_bi[:21])
    print "Summing the poission probabilities to 20 occurences:", sum(probs_po[:21]),"\n"

    print """As you can see, the binomial probabilities approach one much quicker
than the poisson probabilities. Indeed, at 30 success/occurences the
cumulative probability of the binomial distribution is indeed exactly 1, while
it is just a bit less for the poisson distribution.

This might seem physically impossible given that if a die is rolled once per second for 30
seconds one can at most get 30 6s; however, one should note that the die-rolling process is
not well-modelled by the poisson distribution. Namely the assumption of homogeneity - one of
the three central assumptions of a Poisson process, where the average number of occurrences
is proportional to the sample duration, does not hold. The average number of 6's in 1.99
seconds is not almost doulbe that for one second in the given experiment.

Concerning the plots themselves, the distributions appear quite similar. The binomial
distribution appears to be more centralized, with a sharper peak; the poisson distribution
has a "thicker" tail, which fits in with the discussion above."""

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
    comparePlot( n, p )
