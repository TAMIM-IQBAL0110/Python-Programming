# when the same operator is allowed to have different
# meaning according to the context
# dunder function : Double UNDERscore 
"""
| Operator  | Dunder Method    |
| --------- | ---------------- |
| `+`       | `__add__()`      |
| `-`       | `__sub__()`      |
| `*`       | `__mul__()`      |
| `/`       | `__truediv__()`  |
| `//`      | `__floordiv__()` |
| `%`       | `__mod__()`      |
| `**`      | `__pow__()`      |
| `==`      | `__eq__()`       |
| `!=`      | `__ne__()`       |
| `<`       | `__lt__()`       |
| `>`       | `__gt__()`       |
| `<=`      | `__le__()`       |
| `>=`      | `__ge__()`       |
| `len()`   | `__len__()`      |
| `print()` | `__str__()`      |
"""

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"+",self.img ,"j")
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
    
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2 # dunder function allow to + operation
num3.showNumber()

num4 = num1 - num2 
num4.showNumber()