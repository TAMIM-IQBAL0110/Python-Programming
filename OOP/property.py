#We use @property decorator on any method in the class to 
# use the as property

class person:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy+self.chem+self.math)/3)+"%"

p1 = person(98,90,95)
print(p1.percentage)
p1.phy = 94
print(p1.percentage) # percentage not changed 

# to solve this issue we can define method except property
# and call it 
# but have better solution -> property decorator

class person1:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = 
    
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
p2 = person1(98,90,95)
print(p2.percentage)
p2.phy = 94
print(p2.percentage) # percentage is now calculated based on latest marks