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

# FCFS Scheduling
def fcfs(processes):
    n = len(processes)
    current_time = 0
    processes.sort(key=lambda p: p.arrival)
    for i in range(n):
        if current_time < processes[i].arrival:
            current_time = processes[i].arrival
        processes[i].start_time = current_time
        current_time += processes[i].burst
        processes[i].completion = current_time
        processes[i].turnaround = processes[i].completion - processes[i].arrival
        processes[i].waiting = processes[i].turnaround - processes[i].burst
    print("\nFCFS Scheduling:")
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
    fcfs(processes)

if __name__ == "__main__":
    main()