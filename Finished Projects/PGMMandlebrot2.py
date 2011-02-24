from numpy import linspace
#-------------------------
plot = open("/home/evgeny/plot.pgm","w")

h = int(raw_input("Plot height:"))
w = int(raw_input("Plot width:"))

rl = float(raw_input("Lower real line bound:"))
ru = float(raw_input("Upper real line bound:"))
il = float(raw_input("Lower imaginary line bound:"))
iu = float(raw_input("Upper imaginary line bound:"))

detail = int(raw_input("Precision:"))
#-------------------------
def mandlebrotIterator(c):

    z = 0
    i = 0

    while i < detail:
        z = z**2 + c
        if abs(z) >= 2:
            return 0
        i += 1
    return 1
#-------------------------
header = ["P2","\n",str(w)," ",str(h),"\n",str(1),"\n"]

for k in header:

    plot.write(k)
#-------------------------
for y in linspace(il,iu,num=h):
    for x in linspace(rl,ru,num=w):
        plot.write(str(mandlebrotIterator(complex(x,y))))
        plot.write(" ")
    plot.write("\n")

plot.close()
#-------------------------


