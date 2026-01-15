# Banker's Algorithm for Deadlock Avoidance
def calculate_need(maximum, allocation):
    need = []
    for i in range(len(maximum)):
        need.append([maximum[i][j] - allocation[i][j] 
                     for j in range(len(maximum[0]))])
    return need


def is_safe_state(processes, allocation, need, available):
    work = available.copy()
    finish = [False] * processes
    safe_sequence = []

    while len(safe_sequence) < processes:
        found = False
        for i in range(processes):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(len(work))):
                    # Allocate resources
                    for j in range(len(work)):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(f"P{i}")
                    found = True
        if not found:
            return False, []

    return True, safe_sequence


# Number of processes and resources
processes = 5
resources = 3
# Allocation Matrix
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]
# Maximum Requirement Matrix
maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
# Available Resources
available = [3, 3, 2]
# Calculate Need Matrix
need = calculate_need(maximum, allocation)
print("Need Matrix:")
for row in need:
    print(row)
# Check for Safe State
safe, sequence = is_safe_state(processes, allocation, need, available)
if safe:
    print("\nSystem is in a SAFE state.")
    print("Safe Sequence:", " -> ".join(sequence))
else:
    print("\nSystem is in an UNSAFE state (Deadlock may occur).")
