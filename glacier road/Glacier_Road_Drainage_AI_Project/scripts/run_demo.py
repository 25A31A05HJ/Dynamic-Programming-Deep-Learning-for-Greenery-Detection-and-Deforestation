import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','src'))
import numpy as np
from geoai.lakes.baseline import lake_baseline
from geoai.lakes.metrics import binary_metrics
from geoai.change.trends import mann_kendall_sen
np.random.seed(42)
H,W=256,256
# synthetic smoke-test scene, not research data
x,y=np.meshgrid(np.arange(W),np.arange(H)); lake=((x-130)**2+(y-125)**2)<35**2
nir=np.where(lake,.08,.32)+np.random.normal(0,.01,(H,W)); green=np.where(lake,.12,.25)+np.random.normal(0,.01,(H,W)); swir=np.where(lake,.05,.28)+np.random.normal(0,.01,(H,W))
pred,idx,t=lake_baseline(green,nir,swir)
print('Demo MNDWI threshold:',round(t,4)); print('Demo metrics:',binary_metrics(pred,lake))
print('Demo trend:',mann_kendall_sen(np.arange(2016,2025),np.array([100,102,104,107,111,115,118,121,125])))
