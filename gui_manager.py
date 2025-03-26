import tkinter as tk
from tkinter import messagebox
from graph_manager import detect_deadlock
from dependency_manager import add_dependency, reset_dependencies


edges = []

def add_dependency_ui():
   
    global edges
    p1 = entry_p1.get().strip()
    p2 = entry_p2.get().strip()
    
    success, message = add_dependency(edges, p1, p2)
    if success:
        listbox.insert(tk.END, message)
        entry_p1.delete(0, tk.END)
        entry_p2.delete(0, tk.END)
    else:
        messagebox.showerror("❌ Error", message)

def check_deadlock_ui():
   
    global edges
    if not edges:
        messagebox.showwarning("⚠️ Warning", "No dependencies entered!")
        return
    
    is_deadlocked, cycle = detect_deadlock(edges)
    if is_deadlocked:
        messagebox.showerror("🚨 Deadlock Detected", f"Cycle found: {cycle}")
    else:
        messagebox.showinfo("✅ No Deadlock", "No deadlock detected!")

def reset_ui():
   
    global edges
    edges = reset_dependencies()
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

tk.Button(root, text="➕ Add Dependency", command=add_dependency_ui).pack()
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack()

tk.Button(root, text="🔍 Check Deadlock", command=check_deadlock_ui).pack()
tk.Button(root, text="🔄 Reset", command=reset_ui).pack()

root.mainloop()
