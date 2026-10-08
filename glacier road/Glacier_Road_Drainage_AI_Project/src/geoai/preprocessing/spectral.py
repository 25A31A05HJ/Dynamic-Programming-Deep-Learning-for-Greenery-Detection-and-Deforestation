import numpy as np

def normalized_difference(a, b):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    return np.divide(a-b, a+b, out=np.zeros_like(a), where=(a+b)!=0)

def ndwi(green, nir):
    return normalized_difference(green, nir)

def mndwi(green, swir1):
    return normalized_difference(green, swir1)
