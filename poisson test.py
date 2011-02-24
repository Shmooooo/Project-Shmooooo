#Define three function to apply the poission(m,t,k) function.

from poissonq9 import poisson

def taxi():
    print """The probability of getting no taxi in half an hour if there is an average
of 5 taxis per hour is""", poisson(5,0.5,0)

def earthquakes():
    print """The probability of getting three earthquakes in the next 10 years if the mean is 10 over 50 years is""", poisson(10,0.2,3)

def misprints():
    print """The probability of reading 0 misprints in the first 6 pages if the average is 6 per page is equal to""", poisson(6,6,0)

misprints(), earthquakes(), taxi()
