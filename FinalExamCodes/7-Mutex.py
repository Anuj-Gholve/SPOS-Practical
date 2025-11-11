import threading, time, random

mutex = threading.Semaphore(1)
empty = threading.Semaphore(3)
full = threading.Semaphore(0)
buffer = []

def producer():
    for i in range(5):
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print("Produced:", item)
        mutex.release()
        full.release()
        time.sleep(1)

def consumer():
    for i in range(5):
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print("Consumed:", item)
        mutex.release()
        empty.release()
        time.sleep(1)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()

# Sample Output:
# Produced: 42
# Consumed: 42
# Produced: 75
# Consumed: 75
# Produced: 13
# Consumed: 13
