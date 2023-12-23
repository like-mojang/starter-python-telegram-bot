import uvicorn
import threading

class a(threading.Thread):
    def __init__(self):
        super(a, self).__init__()
    def run(self):
        import main

d=a()
d.start()



