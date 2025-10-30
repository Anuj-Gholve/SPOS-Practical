import copy
from collections import deque

class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.remaining = burst
        self.completion = 0
        self.waiting = 0
        self.turnaround = 0
        self.start_time = -1

# Round Robin Scheduling (Non-preemptive)
def roundRobin(processes, quantum):
    time = 0
    completed = 0
    n = len(processes)
    gantt = []
    q = deque()
    visited = [False] * n
    while completed < n:
        for i in range(n):
            if processes[i].arrival <= time and not visited[i]:
                q.append(i)
                visited[i] = True
        if not q:
            gantt.append(-1)
            time += 1
            continue
        i = q.popleft()
        p = processes[i]
        exec_time = min(quantum, p.remaining)
        for _ in range(exec_time):
            gantt.append(p.pid)
        time += exec_time
        p.remaining -= exec_time
        for j in range(n):
            if processes[j].arrival <= time and not visited[j]:
                q.append(j)
                visited[j] = True
        if p.remaining == 0:
            completed += 1
            p.completion = time
        else:
            q.append(i)
    for p in processes:
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst
    print("\nRound Robin Scheduling (Non-preemptive) Gantt Chart:")
    for pid in gantt:
        if pid == -1:
            print("Idle | ", end="")
        else:
            print(f"P{pid} | ", end="")
    print("\n\nPID\tArrival\tBurst\tCompletion\tWaiting\tTurnaround")
    for p in processes:
        print(f"P{p.pid}\t{p.arrival}\t{p.burst}\t{p.completion}\t\t{p.waiting}\t{p.turnaround}")

def main():
    n = int(input("Enter number of processes: "))   
    processes = []
    for i in range(n):
        pid = i + 1
        print(f"\nProcess {pid}:")
        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))
        priority = int(input("Priority (lower number = higher priority): "))
        processes.append(Process(pid, arrival, burst, priority))
    quantum = int(input("Enter time quantum: "))
    roundRobin(processes, quantum)

if __name__ == "__main__":
    main()