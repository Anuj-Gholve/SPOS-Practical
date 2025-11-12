mnt = []   # Macro Name Table
mdt = []   # Macro Definition Table

print("Enter the macro code (type 'END' to finish):")

line = input().strip()

while line != "END":
    if line == "MACRO":
        name = input("Macro name: ").strip()
        mnt.append([name, len(mdt)+1])  # pointer to MDT start
        line = input().strip()
        while line != "MEND":
            mdt.append(line)
            line = input().strip()
        mdt.append("MEND")
    line = input().strip()

print("\nMNT (Macro Name Table):")
print("Name\tMDT Index")
for i in range(len(mnt)):
    print(mnt[i][0], "\t", mnt[i][1])

print("\nMDT (Macro Definition Table):")
for i in range(len(mdt)):
    print(i+1, "\t", mdt[i])
