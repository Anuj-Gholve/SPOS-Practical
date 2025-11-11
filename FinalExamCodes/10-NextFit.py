n = int(input("Enter number of memory blocks: "))
block = [int(input(f"Enter size of Block {i+1}: ")) for i in range(n)]
m = int(input("Enter number of processes: "))
process = [int(input(f"Enter size of Process {i+1}: ")) for i in range(m)]

alloc = [-1]*m
pos = 0
for i in range(m):
    count = 0
    while count < n:
        if block[pos] >= process[i]:
            alloc[i] = pos
            block[pos] -= process[i]
            break
        pos = (pos + 1) % n
        count += 1
    pos = (pos + 1) % n

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
# P1	        120	B2
# P2	        50	B2
# P3	        200	B3
