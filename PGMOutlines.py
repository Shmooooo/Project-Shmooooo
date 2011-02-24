image = open("/home/evgeny/cat.pgm","r")

dataz = image.read()

w = int(dataz.split()[1])
h = int(dataz.split()[2])

values = dataz.split()[3:]

image.close()

b = [int(values[i])//128 for i in range(w*h)]
c = b

for i in range(w*h):
    try:
        s = b[i-w-1] + b[i-w] + b[i-w+1] + b[i-1] + b[i+1] + b[i+w-1] + b[i+w] + b[i+w+1]
        if i <=1000:
            print s, i, b[i-w-1] , b[i-w] , b[i-w+1] , b[i-1] , b[i+1] , b[i+w-1] , b[i+w] , b[i+w+1]
        
    except:
        continue

    if s == 8:
        c[i] = 0
        
out = open("/home/evgeny/catol.pgm","w")
out.write("P2")
out.write("\n")
out.write(str(w))
out.write(" ")
out.write(str(h))
out.write("\n")
out.write("1")
out.write("\n")
for i in range(w*h):
    out.write(str(c[i]))
    out.write(" ")
    if i%w == 0 and i != 0:
        out.write("\n")







