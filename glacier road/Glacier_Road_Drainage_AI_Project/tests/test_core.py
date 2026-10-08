import sys
sys.path.insert(0,'src')
import numpy as np
from geoai.preprocessing.spectral import ndwi,mndwi
from geoai.lakes.metrics import binary_metrics
from geoai.change.post_classification import binary_change

def test_indices_finite():
    a=np.array([[.2,.3]]); b=np.array([[.1,.3]])
    assert np.isfinite(ndwi(a,b)).all(); assert np.isfinite(mndwi(a,b)).all()

def test_metrics_perfect():
    x=np.array([[1,0],[0,1]])
    m=binary_metrics(x,x); assert m['iou']==1 and m['f1']==1

def test_change():
    old=np.array([[1,0]]); new=np.array([[0,1]])
    assert np.array_equal(binary_change(old,new),np.array([[-1,1]]))
