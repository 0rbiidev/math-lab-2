dx, dt = (20, 100)
pointsX, pointsT = (100//dx, 600//dt)
grid = ([[0.0 for i in range(pointsX+1)] for j in range(pointsT+1)])
grid[0] = [0.0] + [500]*(pointsX-1) + [0.0]

r = (0.875 * dt) / (dx**2)
print(r)

for t in range(1, pointsT+1):
    for s in range(1, pointsX):
        grid[t][s] = r*grid[t-1][s+1] + (1 - 2*r)*grid[t-1][s] + r*grid[t-1][s-1]

for x in grid: 
    print(x)