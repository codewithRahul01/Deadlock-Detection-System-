def add_dependency(edges, p1, p2):
  
    if not p1 or not p2:
        return False, "Both process names must be provided!"
    
    edges.append((p1, p2))
    return True, f"{p1} → {p2}"

def reset_dependencies():
    return []
