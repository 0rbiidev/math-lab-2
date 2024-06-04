dx, dt = (20,50)
r = (0.875*dt) / (dx**2)

nLensamples = 100//dx - 1
nTimesamples = 600//dt + 1

s = ([0.0 for i in range(nLensamples+2)])

a = [0.0, 0.0] + [-r/2]*(nLensamples-1) + [0.0]
b = [0.0] + [1+r]*nLensamples + [0.0]
y = [0.0] + [-r/2]*(nLensamples-1) + [0.0, 0.0]

#1 - Decomposition

for i in range(2, nLensamples+1):
    a[i] = a[i] / b[i-1]
    b[i] = b[i] - a[i]*y[i-1]

x = [0.0] + [500.0]*nLensamples + [0.0] #boundary condition

print(x)

for t in range(1, nTimesamples):
    for i in range(1, nLensamples+1): 
        s[i] = (r/2)*x[i-1] + (1-r)*x[i] + (r/2)*x[i+1] # evaluate known values

    #2 - Fwd Sub
    for i in range(2, nLensamples+1):
        s[i] -= a[i]*s[i-1]

    #3 - Bwd Sub
    x[nLensamples] = s[nLensamples] / b[nLensamples]

    for i in range(nLensamples-1, 0, -1):
        x[i] = (s[i] - y[i]*x[i+1]) / b[i]

    print(x[1])
