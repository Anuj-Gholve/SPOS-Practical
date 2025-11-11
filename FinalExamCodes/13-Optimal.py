pages = list(map(int, input("Enter page reference string (space separated): ").split()))
frames = int(input("Enter number of frames: "))

s, faults = [], 0
for i in range(len(pages)):
    p = pages[i]
    if p not in s:
        if len(s) < frames:
            s.append(p)
        else:
            farthest, idx = -1, -1
            for j in range(len(s)):
                if s[j] not in pages[i+1:]:
                    idx = j
                    break
                else:
                    pos = pages[i+1:].index(s[j])
                    if pos > farthest:
                        farthest, idx = pos, j
            s[idx] = p
        faults += 1
    print("Frames:", s)

print("Total Page Faults:", faults)

# Sample Output:
# Enter page reference string (space separated): 7 0 1 2 0 3 0 4
# Enter number of frames: 3
# Frames: [7]
# Frames: [7, 0]
# Frames: [7, 0, 1]
# Frames: [2, 0, 1]
# Frames: [2, 0, 1]
# Frames: [2, 0, 3]
# Frames: [2, 0, 3]
# Frames: [4, 0, 3]
# Total Page Faults: 6
