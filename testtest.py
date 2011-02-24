testblock = [1 for i in range(10000)]
for i in range(1000):
    testblock[i] = 0

w = 100
h = 100

b = [int(testblock[i])//128 for i in range(w*h)]
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

for i in c:
    print c[i]
