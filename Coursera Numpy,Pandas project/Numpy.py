#Exercise : In the following matrix replace negative element by 0 and replace odd elements with -2
import numpy as np
X = np.array([[2, 30, 20, -2, -4],
    [3 ,4 ,40 ,-3 ,-2],
    [-3 ,4, -6, 90, 10],
    [25 ,45 ,34 ,22 ,12],
    [13 ,24 ,22, 32, 37]])
X[X<0]=0 #if there's a numbers less than 0 then replace it with 0
X[X%2==1]=-2 #if there is an odd number than replace it with -2
print(X)