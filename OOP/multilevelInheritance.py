#Multilevel inheritance is when a class is derived 
# from another derived class, forming a chain of inheritance.

class Device:
    def power_on(self):
        print("Device is powered on")


class Phone(Device):
    def call(self):
        print("Calling someone...")


class SmartPhone(Phone):   # Multilevel
    def internet(self):
        print("Browsing the internet...")


# Object
sp = SmartPhone()

sp.power_on()
sp.call()
sp.internet()
