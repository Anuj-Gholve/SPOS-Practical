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

# SJF Non-preemptive Scheduling
def sjf_non_preemptive(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    is_completed = [False] * n
    while completed != n:
        idx = -1
        min_burst = float('inf')
        for i in range(n):
            if processes[i].arrival <= current_time and not is_completed[i]:
                if processes[i].burst < min_burst:
                    min_burst = processes[i].burst
                    idx = i
                elif processes[i].burst == min_burst:
                    if processes[i].arrival < processes[idx].arrival:
                        idx = i
        if idx != -1:
            processes[idx].start_time = current_time
            current_time += processes[idx].burst
            processes[idx].completion = current_time
            processes[idx].turnaround = processes[idx].completion - processes[idx].arrival
            processes[idx].waiting = processes[idx].turnaround - processes[idx].burst
            is_completed[idx] = True
            completed += 1
        else:
            current_time += 1
    print("\nSJF Non-Preemptive Scheduling:")
    print("PID\tArrival\tBurst\tCompletion\tWaiting\tTurnaround")
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
    sjf_non_preemptive(processes)

if __name__ == "__main__":
    main()