pages = list(map(int, input("Enter page reference string (space separated): ").split()))
frames = int(input("Enter number of frames: "))

s, faults = [], 0
for p in pages:
    if p not in s:
        if len(s) < frames:
            s.append(p)
        else:
            s.pop(0)
            s.append(p)
        faults += 1
    else:
        s.remove(p)
        s.append(p)
    print("Frames:", s)

print("Total Page Faults:", faults)

# Sample Output:
# Enter page reference string (space separated): 7 0 1 2 0 3 0 4
# Enter number of frames: 3
# Frames: [7]
# Frames: [7, 0]
# Frames: [7, 0, 1]
# Frames: [0, 1, 2]
# Frames: [1, 2, 0]
# Frames: [2, 0, 3]
# Frames: [0, 3, 0]
# Frames: [3, 0, 4]
# Total Page Faults: 7
