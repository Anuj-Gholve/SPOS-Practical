n = int(input("Enter number of processes: "))

at = []  # Arrival times
bt = []  # Burst times
for i in range(n):
    at.append(int(input(f"Enter Arrival Time of P{i+1}: ")))
    bt.append(int(input(f"Enter Burst Time of P{i+1}: ")))

tq = int(input("Enter Time Quantum: "))
rem = bt[:] 
t = 0
wt, tat = [0]*n, [0]*n
ready_queue = []
visited = [False]*n
completed = 0

while completed < n:
    for i in range(n):
        if at[i] <= t and not visited[i]:
            ready_queue.append(i)
            visited[i] = True

    if not ready_queue:
        t += 1  
        continue

    i = ready_queue.pop(0)  

    if rem[i] > tq:
        rem[i] -= tq
        t += tq
    else:
        t += rem[i]
        rem[i] = 0
        tat[i] = t - at[i]
        wt[i] = tat[i] - bt[i]
        completed += 1

    for j in range(n):
        if at[j] <= t and not visited[j]:
            ready_queue.append(j)
            visited[j] = True

    if rem[i] > 0:
        ready_queue.append(i)

print("\nProcess\tAT\tBT\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

# Sample Output:
# Enter number of processes: 3
# Enter Burst Time of P1: 5
# Enter Burst Time of P2: 3
# Enter Burst Time of P3: 1
# Enter Time Quantum: 2
#
# Process	BT	WT	TAT
# P1	        5	4	9
# P2	        3	4	7
# P3	        1	2	3

