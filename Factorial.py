def factorial(n):
    """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Function to calculate the factorial of a number (n!):

        >>>factorial(5)
        120

    Obeys 0! = 1 definition:

        >>>factorial(0)
        1

    When presented with negative or noninegral arguments, the function attempts to correct them.
    The absolute value of negative and the floor of nonintegral arguments is taken, in that order.
    The function notifies the user of any corrections thus undertaken:
    
        >>>factorial(5.99)
        5.99 is not a nonnegative integer! Using 5 instead.
        120

        >>>factorial(-9.99)
        -9.99 is not a nonnegative integer! Using 9 instead.
        362880

    The function likewise acts on the modulus of complex arguments:

        >>>factorial(3+4j)
        (3+4j) is not a nonnegative integer! Using 5 instead.
        120

    The function returns an error when given an argument invalid as an argument for the abs() function,
    since its corrective faculties hinge thereon.
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    n_ = n                                                   #"check" variable used later to possibly warn of argument modification
    n = int(abs(n))                                          # correct argument to nonnegative integer if possible
    f = 1
    for k in range(n):
        f *= k + 1
    if n_ != n:
        print n_, "is not a nonnegative integer! Using", n, "instead."
    return f


    
