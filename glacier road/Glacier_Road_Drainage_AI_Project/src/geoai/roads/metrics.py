import numpy as np

def topology_summary(pred_graph, ref_graph):
    p_nodes=len(pred_graph.nodes); r_nodes=len(ref_graph.nodes)
    p_edges=len(pred_graph.edges); r_edges=len(ref_graph.edges)
    return {'pred_nodes':p_nodes,'ref_nodes':r_nodes,'pred_edges':p_edges,'ref_edges':r_edges}
