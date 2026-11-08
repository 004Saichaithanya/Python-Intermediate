import threading

event = threading.Event()


def func():
    print("Waiting for the thread to trigger!..\n")
    event.wait()
    print("Welcome to the XYZ Function!\n")


t1 = threading.Thread(target=func)
t1.start()

x = input("Do you want to Trigger the event:(y/n)")
if x == "y":
    event.set()
