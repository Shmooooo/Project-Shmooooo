#Program to read three values from the command line and output a possion probability.

#import sys
#m0 = float(sys.argv[1])       # first input: mean per unit time
#t0 = float(sys.argv[2])       # second input: interval in unit times
#k0 = float(sys.argv[3])       # number of occurrences sought


def poisson(m,t,k):
    """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Function to calculate the poission probability of an occurence with parameters given in the command line.
    Called by reference to its name.

    First input is the mean per unit sample size (be it time, volume, etc.);
    Second input is the total sample size in unit sample sizes;
    Third input is the number of occurences sought.

    Restrictions: total sample size and mean must be greater than 0; sought occurences must be a nonnegative integer.
    (the poission distributions models discrete independent events).

    Some exmaples of a call to this script from a Linux shell:

        ~$ python -i /home/evgeny/Programming/poisson-q9.py 7 1 4
        0.0912261916373

        ~$ python -i /home/evgeny/Programming/poisson-q9.py -7 1 4
        Mean cannot be less than 0. Supplied: -7.0
        None

        ~$ python -i /home/evgeny/Programming/poisson-q9.py 7 1 4.5
        Given: k = 4.5 : not a nonnegative integer. Using k = 4 instead.
        0.0912261916373

    Alternatively the function poission can be imported.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

    from math import factorial, exp
    
    if m < 0:
        print "Mean cannot be less than 0. Supplied:", m
        return None
    if t < 0:
        print "Number of occurrences cannot be less than 0. Supplied:", k
        return None

    k_ = k
    k = int(abs(k))

    p = ((m*t)**k)*exp(-m*t)/factorial(k)



    if k_ != k:
        print "Given: k =", k_, ": not a nonnegative integer. Using k =", k, "instead."

    return p


