# Machine Operation Table (Opcode values)
MOT = {
    "STOP": 0,
    "ADD": 1,
    "SUB": 2,
    "MULT": 3,
    "MOVER": 4,
    "MOVEM": 5,
    "COMP": 6,
    "BC": 7,
    "DIV": 8,
    "READ": 9,
    "PRINT": 10
}

# Registers (for simplicity)
REG = {
    "AREG": 1,
    "BREG": 2,
    "CREG": 3,
    "DREG": 4
}

# Symbol Table (from Pass-I)
SYMTAB = {
    "LOOP": 100,
    "A": 104,
    "B": 105,
    "C": 106
}

# Assembly Code
assembly_code = [
    "LOOP   MOVER  AREG, ='5'",
    "       ADD    BREG, ='1'",
    "       SUB    CREG, ='2'",
    "       STOP",
    "A      DC     5",
    "B      DS     1",
    "C      DS     1"
]

# Pass-II: Generate Machine Code
LOCCTR = 100
object_code = []

for line in assembly_code:
    parts = line.split()
    if len(parts) == 0:
        continue
    
    # Remove label if present
    if parts[0] in SYMTAB:
        parts = parts[1:]
    
    instr = parts[0]
    
    if instr in MOT:
        opcode = MOT[instr]
        if instr == "STOP":
            code = f"{opcode:02d} 00 00"
        else:
            reg = REG[parts[1].replace(",", "")]
            operand = parts[2]
            
            # Check if operand is constant or symbol
            if operand.startswith("='"):
                value = operand.strip("='")
                address = value  # store immediate value directly
            else:
                address = SYMTAB[operand]
            
            code = f"{opcode:02d} {reg:02d} {address:03d}"
        object_code.append((LOCCTR, code))
        LOCCTR += 1
    
    elif instr == "DC":
        value = parts[1]
        object_code.append((LOCCTR, f"00 00 {value}"))
        LOCCTR += 1
    
    elif instr == "DS":
        size = int(parts[1])
        for i in range(size):
            object_code.append((LOCCTR, "00 00 00"))
            LOCCTR += 1

# Print Machine Code
print("LOC\tObject Code")
for addr, code in object_code:
    print(f"{addr}\t{code}")
