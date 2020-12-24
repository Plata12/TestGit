p = {"Washing machine": {"GE": 950, "LG": 700},
     "Notebook": {"GE": 1450, "LG": 1500},
     "Microwave": {"GE": 450, "LG": 300},
     'Dish washer': {"GE": 550, "LG": 450},
     }
def buy():
    total = 0
    while True:
        a = input("select product : ").capitalize()
        b = input("select brand: ").upper()
        if a != "x".upper():
            n = p[a][b]
            total += int(n)
        else:
            break
    print("Total = {}".format(total))
buy()
