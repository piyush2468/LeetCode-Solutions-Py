from threading import Semaphore

class DiningPhilosophers:
    def __init__(self):
        #only one person can eat at a time
        self.dine = Semaphore(value = 1)

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        with self.dine:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
