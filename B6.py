# Memory Allocation Strategies in Python

original_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
blk_size = len(original_blocks)
pr_size = len(processes)


def reset_blocks():
    return original_blocks.copy()


def first_fit():
    blocks = reset_blocks()
    print("\nFIRST FIT:")
    for p in processes:
        allocated = False
        for j in range(blk_size):
            if blocks[j] >= p:
                blocks[j] -= p
                print(f"Process {p} has been allocated to block {j + 1}")
                allocated = True
                break
        if not allocated:
            print(f"Process {p} has not been allocated.")


def next_fit():
    blocks = reset_blocks()
    print("\nNEXT FIT:")
    j = 0
    for p in processes:
        allocated = False
        count = 0
        while count < blk_size:
            if blocks[j] >= p:
                blocks[j] -= p
                print(f"Process {p} has been allocated to block {j + 1}")
                j = (j + 1) % blk_size
                allocated = True
                break
            j = (j + 1) % blk_size
            count += 1
        if not allocated:
            print(f"Process {p} has not been allocated.")


def best_fit():
    blocks = reset_blocks()
    print("\nBEST FIT:")
    for p in processes:
        best_idx = -1
        min_waste = float('inf')
        for j in range(blk_size):
            waste = blocks[j] - p
            if waste >= 0 and waste < min_waste:
                min_waste = waste
                best_idx = j
        if best_idx != -1:
            blocks[best_idx] -= p
            print(f"Process {p} was allocated to block {best_idx + 1}")
        else:
            print(f"Process {p} was not allocated to any block.")


def worst_fit():
    blocks = reset_blocks()
    print("\nWORST FIT:")
    for p in processes:
        worst_idx = -1
        max_waste = -1
        for j in range(blk_size):
            waste = blocks[j] - p
            if waste >= 0 and waste > max_waste:
                max_waste = waste
                worst_idx = j
        if worst_idx != -1:
            blocks[worst_idx] -= p
            print(f"Process {p} was allocated to block {worst_idx + 1}")
        else:
            print(f"Process {p} was not allocated to any block.")


def main():
    while True:
        print("\n\nMemory Allocation Strategies Menu:")
        print("1. First Fit")
        print("2. Next Fit")
        print("3. Best Fit")
        print("4. Worst Fit")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            first_fit()
        elif choice == '2':
            next_fit()
        elif choice == '3':
            best_fit()
        elif choice == '4':
            worst_fit()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":  # ✅ Fixed "__name__"
    main()