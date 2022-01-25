import threading
import random
import time

class Philosopher(threading.Thread):
    running = True

    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
    def next(self):
        while (self.running):
            time.sleep(30)
            print('Philosopher %s wants to eat.' % self.index)
            self.eat()
    def eat(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
        while self.running:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print('Philosopher %s changes forks.' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()
    def dining(self):
        print('Philosopher %s starts eating. ' % self.index)
        time.sleep(30)
        print('Philosopher %s finishes eating.' % self.index)

def main():
    forks = [threading.Semaphore() for n in range(5)]

    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5])
                    for i in range(5)]

    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher.running = False
    print("We are done.")


if __name__ == "__main__":
    main()