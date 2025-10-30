import copy

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

# Priority Scheduling (Preemptive)
def priorityPreemptive(processes):
    time = 0
    completed = 0
    n = len(processes)
    gantt = []
    while completed < n:
        available = [p for p in processes if p.arrival <= time and p.remaining > 0]
        if available:
            current = min(available, key=lambda p: p.priority)
            gantt.append(current.pid)
            current.remaining -= 1
            time += 1
            if current.remaining == 0:
                completed += 1
                current.completion = time
        else:
            gantt.append(-1)
            time += 1
    for p in processes:
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst
    print("\nPriority Scheduling (Preemptive) Gantt Chart:")
    for pid in gantt:
        if pid == -1:
            print("Idle | ", end="")
        else:
            print(f"P{pid} | ", end="")
    print("\n\nPID\tArrival\tBurst\tPriority\tCompletion\tWaiting\tTurnaround")
    for p in processes:
        print(f"P{p.pid}\t{p.arrival}\t{p.burst}\t{p.priority}\t\t{p.completion}\t\t{p.waiting}\t{p.turnaround}")

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
    priorityPreemptive(processes)

if __name__ == "__main__":
    main()