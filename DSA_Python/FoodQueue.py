import threading
from threading import Lock
from collections import deque
import time


class Hotel:
    def __init__(self):
        self.container = deque()
        self.lock = Lock()

    def place_order(self, item):
        with self.lock:
            print(f"{item} order confirmed successfully")
            self.container.appendleft(item)

    def serve_order(self):
        with self.lock:
            if self.container:
                print(f"{self.container.pop()} is sucessfully served to you!")
            else:
                print("No orders Yet!")
        time.sleep(5)


hotel = Hotel()
print("Place Orders:")
orders = ["pizza", "samosa", "pasta", "biryani", "burger", "gulabjamun"]
place_orders = []
for item in orders:
    thread = threading.Thread(target=hotel.place_order, args=(item,))
    place_orders.append(thread)
    thread.start()
    time.sleep(0.5)

for thread in place_orders:
    thread.join()


print("serve Orders:")
serve_orders = []
for _ in orders:
    thread = threading.Thread(target=hotel.serve_order)
    serve_orders.append(thread)
    thread.start()
    time.sleep(0.5)

for thread in serve_orders:
    thread.join()
