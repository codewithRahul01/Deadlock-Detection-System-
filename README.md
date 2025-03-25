Deadlock-Detection-System-
We will be using RAGs(Resource Allocation Graphs) to detect deadlocks by checking for cycles in the graph and maing it more viualized and user oriented using Python
Deadlock Detection System

 Overview
The Deadlock Detection System is a Python-based application that utilizes Resource Allocation Graphs (RAGs) to detect deadlocks in concurrent systems. By visualizing the process-resource interactions as a directed graph, the system identifies cycles in the graph structure, which indicate deadlocks.

 Features
- Graph-based Representation: Uses networkx to create a directed Resource Allocation Graph (RAG).
- Deadlock Detection: Implements cycle detection algorithms to identify deadlocks.
- User-friendly Visualization: Utilizes matplotlib for visualizing the allocation and request edges in the RAG.
- Interactive Interface: Allows users to dynamically add processes and resources and simulate resource allocation.
- Console-based Output: Provides clear feedback on deadlock status.

Technologies Used
- Python 3.x
- networkx (for graph representation and cycle detection)
- matplotlib (for visualization)
- tkinter (for GUI interface, if applicable)

 Installation
1. Clone the repository:
   
   git clone https://github.com/your-username/deadlock-detection-system.git
   cd deadlock-detection-system
   
2. Install required dependencies:
   
   pip install networkx matplotlib
   

## Usage
1. Run the Python script:
   
   python main.py
   
2. Enter process and resource allocations through the interface.
3. Click Check Deadlock to analyze the system.
4. The system will indicate whether a deadlock has been detected and visualize the resource allocation graph.

 Example
 Sample Allocation
| Process | Resource | Type |
|---------|---------|------|
| P1      | R1      | Allocated |
| P2      | R2      | Requested |
| P2      | R1      | Allocated |
| P1      | R2      | Requested |

Result: Deadlock detected due to a cycle in the RAG.

 Future Enhancements
- Implement real-time logging of deadlock occurrences.
- Provide recommendations to resolve deadlocks.
- Extend support for different deadlock prevention strategies.

 License
This project is licensed under the MIT License - see the LICENSE file for details.

 Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

---
Developed by Vaibhav Mohanty, Shubhaayu Madan, Rahul Jangra
