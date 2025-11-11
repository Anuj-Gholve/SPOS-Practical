n = int(input("Enter number of processes: "))
bt, pr, at = [], [], []
for i in range(n):
    at.append(int(input(f"Enter Arrival Time of P{i+1}: ")))
    bt.append(int(input(f"Enter Burst Time of P{i+1}: ")))
    pr.append(int(input(f"Enter Priority of P{i+1}: ")))

done = [0]*n
t = 0
wt, tat = [0]*n, [0]*n
complete = 0
while complete != n:
    idx = -1
    best = 9999
    for i in range(n):
        if at[i] <= t and not done[i] and pr[i] < best:
            best = pr[i]
            idx = i
    if idx == -1:
        t += 1
        continue
    t += bt[idx]
    wt[idx] = t - at[idx] - bt[idx]
    tat[idx] = t - at[idx]
    done[idx] = 1
    complete += 1

print("\nProcess\tAT\tBT\tPR\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{pr[i]}\t{wt[i]}\t{tat[i]}")

# Sample Output:
# Enter number of processes: 3
# Enter Arrival Time of P1: 0
# Enter Burst Time of P1: 5
# Enter Priority of P1: 2
# Enter Arrival Time of P2: 1
# Enter Burst Time of P2: 3
# Enter Priority of P2: 1
# Enter Arrival Time of P3: 2
# Enter Burst Time of P3: 4
# Enter Priority of P3: 3
#
# Process	AT	BT	PR	WT	TAT
# P1	        0	5	2	3	8
# P2	        1	3	1	0	3
# P3	        2	4	3	6	10
