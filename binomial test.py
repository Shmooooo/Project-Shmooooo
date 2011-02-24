#Several functions to apply the binomial distribution

from Binomial import binomial

def coin2():
    print """The probability of getting exactly two heads after flipping a fair
coin 5 times is""", binomial(5,2,0.5)

def coin4():
    print """The probability of getting four ones in a row when rolling a fair die
four times in a row is""", binomial(4,4,1./6)

def skier():
    print """The probability of breaking a ski at least once across five
ompetitions is""", 1 - binomial(5,5,119./120)

#For the last function it is more expdient to calculate the probability of the complementary
#event, then subtract that value from 1.    
