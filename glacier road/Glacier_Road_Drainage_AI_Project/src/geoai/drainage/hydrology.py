import numpy as np
from scipy.ndimage import gaussian_filter

def terrain_derivatives(dem, pixel_size=30):
    smooth=gaussian_filter(dem.astype(float), sigma=1)
    gy,gx=np.gradient(smooth, pixel_size, pixel_size)
    slope=np.degrees(np.arctan(np.hypot(gx,gy)))
    return slope

def relative_low_lying_index(dem):
    dem=np.asarray(dem,float)
    return np.nanpercentile(dem, 25) - dem
