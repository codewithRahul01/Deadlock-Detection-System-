import networkx as nx
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class ResourceAllocationGraph:
    def __init__(self, root):
        self.graph = nx.DiGraph()
        self.allocations = {}
        
        root.title("Resource Allocation Graph Simulator")
        root.geometry("400x300")
        
        self.process_label = tk.Label(root, text="Process:")
        self.process_label.grid(row=0, column=0)
        self.process_entry = tk.Entry(root)
        self.process_entry.grid(row=0, column=1)
        
        self.resource_label = tk.Label(root, text="Resource:")
        self.resource_label.grid(row=1, column=0)
        self.resource_entry = tk.Entry(root)
        self.resource_entry.grid(row=1, column=1)
        
        self.add_button = tk.Button(root, text="Allocate Resource", command=self.add_edge)
        self.add_button.grid(row=2, column=0, columnspan=2)
        
        self.check_deadlock_button = tk.Button(root, text="Check Deadlock", command=self.check_deadlock)
        self.check_deadlock_button.grid(row=3, column=0, columnspan=2)
        
        self.visualize_button = tk.Button(root, text="Visualize Graph", command=self.visualize_graph)
        self.visualize_button.grid(row=4, column=0, columnspan=2)
    
    def add_edge(self):
        process = self.process_entry.get().strip()
        resource = self.resource_entry.get().strip()
        
        if process and resource:
            self.graph.add_edge(process, resource)
            self.allocations[process] = resource
            messagebox.showinfo("Success", f"Edge added: {process} -> {resource}")
        else:
            messagebox.showwarning("Input Error", "Please enter both Process and Resource names.")
    
    def check_deadlock(self):
        try:
            cycle = nx.find_cycle(self.graph, orientation='original')
            messagebox.showerror("Deadlock Detected", f"Cycle Found: {cycle}")
        except nx.NetworkXNoCycle:
            messagebox.showinfo("No Deadlock", "No deadlock detected.")
    
    def visualize_graph(self):
        if not self.graph.nodes:
            messagebox.showwarning("No Data", "No nodes in the graph to visualize.")
            return
        
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_color="black", arrowsize=20)
        plt.title("Resource Allocation Graph")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ResourceAllocationGraph(root)
    root.mainloop()
