class Customer:
    name = " "
    lastName = " "
    age = 0
    def addCart(self):
        print("Added product to", self.name,self.lastName,"'s cart")
customer1 = Customer()
customer1.name = "Pla"
customer1.lastName ="Johnson"
customer1.age = 38
customer1.addCart()

customer2 = Customer()
customer2.name = "Tom"
customer2.lastName ="Hank"
customer2.age = 65
customer2.addCart()

customer3 = Customer()
customer3.name = "Chris"
customer3.lastName ="Hamsworth"
customer3.age = 40
customer3.addCart()

customer4 = Customer()
customer4.name = "Brad"
customer4.lastName ="Pitt"
customer4.age = 55
customer4.addCart()

customer5 = Customer()
customer5.name = "Tony"
customer5.lastName ="Stark"
customer5.age = 57
customer5.addCart()
