from random import randint

class Train :

    def __init__(self, Train_No):
        self.Train_No = Train_No

    def book_ticket (self  , From , To ):
        print(f"ticket is booked in train no is : {self.Train_No} from {From} to {To}")
    
    def Get_Status (self):
        print(f"Your train : {self.Train_No} is running on time as expected ")

    def Fare_Info (self , From , To):
        print(f"ticket fare your train no is : {self.Train_No} from {From} to {To} is {randint(222 , 5555)} Rupees ") 


t = int ( input ( " Enter your Train No : "))

t=Train(t)

t.book_ticket (" Jaipur " , " Delhi ")

t.Get_Status()

t.Fare_Info ( " Jaipur " , " Delhi ")