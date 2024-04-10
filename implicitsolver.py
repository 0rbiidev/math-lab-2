dx, dt = (20,100)
grid = ([[0.0 for i in range(100//dx + 1)] for j in range(600//dt + 1)])
grid[0] = [0.0] + [500]*(100//dx - 1) + [0.0]
r = (0.875 * dt) / (2 * dx**2)
b = [0.0 for i in range (100//dx)]
A = ([[0.0 for i in range(100//dx)] for j in range(100//dx)])

x = 1

for j in (n1 for n1 in range(1, 600) if n1%dt == 0):
    y = 1
    A[0][0] = 1+r
    A[0][1] = -(r/2)
    b[0] = 0

    for i in (n2 for n2 in range(1, 100) if n2%dx == 0):
        A[y][y-1] = -r/2
        A[y][y] = 1+r
        A[y][y+1] = -r/2

        b[y] = (r/2)*grid[x][y-1] + (1-r)*grid[x][y] + (r/2)*grid[x][y+1]

        y++

    # Thomas algorithm for trilinear matrix

    for i in range(1,len(A)): #decompose
        A[i][i-1] /= A[i-1][i-1]
        A[i][i] -= A[i][i-1] * A[i][i+1] 

    for i in range(1,len(A)): #fwd sub
        b[i] -= A[i][i] * b[i-1]
    
    # bwd sub
    

    x++