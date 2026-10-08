import numpy as np

def binary_metrics(pred, ref):
    pred=np.asarray(pred).astype(bool); ref=np.asarray(ref).astype(bool)
    tp=np.logical_and(pred,ref).sum(); fp=np.logical_and(pred,~ref).sum(); fn=np.logical_and(~pred,ref).sum()
    iou=tp/(tp+fp+fn) if tp+fp+fn else 1.0
    precision=tp/(tp+fp) if tp+fp else 0.0
    recall=tp/(tp+fn) if tp+fn else 0.0
    f1=2*precision*recall/(precision+recall) if precision+recall else 0.0
    return {'iou':float(iou),'precision':float(precision),'recall':float(recall),'f1':float(f1)}
