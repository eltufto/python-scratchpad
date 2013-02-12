import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        #runsuite.run(gui_interaction)
        print "entering run of thread"
        for i in range(10):
            print "thread loop # " + str(i)
        print "exiting thread"
        
thread = MyThread()
thread.start()
print "program finished"