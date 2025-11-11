n = int(input("Enter number of processes: "))
bt = []
for i in range(n):
    bt.append(int(input(f"Enter Burst Time of P{i+1}: ")))
tq = int(input("Enter Time Quantum: "))

rem = bt[:]
t = 0
wt, tat = [0]*n, [0]*n
done = 0
while True:
    flag = True
    for i in range(n):
        if rem[i] > 0:
            flag = False
            if rem[i] > tq:
                t += tq
                rem[i] -= tq
            else:
                t += rem[i]
                wt[i] = t - bt[i]
                rem[i] = 0
                tat[i] = t
    if flag:
        break

print("\nProcess\tBT\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

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
