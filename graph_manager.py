import networkx as nx

def detect_deadlock(edges):
    G = nx.DiGraph()
    G.add_edges_from(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        return True, cycle  
    except nx.NetworkXNoCycle:
        return False, []  
