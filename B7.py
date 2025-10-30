# Page Replacement Algorithms Simulation
# Algorithms: Least Recently Used (LRU) and Optimal

ref_string = [0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1]
current_pages = []
last_used = []
hit = 0
miss = 0


def find_LRU(window):
    """Find the least recently used page index."""
    min_index = 0
    for i in range(1, window):
        if last_used[i] < last_used[min_index]:
            min_index = i
    return min_index


def LRU(window):
    """Simulate the LRU page replacement algorithm."""
    global hit, miss, current_pages, last_used

    hit = 0
    miss = 0
    current_pages = [-1] * window
    last_used = [-1] * window
    length = len(ref_string)

    for i in range(length):
        page = ref_string[i]
        hit_flag = False

        # Check if page already in memory
        for j in range(window):
            if current_pages[j] == page:
                hit += 1
                hit_flag = True
                last_used[j] = i  # Update last used time
                break

        # Page fault (miss)
        if not hit_flag:
            miss += 1
            empty_found = False

            # Check for empty frame
            for j in range(window):
                if current_pages[j] == -1:
                    current_pages[j] = page
                    last_used[j] = i
                    empty_found = True
                    break

            # If no empty frame, replace LRU page
            if not empty_found:
                lru_index = find_LRU(window)
                current_pages[lru_index] = page
                last_used[lru_index] = i

    print("\n----- LRU -----")
    print(f"Number of hits: {hit}")
    print(f"Number of misses: {miss}")


def find_Optimal(current_index, window):
    """Find the page to replace using the Optimal algorithm."""
    farthest = current_index
    max_index = -1
    length = len(ref_string)

    for i in range(window):
        page = current_pages[i]
        found = False

        for j in range(current_index + 1, length):
            if page == ref_string[j]:
                found = True
                if j > farthest:
                    farthest = j
                    max_index = i
                break

        # If page is never used again
        if not found:
            return i

    return max_index if max_index != -1 else 0


def Optimal(window):
    """Simulate the Optimal page replacement algorithm."""
    global hit, miss, current_pages

    hit = 0
    miss = 0
    current_pages = [-1] * window
    length = len(ref_string)

    for i in range(length):
        page = ref_string[i]
        hit_flag = False

        # Check if page is already in memory
        for j in range(window):
            if current_pages[j] == page:
                hit += 1
                hit_flag = True
                break

        # Page fault (miss)
        if not hit_flag:
            miss += 1
            empty_found = False

            # Check for empty frame
            for j in range(window):
                if current_pages[j] == -1:
                    current_pages[j] = page
                    empty_found = True
                    break

            # If no empty frame, use Optimal replacement
            if not empty_found:
                optimal_index = find_Optimal(i, window)
                current_pages[optimal_index] = page

    print("\n----- OPTIMAL -----")
    print(f"Number of hits: {hit}")
    print(f"Number of misses: {miss}")


def display(window):
    """Display the current pages in memory."""
    print("\nCurrent pages are:", current_pages[:window])


def main():
    window = int(input("Enter window size: "))
    LRU(window)
    display(window)
    Optimal(window)
    display(window)


if __name__ == "__main__":
    main()
