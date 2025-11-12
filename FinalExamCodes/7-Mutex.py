class Synchronization:
    def __init__(self):  
        self.a = [0] * 10
        self.mutex = [1]
        self.empty = [10]
        self.full = [0]
        self.in_ = [0]  
        self.out = [0]

    def wait(self, x):
        if x[0] > 0:
            x[0] -= 1

    def signal(self, x):
        x[0] += 1

    def producer(self):
        if self.empty[0] > 0 and self.mutex[0] == 1:
            self.wait(self.empty)
            self.wait(self.mutex)
            data = int(input("Data to be produced: "))
            self.a[self.in_[0]] = data
            self.in_[0] = (self.in_[0] + 1) % 10
            self.signal(self.mutex)
            self.signal(self.full)
        else:
            print("Buffer is full, cannot produce!")

    def consumer(self):
        if self.full[0] > 0 and self.mutex[0] == 1:
            self.wait(self.full)
            self.wait(self.mutex)
            print("Data consumed is:", self.a[self.out[0]])
            self.out[0] = (self.out[0] + 1) % 10
            self.signal(self.mutex)
            self.signal(self.empty)
        else:
            print("Buffer is empty, cannot consume!")

def main():
    s = Synchronization()
    while True:
        print("\n1. Producer\n2. Consumer\n3. Exit")
        fchoice = int(input("Enter your choice: "))
        if fchoice == 1:
            s.producer()
        elif fchoice == 2:
            s.consumer()
        elif fchoice == 3:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__": 
    main()
