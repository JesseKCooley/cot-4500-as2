from ..main import assignment_2
import math
import numpy as np

w = 3.7
degree = 2
xArray = [3.6,3.8,3.9]
fxArray = [1.675, 1.436,1.318]
answer1 = assignment_2.Neville(w,xArray,fxArray,degree)
print(answer1 )
print('\n')


x = [7.2, 7.4, 7.5, 7.6]
y = [23.5492, 25.3913, 26.8224, 27.4589]

diffs = assignment_2.newt_forward_table(x,y)
#degree 1 seems to give the closest approximation?
result = assignment_2.newton_interpolation(x,y,7.3,3,diffs)
#iterate the matrix diagonal to print polynomials?
for i in range(1,4):

    print(diffs[i][i])


print('\n')
print(result)
print('\n')



#hx = [3.6e0,3.8e0,3.9e0]
#hy = [1.675e0,1.436e0,1.318e0]
#hprime = [-1.195e0,-1.188e0,-1.182e0]

hx = [2.1,2.5,2.6]
hy = [5.456, 6.298, 6.427]
hprime = [.862, 1.489, 1.743]

htable = assignment_2.hermite_divided_diff_table(hx,hy,hprime)

original_print_options = np.get_printoptions()
np.set_printoptions(formatter={'float': '{:0.3e}'.format})

for row in htable:
    print(row)

print('\n')
np.set_printoptions(**original_print_options)

xArray = [2,5,8,10]
fxArray = [3,5,7,9]
A,b,x = assignment_2.cubic_spline_interpolation(xArray,fxArray)
print(A)
print(b)
print(x)