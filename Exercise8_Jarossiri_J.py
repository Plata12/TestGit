usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "HawaiiThai" and passwordInput == "9722132334":
    print("WELCOME TO HAWAII THAI MASSAGE")
    print("---**---Hawaii Thai---**---")
    print("1. Thai Massage           $70")
    print("2. Swedish Massage        $70")
    print("3. Deep Tissue Massage    $70")
    print("4. Hot Stone Massage      $90")
    print("5. Aroma Massage          $90")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("price ($) "))
        result = price
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price :"))
        price2 = int(input("Second Product Price :"))
        result = price1+price2
        print(result)
    elif userSelected == 3:
        price1 = int(input("1st Product Price :"))
        price2 = int(input("2nd Product Price :"))
        price3 = int(input("3rd Product Price :"))
        result = price1+price2+price3
        print(result)
    elif userSelected == 4:
        price1 = int(input("1st Product Price :"))
        price2 = int(input("2nd Product Price :"))
        price3 = int(input("3rd Product Price :"))
        price4 = int(input("4th Product Price :"))
        result = price1+price2+price3+price4
        print(result)
    elif userSelected == 5:
        price1 = int(input("1st Product Price :"))
        price2 = int(input("2nd Product Price :"))
        price3 = int(input("3rd Product Price :"))
        price4 = int(input("4th Product Price :"))
        price5 = int(input("5th Product Price :"))
        result = price1+price2+price3+price4+price5
        print(result)

