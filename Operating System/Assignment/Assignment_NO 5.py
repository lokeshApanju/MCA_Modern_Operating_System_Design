# Disk Scheduling Algorithms: FCFS and SSTF
def fcfs_disk_scheduling(requests, head):
    total_seek = 0
    current = head
    print("FCFS Disk Scheduling")
    print("Head Movement:")
    for req in requests:
        movement = abs(req - current)
        total_seek += movement
        print(f"{current} -> {req}  (Seek = {movement})")
        current = req
    return total_seek

def sstf_disk_scheduling(requests, head):
    total_seek = 0
    current = head
    pending = requests.copy()
    print("\nSSTF Disk Scheduling")
    print("Head Movement:")

    while pending:
        nearest = min(pending, key=lambda x: abs(x - current))
        movement = abs(nearest - current)
        total_seek += movement
        print(f"{current} -> {nearest}  (Seek = {movement})")
        current = nearest
        pending.remove(nearest)
    return total_seek

# Fixed Disk Request Queue and Initial Head Position
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
# FCFS Execution
fcfs_seek = fcfs_disk_scheduling(requests, head)
print("Total Seek Time (FCFS):", fcfs_seek)
# SSTF Execution
sstf_seek = sstf_disk_scheduling(requests, head)
print("Total Seek Time (SSTF):", sstf_seek)
