#Create student class that takes name & 
# marks of 3 subjects as arguments in  constructor.

class student:
    def __init__(self,name,phy,math,chemistry):
        self.name = name
        self.phy = phy
        self.math = math
        self.chemistry = chemistry
    def marksAverage(self):
        avg = (self.phy+ self.math + self.chemistry)/3
        print(f"average marks:{avg}")

class student2:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def marksAverage(self):
        sum = 0
        for val in self.marks:
            sum+=val
        avg = sum/3
        print(f"average marks:{avg}")
        

s1 = student('tamim', 90,94,89)
s1.marksAverage()

s2 = student2('tamim',[90,94,89])
s2.marksAverage()
        