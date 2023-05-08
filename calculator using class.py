class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    def result(self):
       print("result will be" + self.add,self.sub,self.mul,self.div)
num1 = int(input("eneter the 1st number:"))
num2 = int(input("enter the 2nd number:"))
obj = Calculator(num1,num2)

while True:
    def fun():
        print("1.addition\n","2.subtraction\n","3.multiplication\n","4.division\n")
    choice  = int(input("enter your choice:"))
   
    if choice == 1:
        print("addition of 2 number is",obj.add())
    elif choice == 2:
        print("addition of 2 number is",obj.sub())
    elif choice == 3:
        print("addition of 2 number is",obj.mul())
    elif choice == 4:
        print("addition of 2 number is",obj.div())
    else:
        print("Enter the correct choice!")
     

    

