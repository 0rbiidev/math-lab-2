dx, dt = (5,10)
r = (0.875*dt) / (dx**2)

g = 0.1
c = 400

nLensamples = 100//dx - 1
nTimesamples = 60//dt + 1

s = ([0.0 for i in range(nLensamples+2)])

a = [0.0, 0.0] + [-r/2]*(nLensamples-1) + [0.0]
b = [0.0] + [1+r]*nLensamples + [0.0]
y = [0.0] + [-r/2]*(nLensamples-1) + [0.0, 0.0]

#1 - Decomposition

for i in range(2, nLensamples+1):
    a[i] = a[i] / b[i-1]
    b[i] = b[i] - a[i]*y[i-1]

time = 0

X = []
X.append(([0.0 for i in range(nLensamples+2)]))

for i in range(1,nLensamples+1):
    X[0][i] = (-i * g * (i - 100)) + c

print(X[0][4])

for t in range(1, nTimesamples):
    X.append(([0.0 for i in range(nLensamples+2)]))
    time+=dt
    for i in range(1, nLensamples+1): 
        s[i] = (r/2)*X[t-1][i-1] + (1-r)*X[t-1][i] + (r/2)*X[t-1][i+1] # evaluate known values

    #2 - Fwd Sub
    for i in range(2, nLensamples+1):
        s[i] -= a[i]*s[i-1]

    #3 - Bwd Sub
    X[t][nLensamples] = s[nLensamples] / b[nLensamples]

    for i in range(nLensamples-1, 0, -1):
        X[t][i] = (s[i] - y[i]*X[t][i+1]) / b[i]
    
    print(X[t][4])

    

for x in range(0, nLensamples+2):
    print(x*dx, str([X[j][x] for j in range(0,nTimesamples)]).strip("[]"))
