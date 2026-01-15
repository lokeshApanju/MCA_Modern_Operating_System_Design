# FCFS (First Come First Serve) cpu scheduling algorithm
def fcfs(processes):
    time = 0
    print("FCFS Scheduling")
    for p in processes:
        print(f"Process {p[0]} runs from {time} to {time + p[1]}")
        time += p[1]
# (Process ID, Burst Time)
processes = [("P1", 5), ("P2", 3), ("P3", 8)]
fcfs(processes)

# SJF (Shortest Job First) cpu scheduling algorithm
def sjf(processes):
    time = 0
    processes = sorted(processes, key=lambda x: x[1])  # Sort by burst time
    print("\nSJF Scheduling")
    for p in processes:
        print(f"Process {p[0]} runs from {time} to {time + p[1]}")
        time += p[1]
processes = [("P1", 5), ("P2", 3), ("P3", 8)]
sjf(processes)

# Round Robin cpu scheduling algorithm
def round_robin(processes, quantum):
    time = 0
    queue = processes.copy()
    print("\nRound Robin Scheduling")
    
    while queue:
        p = queue.pop(0)
        if p[1] > quantum:
            print(f"Process {p[0]} runs from {time} to {time + quantum}")
            time += quantum
            queue.append((p[0], p[1] - quantum))
        else:
            print(f"Process {p[0]} runs from {time} to {time + p[1]}")
            time += p[1]
processes = [("P1", 5), ("P2", 3), ("P3", 8)]
round_robin(processes, quantum=4)

# Priority Scheduling cpu scheduling algorithm
def priority_scheduling(processes):
    time = 0
    processes = sorted(processes, key=lambda x: x[2])  # Sort by priority
    print("\nPriority Scheduling")
    for p in processes:
        print(f"Process {p[0]} runs from {time} to {time + p[1]}")
        time += p[1]
# (Process ID, Burst Time, Priority)
processes = [("P1", 5, 2), ("P2", 3, 1), ("P3", 8, 3)]
priority_scheduling(processes)