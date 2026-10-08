import numpy as np
from scipy.stats import kendalltau, theilslopes

def mann_kendall_sen(years, values):
    years=np.asarray(years); values=np.asarray(values,float)
    ok=np.isfinite(values); x=years[ok]; y=values[ok]
    if len(y)<3: return {'n':int(len(y)),'tau':np.nan,'p_value':np.nan,'sen_slope':np.nan}
    tau,p=kendalltau(x,y); slope=theilslopes(y,x).slope
    return {'n':int(len(y)),'tau':float(tau),'p_value':float(p),'sen_slope':float(slope)}
