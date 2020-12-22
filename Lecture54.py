usernameInput = input("username : ")
passwordInput = input("password : ")
while usernameInput != "HawaiiThai" or passwordInput != "234484":
    print("Try again!!")
    usernameInput = input("username : ")
    passwordInput = input("password : ")
    print("Good Job! You're in!")

def productList():
    print("---*---Hawaii Thai Warehouse---*---")
    print("1. Thai Massage Table")
    print("2. Swedish Massage Table")
    print("3. Herbal balls kit")
    print("4. Foot Massage kit")

def productSelected():
    userSelected = int(input(">>"))
    return userSelected

def taxCalculate(totalPrice):
    vat = 0.07
    result = totalPrice + (totalPrice * vat)
    return result
def priceCalculate():
    item1 = int(input("Thai Massage Table :"))
    item2 = int(input("Swedish Massage Table :"))
    item3 = int(input("Herbal Balla kit :"))
    item4 = int(input("Foot Massage kit :"))

    return taxCalculate(item1 + item2 + item3 + item4)
print(priceCalculate())

print("THANK YOU. Have a wonderful day!")






