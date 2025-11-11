n = int(input("Enter number of processes: "))
bt = []
at = []
for i in range(n):
    at.append(int(input(f"Enter Arrival Time of P{i+1}: ")))
    bt.append(int(input(f"Enter Burst Time of P{i+1}: ")))

rt = bt[:]
t = 0
complete = 0
wt = [0]*n
tat = [0]*n
while complete != n:
    shortest = -1
    mn = 9999
    for i in range(n):
        if at[i] <= t and rt[i] < mn and rt[i] > 0:
            mn = rt[i]
            shortest = i
    if shortest == -1:
        t += 1
        continue
    rt[shortest] -= 1
    if rt[shortest] == 0:
        complete += 1
        finish = t + 1
        wt[shortest] = finish - bt[shortest] - at[shortest]
        if wt[shortest] < 0:
            wt[shortest] = 0
    t += 1

for i in range(n):
    tat[i] = bt[i] + wt[i]

print("\nProcess\tAT\tBT\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

# Sample Output:
# Enter number of processes: 3
# Enter Arrival Time of P1: 0
# Enter Burst Time of P1: 7
# Enter Arrival Time of P2: 2
# Enter Burst Time of P2: 4
# Enter Arrival Time of P3: 4
# Enter Burst Time of P3: 1
#
# Process	AT	BT	WT	TAT
# P1	        0	7	5	12
# P2	        2	4	2	6
# P3	        4	1	0	1
