class calculator :


    def __init__(self , n ):
        self.n = n 
    
    @staticmethod
    def greet ():
        print( " Heyy welcome to the calculator app ")
    

    def Square (self):
        print(f" The Square of your number is {self.n*self.n} ")

    def Cube (self):
        print(f" The Cube of your number is {self.n*self.n*self.n} ")

    def SquareRoot (self):
        print(f" The square root of your number is {self.n**1/2} ")

a = int(input( "Enter a number : ")) 

n = calculator(a)

n.greet()
n.Square()
n.Cube()
n.SquareRoot()