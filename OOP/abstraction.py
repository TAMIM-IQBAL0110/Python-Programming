# Hiding the implementation details of a class and only
# showing the essential features to the user

class car:
    def ___init__(self):
        self.acc = False 
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("car is starting...")
    def stop(self):
        self.brk = True
        print("car is stop...")

car1 = car()
car1.start()
car1.stop()
