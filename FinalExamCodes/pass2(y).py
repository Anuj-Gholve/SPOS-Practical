# MNT: Macro Name Table
mnt = {
    "INCR": 1   # Macro name : starting index in MDT
}

# MDT: Macro Definition Table
mdt = {
    1: "A 1",
    2: "MEND"
}

print("Enter the intermediate code (type 'END' to finish):")
intermediate = []
line = input().strip()
while line != "END":
    intermediate.append(line)
    line = input().strip()

expanded_code = []

for line in intermediate:
    words = line.split()
    if len(words) > 0 and words[0] in mnt:
        # Macro call found → expand using MDT
        index = mnt[words[0]]
        while mdt[index] != "MEND":
            expanded_code.append(mdt[index])
            index += 1
    else:
        # Normal line
        expanded_code.append(line)

print("\nExpanded Code after Pass-II:")
for line in expanded_code:
    print(line)
