menuList = []

def showBill():
    print("----PKT Kitchen----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1], )

while True:
    menuName = input("Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])
showBill()