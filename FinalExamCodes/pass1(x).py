# OPCODE TABLE (MOT) - Machine Operation Table
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

# DIRECTIVES
DIRECTIVES = ["START", "END", "DC", "DS"]

# Symbol Table
SYMTAB = {}

# Location Counter
LOCCTR = 0

# Read assembly code
assembly_code = [
    "START 100",
    "LOOP   MOVER  AREG, ='5'",
    "       ADD    BREG, ='1'",
    "       SUB    CREG, ='2'",
    "       STOP",
    "A      DC     5",
    "B      DS     1",
    "C      DS     1",
    "END"
]

# Pass-I Implementation
for line in assembly_code:
    parts = line.split()
    
    if len(parts) == 0:
        continue
    
    # Handle START directive
    if parts[0] == "START":
        LOCCTR = int(parts[1])
        print(f"START at address {LOCCTR}")
        continue
    
    # Handle END directive
    if parts[0] == "END":
        print("END of program")
        break
    
    # Check if first part is a label
    if parts[0] not in MOT and parts[0] not in DIRECTIVES:
        label = parts[0]
        SYMTAB[label] = LOCCTR
        parts = parts[1:]  # Remove label from line
    
    # Process instruction or directive
    instr = parts[0]
    
    if instr in MOT:
        LOCCTR += 1  # Assume each instruction is 1 word
    elif instr == "DC":
        LOCCTR += 1
    elif instr == "DS":
        LOCCTR += int(parts[1])
    
# Print Symbol Table
print("\nSymbol Table (SYMTAB):")
for symbol, addr in SYMTAB.items():
    print(f"{symbol} -> {addr}")
