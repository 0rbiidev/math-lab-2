import math

for t in (n1 for n1 in range(0,601) if n1%100 == 0):
    wire = []
    wire.append(0)
    for x in (n2 for n2 in range(1,100) if n2%20 == 0):
        T = 0.0
        for n in (n3 for n3 in range(1, 5000) if n3%2 == 1):
            T += (1/n) * math.sin((n*math.pi*x)/100) * math.exp((-((n**2 * math.pi**2 * 0.875)) * t) / 100**2)
        T = T*(2000/math.pi)
        wire.append(T)
    wire.append(0)
    print(wire)
