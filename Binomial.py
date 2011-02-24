def binomial(n,k,p,v=False):
    """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Function to calculate the probability of k successes in n independent repeated trials, with a trial success probability of p:

        >>> binomial(2,1,0.5)
        0.5

    If function is run as the main program, it asks the user to imput the values of n, k, and p. If it is imported it will
    bypass the prompt and use the values supplied.
    
    Function stops and warns user if given probability is illegal (less than 0 or greater than 1).
    The error messages for this function are designed to impress upon the user the gravity of his transgression:

        >>> binomial (2,1,1.5)
        Invalid probability. p must be less than or equal to 1 and greater than or equal to 0. Supplied: 1.5
        Deleting system32...
        Please wait...
        ...
        Success!

    Function attempts to correct values of n and k supplied to be valid arguments for factorial(). Namely takes the absolute value
    of negative arguments and the floor of noninteger arguments, in that order. The function notifies the user of the corrections:

        >>> binomial(2.3,-1.9,0.5)  
        2.3 is not a nonnegative integer. Using 2 instead.
        -1.9 is not a nonnegative integer. Using 1 instead.
        0.5

    If at this point value of k is greater than the value of n, something which is mathematically undefined
    (cannot have more successes than trials), the functions stops and notifies the user:

        >>> binomial(5,6,0.5)
        k must be less than n. Supplied, k = 6 n = 5
        Attempting sudo rm -r /
        ...
        Success!

    An additional extra feature of the function is the v kwarg (flag). The flag is set to False by default; when set to True
    the function gives a verbose statement regarding its output irrespective of whether it is the main program or not.
    It still returns the probability for the purposes of further computation.

        binomial(2,1,0.5,v=True) 
        The probability of 1 successes in 2 independent repeated trials with a trial probability of success equal to 0.5 is
        0.5 

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    from math import factorial

# clause to determine if input is required
    
    if __name__ == '__main__':

        n = int(raw_input('Number of trials:'))  #convert input to appropriate type
        k = int(raw_input('Number of successes:'))
        p = float(raw_input('Trial probability of success:'))
        
# define check variables to be used later to warn of correction attempts by the funciton

    n_ = n                         
    k_ = k  

# invalid probability stops function and warns user 
    
    if p > 1 or p < 0: 
        print "Invalid probability. p must be less than or equal to 1 and greater than or equal to 0. Supplied:", p  
        return "Deleting system32...\nPlease wait...\n...\nSuccess!"

# attempt to correct invalid values of n, k
    
    n = int(abs(n))                                    
    k = int(abs(k))

# stops function if k is greater than n, warns user
    
    if k > n:
        print "k must be less than n. Supplied, k =", k, "n =", n
        return "Attempting sudo rm -r /\n...\nSuccess!"

    r = factorial(n)*(p**k)*((1-p)**(n-k))/(factorial(k)*factorial(n-k))

# notifies user of corrections

    if n != n_:
        print n_, "is not a nonnegative integer. Using n =", n, "instead."
    if k != k_:
        print k_, "is not a nonnegative integer. Using k =", k, "instead."   

# checks verbose flag and gives a detailed printout if it is set or if the function is the main program
    if v==True or __name__=='__main__':
        print "The probability of %g successes in %g independent repeated trials with a trial probability of success equal to %g is"%(k,n,p)
        return r
    return r
    
print binomial(3,3,0.5)  
        
import doctest
doctest.testfile()
