import numpy as np

def binary_change(old_mask, new_mask):
    old=np.asarray(old_mask).astype(bool); new=np.asarray(new_mask).astype(bool)
    return (new.astype(np.int8)-old.astype(np.int8))
