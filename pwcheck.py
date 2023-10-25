def strength(password):
    checks = {"nchar": False, "upper": False, "digit": False}

    if len(password) >= 8:
        checks["nchar"] = True

    for i in password:
        if i.isupper():
            checks["upper"] = True
        if i.isnumeric:
            checks["digit"] = True

    if sum(checks.values()) != 3:
        print("Weak password")

    if sum(checks.values()) == 3:
        print("Sufficently strong password")


pw = input("enter pw")

strength(pw)
