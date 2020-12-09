#!/usr/bin/python3
import threading
import random
import time

deadlock = True

'''
Class philosopher which define each philosopher.
'''
class Philosopher(threading.Thread):
    def __init__(self, name, LeftFork, RightFork):
        threading.Thread.__init__(self)
        self.name = name
        self.LeftFork = LeftFork
        self.RightFork = RightFork

    def run(self):
        while 1:
            print(f'{self.name} is thinking about our destiny.')
            time.sleep(random.uniform(3, 13))
            print(f'{self.name} Want to eat dinner')
            self.tryGetForks()

    '''
    Method describe how philosopher take forks to eat dinner
    '''
    def tryGetForks(self):
        Lfork, Rfork = self.LeftFork, self.RightFork

        while True:
            Lfork.acquire(True)
            locked = Rfork.acquire(False)
            if locked:
                break
            if deadlock is False:
                Lfork.release()
                print(f'{self.name} changes destiny')
                Lfork, Rfork = Rfork, Lfork
            else:
                print(f'{self.name} waiting for fork ')

        self.eating()
        Rfork.release()
        Lfork.release()

    '''
    Method describe eat process 
    '''
    def eating(self):
        print(f'{self.name} starts eating')
        time.sleep(random.uniform(1, 10))
        print(f'{self.name} Mmmm, delicious dinner, so what I was thinking about?')


def Test():
    forks = [threading.Lock() for n in range(5)]
    names = ('Immanuel Kant', 'Carl Gustav Jung', 'Arystoteles', 'Schopenhauer', 'Benedykt XVI')
    philosophers = [Philosopher(names[i], forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

    random.seed(1234321)
    for p in philosophers:
        p.start()

if __name__ == "__main__":
    Test()