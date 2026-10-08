import numpy as np
from skimage.morphology import skeletonize, remove_small_objects
import networkx as nx

def clean_and_skeletonize(mask, min_pixels=8):
    mask=remove_small_objects(mask.astype(bool), min_size=min_pixels)
    return skeletonize(mask)

def skeleton_to_graph(skel):
    G=nx.Graph()
    rows, cols=np.where(skel)
    for r,c in zip(rows,cols):
        G.add_node((int(r),int(c)))
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if dr==dc==0: continue
                q=(int(r+dr),int(c+dc))
                if q in G:
                    G.add_edge((int(r),int(c)),q,weight=float((dr*dr+dc*dc)**0.5))
    return G
