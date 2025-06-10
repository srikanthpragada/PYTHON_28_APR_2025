from threading import Thread
import threading

class PrintThread(Thread):
    def run(self):
        for n in range(1, 11):
            print(f"Child {n}")

print(threading.current_thread())
pt = PrintThread()
pt.start()

for n in range(1, 11):
    print(f"Main {n}")



