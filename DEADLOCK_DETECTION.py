import networkx as nx
import tkinter as tk
from tkinter import messagebox

def detect_deadlock(edges):
  
    G = nx.DiGraph()
    G.add_edges_from(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        return True, cycle  # Deadlock detected
    except nx.NetworkXNoCycle:
        return False, []  # No deadlock

def add_dependency():
    
    p1 = entry_p1.get().strip()
    p2 = entry_p2.get().strip()
    
    if not p1 or not p2:
        messagebox.showerror("❌ Error", "Both process names must be provided!")
        return
    
    edges.append((p1, p2))
    listbox.insert(tk.END, f"{p1} → {p2}")
    entry_p1.delete(0, tk.END)
    entry_p2.delete(0, tk.END)

def check_deadlock():
    
    if not edges:
        messagebox.showwarning("⚠️ Warning", "No dependencies entered!")
        return
    
    is_deadlocked, cycle = detect_deadlock(edges)
    if is_deadlocked:
        messagebox.showerror("🚨 Deadlock Detected", f"Cycle found: {cycle}")
    else:
        messagebox.showinfo("✅ No Deadlock", "No deadlock detected!")

def reset():
    
    global edges
    edges = []
    listbox.delete(0, tk.END)


root = tk.Tk()
root.title("AI Deadlock Detection System")
root.geometry("400x400")

tk.Label(root, text="Enter Process Dependencies", font=("Arial", 12)).pack()
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Process 1:").grid(row=0, column=0)
entry_p1 = tk.Entry(frame)
entry_p1.grid(row=0, column=1)

tk.Label(frame, text="Process 2:").grid(row=1, column=0)
entry_p2 = tk.Entry(frame)
entry_p2.grid(row=1, column=1)

tk.Button(root, text="➕ Add Dependency", command=add_dependency).pack()
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack()

tk.Button(root, text="🔍 Check Deadlock", command=check_deadlock).pack()
tk.Button(root, text="🔄 Reset", command=reset).pack()

edges = [] 

root.mainloop()
