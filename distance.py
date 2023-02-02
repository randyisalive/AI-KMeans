import math

def mathDistance(tuple2,tuple):
    z,m = tuple
    x,y = tuple2
    X = (x-z)
    X = math.pow(X,2)
    Y = (y-m)
    Y = math.pow(Y,2)
    Z = X + Y
    result = math.sqrt(Z)
    return result

