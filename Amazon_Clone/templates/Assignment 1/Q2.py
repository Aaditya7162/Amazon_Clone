class order:
    def __init__(self,OrderID,CustomerName,RestaurentName,Dist):
        self.OrderID=OrderID
        self.CustomerName=CustomerName
        self.RestaurentName=RestaurentName
        self.Dist=Dist

    def display(self):
        print(f"Order ID: {self.OrderID}")
        print(f"Customer Name: {self.CustomerName}")
        print(f"Restaurent Name: {self.RestaurentName}")
        print(f"Distance (in Kilometers): {self.Dist}")

class std(order):
    def charges(self):
        print(f"The charges of the order with standard delivery is ₹{40+self.Dist*10}")
class express(order):
    def charges(self):
            print(f"The charges of the order with express delivery is ₹{80+self.Dist*20}")
class premium(order):
    def charges(self):
             print(f"The charges of the order with premium delivery is ₹{120+self.Dist*30}")

ord1=std("A101","Rahul","The Taste of Amritsar",15)
ord2=express("A102","Neha","The Chinese Bowl",9)
ord3=premium("A103","Aaditya","Hangouts",19)
print("------------Standard Delivery------------")
ord1.display()
ord1.charges()
print("------------Express Delivery------------")
ord2.display()
ord2.charges()
print("------------Premium Delivery------------")
ord3.display()
ord3.charges()