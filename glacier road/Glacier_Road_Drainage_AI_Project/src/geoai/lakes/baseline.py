import numpy as np
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from geoai.preprocessing.spectral import ndwi, mndwi

def lake_baseline(green, nir, swir1, min_pixels=9):
    idx = mndwi(green, swir1)
    valid = np.isfinite(idx)
    threshold = threshold_otsu(idx[valid]) if valid.any() else 0.0
    mask = (idx > threshold) & valid & (nir < np.nanpercentile(nir[valid], 80))
    lab = label(mask, connectivity=2)
    cleaned = np.zeros_like(mask, dtype=bool)
    for r in regionprops(lab):
        if r.area >= min_pixels:
            cleaned[lab == r.label] = True
    return cleaned, idx, float(threshold)
