import numpy as np



def Neville (w, xArray, fxArray, degree):
    n = len(xArray)
    neville = np.zeros( (n,n) )
    for i in range(n):
        neville[i,0] = fxArray[i]
    for i in range(1,n):
        for j in range(1, i+1):
            neville[i,j] = ((w - xArray[i-j])* neville[i,j-1] - (w- xArray[i]) * neville[i-1,j-1] )/ (xArray[i] - xArray[i-j])
    return neville[degree,n-1]

"""
for the HW assignment:
w = 3.7
degree = 2
xArray = (3.6,3.8,3.9)
fxArray = (1.675, 1.436,1.318)
"""


def newt_forward_table(x,y):
    n = len(x)
    differences = np.zeros((n, n))
    for i in range(n):
        differences[i][0] = y[i]
    
    for i in range(1,n):
        for j in range(1,i+1):

            left = differences[i][j-1]
            leftUpper = differences[i-1][j-1]
            denom = x[i]-x[i-j]
            differences[i][j] = (left-leftUpper)/denom


    return differences



def newton_interpolation(x, y, xi, degree, divided_diff):
    n = len(x)
    sum = divided_diff[0][0]
    temp = 1
    for i in range(1, degree+1):
        temp *= (xi - x[i - 1])
        product = temp * divided_diff[i][i]
        sum += (product)
     
    return sum



"""
for the HW assignment:
xArray = (7.2,7.4,7.5,7.6)
fxArray = (23.5492,25.3913,26.8224,27.4589)

"""


#2nd to last value is still INCORRECT!!!!
def hermite_divided_diff_table(x, y, dy):
    n = len(x)
    m = (2 * n)-1
    # Create a divided difference table
    differences = np.zeros((m+1, m))
    
    # Fill the divided difference table with function values
    for i in range(n):
        differences[2*i][0] = x[i]
        differences[2*i+1][0] = x[i]
        differences[2*i][1] = y[i]
        differences[2*i+1][1] = y[i]
    # Constructing the divided difference table
    #hardcode entry at 1,2 because it's hard to reach pythonically
    differences[1][2] = dy[0]
    for i in range(1, m+1):
        for j in range(2 ,i+2):
            if j > m-1:
                continue
            #the 'first' column gets the derivative values on odd rows
            if j == 2 and i % 2 == 1:
                differences[i][j] = dy[(i-1)//2]
            else:
            #all other columns are filled out with 'normal' divided difference
            #taking care not to grab bunk values with our i-j arithmetic
                if i % 2 == 1:
                    differences[i][j] = (differences[i][j-1] - differences[i-1][j-1]) / (x[i//2] - x[((i)-j)//2])
                else:
                    differences[i][j] = (differences[i][j-1] - differences[i-1][j-1]) / (x[i//2] - x[((i+1)-j)//2])


    
    return differences

def cubic_spline_interpolation(x, y):
    n = len(x)
    h = [x[i + 1] - x[i] for i in range(n - 1)]

    # Construct the tridiagonal matrix A
    A = np.zeros((n, n))
    A[0, 0] = 1
    A[n - 1, n - 1] = 1
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]

    # Construct the vector b
    b = np.zeros(n)
    for i in range(1, n - 1):
        b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

   
    x = thomas_algorithm(A, b)

    return A, b, x

def thomas_algorithm(A, b):
    n = len(b)
    c, d = [0] * n, [0] * n
    c[0] = A[0, 0] / A[0, 0]
    d[0] = b[0] / A[0, 0]

    for i in range(1, n):
        c[i] = A[i, i] - A[i, i - 1] * A[i - 1, i] / c[i - 1]
        d[i] = (b[i] - A[i, i - 1] * d[i - 1]) / c[i]

    x = np.zeros(n)
    x[n - 1] = d[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = d[i] - A[i, i + 1] * x[i + 1] / c[i]

    return x

