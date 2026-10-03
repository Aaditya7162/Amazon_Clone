class package:
    def __init__(self,packID,CustomerName,dest,weight):
        self.packID=packID
        self.CustomerName=CustomerName
        self.dest=dest
        self.weight=weight
    def display(self):
        print(f"Package ID; {self.packID}")
        print(f"Customer Name: {self.CustomerName}")
        print(f"Destination: {self.dest}")
        print(f"Package weight in kilograms: {self.weight}")
    
class regular(package):
    def pricing(self):
        print(f"The pricing for regular package: ₹{50+self.weight*15}")
class fragile(package):
    def pricing(self):
        print(f"The pricing for fragile package: ₹{100+self.weight*25}")
class express(package):
    def pricing(self):
        print(f"The pricing for express package: ₹{150+self.weight*40}")
        
ord1=regular("P01","Priyal","Delhi",20)
ord2=fragile("P02","Ashish","West Bengal",34)
ord3=express("P03","Sneha","Gurgaon",5)
print("--------------Regular Pricing--------------")
ord1.display()
ord1.pricing()
print("--------------Fragile Pricing--------------")
ord2.display()
ord2.pricing()
print("--------------Express Pricing--------------")
ord3.display()
ord3.pricing()