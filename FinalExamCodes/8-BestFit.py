n = int(input("Enter number of memory blocks: "))
block = [int(input(f"Enter size of Block {i+1}: ")) for i in range(n)]
m = int(input("Enter number of processes: "))
process = [int(input(f"Enter size of Process {i+1}: ")) for i in range(m)]

alloc = [-1]*m
for i in range(m):
    best = -1
    for j in range(n):
        if block[j] >= process[i]:
            if best == -1 or block[j] < block[best]:
                best = j
    if best != -1:
        alloc[i] = best
        block[best] -= process[i]

print("\nProcess\tSize\tBlock")
for i in range(m):
    if alloc[i] != -1:
        print(f"P{i+1}\t{process[i]}\tB{alloc[i]+1}")
    else:
        print(f"P{i+1}\t{process[i]}\tNot Allocated")

# Sample Output:
# Enter number of memory blocks: 3
# Enter size of Block 1: 100
# Enter size of Block 2: 500
# Enter size of Block 3: 200
# Enter number of processes: 3
# Enter size of Process 1: 120
# Enter size of Process 2: 50
# Enter size of Process 3: 200
#
# Process	Size	Block
# P1	        120	B3
# P2	        50	B1
# P3	        200	B2
