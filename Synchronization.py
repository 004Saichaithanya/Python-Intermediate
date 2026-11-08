import threading
import time

x = 256
lock = threading.Lock()


def double():
    global x, lock
    lock.acquire()
    while x < 1024:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached Maximum Limit!")
    lock.release()


def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached Minimum Limit!")
    lock.release()


t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)
t1.start()
t2.start()
